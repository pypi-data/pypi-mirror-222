from pickled_carrots.waveforms import hsf_to_obspy
from uquake.core import read, read_events, read_inventory
import hashlib
from pickled_carrots.waveforms import HeaderLookups
from uquake.core.stream import Stream, Trace
from uquake.core.inventory import (Inventory, Network, Station, Channel,
                                   SystemResponse, Equipment)
from uquake.core.event import Catalog
from pickled_carrots.vinegar import event
import numpy as np
from pathlib import Path
from importlib import reload
import tarfile
from io import BytesIO
import tempfile
from pickled_carrots import waveforms
from uquake.core.data_ensemble import SeismicDataEnsemble
reload(event)

lookups = HeaderLookups()


class HSFHandler(object):
    def __init__(self, st, header, network, experimental=False):
        self.st = Stream(st)
        self.header = header
        self.network_code = network
        self.experimental = experimental

    @classmethod
    def from_hsf_file(cls, hsf_path, network):
        st, header = hsf_to_obspy(hsf_path, print_out=False,
                                  experimental=False,
                                  groundmotion=False, return_head=True)
        return cls(st, header, network, experimental=False)

    @property
    def event_type(self):
        ev_type = self.header['evtype']
        if ev_type < 12:
            return self.event_type_look_up[ev_type]
        else:
            return chr(ev_type)

    @property
    def event_type_look_up(self):
        return ['seismic event', 'bast', 'rock burst', 'casing failure', 'background',
                'noise', 'custom 1', 'custom 2', 'custom 3', 'unknown event',
                'sgm event', 'duplicate']

    @property
    def int_stream(self):
        # converting from voltage to integer
        for i, tr in enumerate(self.st.copy()):
            tr.data = (tr.data * 2 ** self.header['nbit']).astype(int)

    @property
    def alternate_station_codes(self):
        station_codes = []
        for station_name in self.header['ch_descr']:
            station_codes.append(station_name_converter(station_name))

        return station_codes

    @property
    def station_codes(self):
        return self.header['ch_descr']

    @property
    def location_codes(self):
        site_list = []
        locations = []
        for tr, station_name in zip(self.st, self.station_codes):
            # station_name = tr.stats.station
            station_code = station_name_converter(station_name)
            location = 1
            channel_code = tr.stats.channel
            site_code = generate_site_code(station_code, location,
                                           channel_code)
            while site_code in site_list:
                location += 1
                site_code = generate_site_code(station_code, location,
                                               channel_code)

            site_list.append(site_code)
            locations.append(location)
        return locations

    @property
    def gain(self):
        return self.header['gain']

    @property
    def sensitivity(self):
        return expand_list(self.header['snstvt'], self.header['ch_descr'])

    @property
    def component_map(self):
        component_map = {'E': '1',
                         'N': '2',
                         'Z': '3',
                         'X': '1',
                         'Y': '2',
                         'Z': '3'}
        return component_map

    @property
    def channel_code_map(self):
        channel_code = {'GEOPHONE': 'GP',
                        'SGM_GEOPHONE': 'GP',
                        'ACCELEROMETER': 'GN',
                        'FBA_ACCELEROMETER': 'SN'}
        return channel_code

    @property
    def sensor_types(self):
        sensor_types = []
        previous_code = self.station_codes[0]
        i = 0
        for station_code in self.station_codes:
            if station_code != previous_code:
                previous_code = station_code
                i += 1
            sensor_types.append(self.header['stype'][i])
        return sensor_types

    @property
    def channel_codes(self):
        channels = []
        previous_code = self.station_codes[0]
        i = 0
        # for tr, stype in zip(self.st, self.header['stype']):
        stypes = self.sensor_types
        for station_code, tr in zip(self.station_codes, self.st):
            if station_code != previous_code:
                previous_code = station_code
                i += 1
            channel = self.channel_code_map[lookups.sensor_types[stypes[i]]]
            if tr.stats.channel[-1].upper() in self.component_map.keys():
                component = self.component_map[tr.stats.channel[-1].upper()]
            else:
                component = tr.stats.channel[-1].upper()
            channel += component
            channels.append(channel)

        return channels

    @property
    def channels(self):
        channels = {}
        for station_code in self.station_codes:
            channels[station_code] = []
        channel_codes = self.channel_codes
        location_codes = self.location_codes
        slocs = self.sensor_locations
        stypes = self.sensor_types
        sensor_orientations = self.sensor_orientations
        resonant_frequency = self.sensor_resonance_frequencies
        for i, station_code in enumerate(self.station_codes):
            sensor_type = lookups.sensor_types[stypes[i]]
            location_code = f'{location_codes[i]:02d}'
            sensor = Equipment(type=sensor_type, description='sensor',
                               manufacturer='ESG', vendor='ESG')
            digitizer = Equipment(type='Paladin',
                                  description='data acquisition',
                                  manufacturer='ESG', vendor='ESG')
            sr = SystemResponse()
            if 'GEOPHONE' in sensor_type:
                sr.add_geophone(resonant_frequency[i], 1)
            else:
                sr.add_accelerometer(2300, 1)

            channel = Channel(code=channel_codes[i],
                              location_code=location_code,
                              x=slocs[i][0], y=slocs[i][1], z=slocs[i][2],
                              types=['CONTINUOUS'],
                              sample_rate=self.st[i].stats.sampling_rate,
                              sensor=sensor, data_logger=digitizer,
                              response=sr.response)
            channel.set_orientation(sensor_orientations[i])
            channels[station_code].append(channel)
        return channels

    @property
    def stations(self):
        stations = []
        channels = self.channels
        i = np.unique(self.station_codes, return_index=True)[1]
        station_codes = np.array(self.station_codes)[i]
        alternate_station_code = np.array(self.alternate_station_codes)[i]
        for i in range(len(station_codes)):
            station = Station(code=station_codes[i],
                              channels=channels[station_codes[i]],
                              alternate_code=alternate_station_code[i])
            stations.append(station)
        return stations

    @property
    def network(self):
        return Network(code=self.network_code, stations=self.stations)

    @property
    def inventory(self):
        return Inventory(networks=[self.network])

    @property
    def sensor_locations(self):
        previous_code = self.station_codes[0]
        sensor_locations = []
        i = 0
        for station_code in self.station_codes:
            if station_code != previous_code:
                i += 1
                previous_code = station_code
            sensor_locations.append(self.header['pos'][i])

        return sensor_locations

    @property
    def sensor_resonance_frequencies(self):
        return self.header['low_f']

    def sensor_high_frequencies(self):
        return self.header['high_f']

    @property
    def sensor_orientations(self):
        previous_code = self.station_codes[0]
        sensor_orientations = []
        i = 0
        j = 0
        for station_code in self.station_codes:
            if station_code != previous_code:
                i += 1
                j = 0
                previous_code = station_code
            sensor_orientations.append(self.header['sen_rot'][i][j])
            j += 1
        return sensor_orientations

    @property
    def alternate_names(self):
        return [tr.stats.station for tr in self.st]

    @property
    def stream(self):
        st_out = Stream()
        for tr, station, location, channel in \
                zip(self.st, self.station_codes, self.location_codes,
                    self.channel_codes):
            tr_out = Trace()
            tr_out.data = tr.data
            tr_out.stats.sampling_rate = tr.stats.sampling_rate
            tr_out.stats.starttime = tr.stats.starttime
            tr_out.stats.network = self.network_code
            tr_out.stats.station = station
            tr_out.stats.location = f'{location:02d}'
            tr_out.stats.channel = channel
            st_out.traces.append(tr_out)

        return st_out

    @property
    def event(self):
        for tr, tr2 in zip(self.st, self.stream):
            tr.stats.station = tr2.stats.station
            tr.stats.location = tr2.stats.location
            tr.stats.channel = tr2.stats.channel

        evt = event.create_event(self.st, self.header, self.network_code)
        for i in range(len(evt.preferred_origin().arrivals)):
            evt.preferred_origin().arrivals[i].pick_id = \
                evt.picks[i].resource_id
        return evt

    @property
    def catalog(self):
        return Catalog(events=[self.event])

    @property
    def seismic_data_ensemble(self):
        return SeismicDataEnsemble(self.stream, self.catalog, self.inventory)

    @classmethod
    def read(cls, file_path, network, experimental=False):
        if isinstance(file_path, Path):
            file_path = str(file_path)
        with tempfile.NamedTemporaryFile(delete=True) as tmpfile:
            st, head = waveforms.hsf_to_obspy(file_path, print_out=False,
                                              groundmotion=False, return_head=True,
                                              experimental=experimental)

        # convert voltage into 32 bits integer (ADC counts)
        volt_ranges = expand_list(head['volt_range'], head['ch_descr'])
        previous_stations = []
        i = 0
        for tr, volt_range in zip(st, volt_ranges):
            if tr.stats.station not in previous_stations:
                i += 1
                previous_stations.append(tr.stats.station)
            tr.data = (tr.data + volt_range) / 2 * volt_range * 2 ** 32
            tr.data.astype(int)

        return cls(st, head, network)


