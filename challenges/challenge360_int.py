import math
import cmath
from collections import OrderedDict
from typing import List, Tuple

import requests

OPENSKY_API_URL = 'https://opensky-network.org/api/states/all'

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
        self.repr_str = [self.callsign, self.lat, self.long, self.altitude, self.country, self.icaoid]

    def __str__(self):
        return '{}\n' \
               'LAT: {} LONG: {}\n' \
               'ALTITUDE: {} Meters\n' \
               'COUNTRY: {}\n' \
               'ICAO ID: {}\n'.format(*self.repr_str)

    def __repr__(self):
        return 'Airplane({},{},{},{},{},{})'.format(*self.repr_str)

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

    def _calculate_a(self, lat: float, long: float) -> float:
        """ a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2) """
        lat_rad = math.radians(lat)
        long_rad = math.radians(long)
        airplane_lat_rad = math.radians(self.lat)
        airplane_long_rad = math.radians(self.long)
        delta_lat = lat_rad - airplane_lat_rad
        delta_long = long_rad - airplane_long_rad

        a = cmath.sin(delta_lat / 2) ** 2 + cmath.cos(lat_rad) * cmath.cos(airplane_lat_rad) * cmath.sin(
            delta_long / 2) ** 2
        return a

    def _calculate_c(self, a: float) -> float:
        """ c = 2 ⋅ atan2( √a, √(1−a) ) """

        sqrt_a = cmath.sqrt(a)
        sqrt_one_minus_a = cmath.sqrt(1 - a)

        return 2 * math.atan2(sqrt_a.real, sqrt_one_minus_a.real)

    def _haversine(self, lat: float, long: float) -> float:
        """
        Units in Kilometers
        Haversine formula - latitudes must be in radians:
        a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
        c = 2 ⋅ atan2( √a, √(1−a) )
        d = R ⋅ c
        """
        earth_radius = 6371.0
        a = self._calculate_a(lat, long)
        c = self._calculate_c(a)
        distance = earth_radius * c
        return abs(distance)

    def distance(self, lat: float, long: float) -> float:
        """ Given a latitude and longitude calculate distance to airplane including altitude, return kilometers """
        # Initial euclidian formula below
        # diff_lat = self.lat - lat
        # diff_long = self.long - long
        # euclidian = math.sqrt((diff_lat ** 2 + diff_long ** 2 + self.altitude ** 2))

        return self._haversine(lat, long) + self.altitude / 1000


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


def main(location: str) -> Airplane:
    print('Finding closest aeroplane to {}'.format(location))
    lat, long = convert_str_coordinates(location)
    aeroplanes = get_list_of_aeroplanes_from_opensky()
    closest_aeroplane, distance = find_closest_aeroplane(lat, long, aeroplanes)

    print('At about {:.2f} km away, the closest airplane is: '.format(distance))
    print(closest_aeroplane)
    return closest_aeroplane


if __name__ == '__main__':
    challenge_inputs = [JFK_AIRPORT, EIFEL_TOWER]
    for challenge in challenge_inputs:
        main(challenge)
