from collections import OrderedDict
from typing import List
import math
import requests

OPENSKY_API_URL = 'https://opensky-network.org/api/states/all'


class Airplane:
    def __init__(self, callsign: str, lat: float, long: float, altitude: float, country: str, icaoid: str):
        self.callsign = callsign
        self.lat = lat
        self.long = long
        self.altitude = altitude
        self.country = country
        self.icaoid = icaoid

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

    def find_distance(self, lat: float, long: float) -> float:
        """ Given a latitude and longitude calculate how far away the plane is """
        diff_lat = self.lat - lat
        diff_long = self.long - long
        distance_over_ground = math.hypot(diff_lat, diff_long)
        return math.hypot(distance_over_ground, self.altitude)


def find_closest_aeroplane(lat: float, long: float, airplanes: List[Airplane]) -> Airplane:
    results = []
    for airplane in airplanes:
        results.append((airplane, airplane.find_distance(lat=lat, long=long)))
    results.sort(key=lambda x: x[1])
    return results[0][0]
