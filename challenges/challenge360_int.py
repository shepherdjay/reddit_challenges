import math
from collections import OrderedDict
from typing import List, Tuple

import requests

OPENSKY_API_URL = 'https://opensky-network.org/api/states/all'
EARTH_RADIUS = 6373.0
JFK_AIRPORT = '40.6413 N 73.7781 W'
EIFEL_TOWER = '48.8584 N 2.2945 E'


class Airplane:
    def __init__(self, callsign: str, lat: float, long: float, altitude: float, country: str, icaoid: str):
        self.callsign = callsign
        self.lat = lat
        self.long = long
        self.altitude = altitude
        self.country = country
        self.icaoid = icaoid

    def __str__(self):
        return '{}\n' \
               'LAT: {} LONG: {}\n' \
               'ALTITUDE: {}\n' \
               'COUNTRY: {}\n' \
               'ICAO ID: {}\n'.format(
            self.callsign, self.lat, self.long, self.altitude, self.country, self.icaoid
        )

    def __repr__(self):
        return 'Airplane({},{},{},{},{},{})'.format(self.callsign, self.lat, self.long, self.altitude, self.country,
                                                    self.icaoid)

    @classmethod
    def from_opensky(cls, openskydata: list) -> 'Airplane':
        """ Returns Airplane object """
        openskydata_map = OrderedDict({
            'callsign': 1,
            'lat': 6,
            'long': 5,
            'altitude': 7,
            'country': 2,
            'icaoid': 0,
        })
        mapped_data = [openskydata[x] for x in openskydata_map.values()]
        return cls(*mapped_data)

    def distance(self, lat: float, long: float) -> float:
        """ Given a latitude and longitude calculate distance to airplane including altitude """
        diff_lat = math.radians(self.lat) - math.radians(lat)
        diff_long = math.radians(self.long) - math.radians(long)
        ground_distance = math.hypot(diff_lat, diff_long)
        total_distance = math.hypot(ground_distance, self.altitude)
        return total_distance


def find_closest_aeroplane(lat: float, long: float, airplanes: List[Airplane]) -> Tuple[Airplane, float]:
    results = []
    for airplane in airplanes:
        if airplane.lat and airplane.long and airplane.altitude:
            results.append((airplane, airplane.distance(lat=lat, long=long)))
    results.sort(key=lambda x: x[1])
    return results[0]


def get_list_of_aeroplanes_from_opensky() -> List[Airplane]:
    raw_data = requests.get(OPENSKY_API_URL)
    json_data = raw_data.json()
    airplanes = []
    for data in json_data['states']:
        airplanes.append(Airplane.from_opensky(data))
    return airplanes


def convert_str_coordinates(str_input: str) -> Tuple[float, float]:
    split_string = str_input.split(sep=' ')
    if split_string[1] == 'N':
        lat = float(split_string[0])
    else:
        lat = float('-' + split_string[0])

    if split_string[3] == 'E':
        long = float(split_string[2])
    else:
        long = float('-' + split_string[2])

    return lat, long


def main(location: str):
    print('Finding closest aeroplane to {}'.format(location))
    lat, long = convert_str_coordinates(location)
    aeroplanes = get_list_of_aeroplanes_from_opensky()
    closest_aeroplane, distance = find_closest_aeroplane(lat, long, aeroplanes)

    print('At {} away, the closest airplane is: '.format(distance))
    print(closest_aeroplane)
    return closest_aeroplane


if __name__ == '__main__':
    challenge_inputs = [JFK_AIRPORT, EIFEL_TOWER]
    for challenge in challenge_inputs:
        main(challenge)