def expand_list(to_expand, expand_to):
    """
    Expand a list to match the number of elements in another list while preserving
    correspondence.

    :param to_expand: The list to be expanded. It should have the same number of
    elements as the number of unique elements in 'to_expand`.
    :param expand_to: The list containing duplicate items that determine the
                      expansion. It contains duplicates, and the number of
                      unique elements in this list must match the number of elements in
                      `to_expand`.
    :return: The expanded list, where each item in `expand_to` is repeated based on the
             number of occurrences of its corresponding element in `to_expand`.
    """
    expanded_list = []
    count_dict = {}

    # Count the occurrences of each item in `expand_to` and store them in `count_dict`
    for item in expand_to:
        if item not in count_dict:
            count_dict[item] = 0
        count_dict[item] += 1

    # Expand `expand_to` based on the counts stored in `count_dict`
    for item in expand_to:
        expanded_list.append(to_expand[count_dict[item] - 1])
        count_dict[item] -= 1

    return expanded_list


def generate_site_code(station_code, location, channel_code):
    return f'{station_code}.{location:02d}.{channel_code}'


def station_name_converter(station_name):
    hash = hashlib.md5(station_name.encode('ascii')).hexdigest()
    mseed_station_code = hash[:5]
    return mseed_station_code


def patch_using_catalog(data_ensemble, catalogue_line, network):
    event_type = event.uquake_event_from_letter_id(
        catalogue_line['EvtType'], network)
    data_ensemble.catalog[0].event_type = event_type
    if catalogue_line['WF_Modified']:
        evaluation_mode = 'manual'
        if catalogue_line['Rejected']:
            evaluation_status = 'rejected'
        else:
            evaluation_status = 'final'
    else:
        evaluation_mode = 'automatic'
        if catalogue_line['MultiProc']:
            if catalogue_line['Rejected']:
                evaluation_status = 'rejected'
            else:
                evaluation_status = 'confirmed'
        elif catalogue_line['RemoteProc']:
            if catalogue_line['Rejected']:
                evaluation_status = 'rejected'
            else:
                evaluation_status = 'preliminary'

    for pick in data_ensemble.catalog[0].picks:
        pick.evaluation_mode = evaluation_mode
        pick.evaluation_status = evaluation_status

    data_ensemble.catalog[0].preferred_origin().evaluation_mode = evaluation_mode
    data_ensemble.catalog[0].preferred_origin().evaluation_status = evaluation_status

    data_ensemble.catalog[0].preferred_magnitude().evaluation_mode = evaluation_mode
    data_ensemble.catalog[0].preferred_magnitude().evaluation_status = evaluation_status

    trg_id = catalogue_line['TrgID']

    data_ensemble.catalog[0].resource_id.id = f'esg:/{network}/{trg_id}'

    return data_ensemble

