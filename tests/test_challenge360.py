from unittest.mock import patch

import pytest

import challenges.challenge360_int as ch360
from challenges.challenge360_int import Airplane, find_closest_aeroplane, convert_str_coordinates, JFK_AIRPORT, \
    EIFEL_TOWER

JFK_AIRPLANE = ["aaaaaa", "JFK1    ", "United States", 1526074539, 1526074539, -73.7781, 40.6413, 11200.0, False,
                230.0, 130.0, None, None, 11200.0, "7500", False, 0]
EIFEL_TOWER_AIRPLANE = ["bbbbbb", "EIF1    ", "France", 1526074539, 1526074539, 2.2945, 48.8584, 11200.0, False, 230.0,
                        130.0,
                        None, None, 11200.0, "7600", False, 0]

JFK_AIRPORT_COORD = (40.6413, -73.7781)
EIFEL_TOWER_COORD = (48.8584, 2.2945)

TEST_RESPONSE = {'states': [JFK_AIRPLANE, EIFEL_TOWER_AIRPLANE]}


@pytest.mark.parametrize(
    'lat, long, expected', [
        (*JFK_AIRPORT_COORD, 'aaaaaa'),
        (*EIFEL_TOWER_COORD, 'bbbbbb')
    ]
)
def test_find_closest_aeroplane(lat, long, expected):
    test_airplanes = [Airplane.from_opensky(_) for _ in TEST_RESPONSE['states']]

    closest_airplane, distance = find_closest_aeroplane(lat, long, test_airplanes)

    assert expected == closest_airplane.icaoid
    assert 11.2 == distance


def test_return_airplane_from_opensky():
    jfk = Airplane.from_opensky(JFK_AIRPLANE)

    assert 'aaaaaa' == jfk.icaoid
    assert 11200 == jfk.altitude


@pytest.mark.parametrize(
    'test_plane, exp_distance, resolution', [
        (JFK_AIRPLANE, 11.2, None),
        (EIFEL_TOWER_AIRPLANE, 5822, 100),
        pytest.param(EIFEL_TOWER_AIRPLANE, 5822, None, marks=pytest.mark.xfail)
    ]
)
def test_find_distance(test_plane, exp_distance, resolution):
    airplane = Airplane.from_opensky(test_plane)
    assert exp_distance == pytest.approx(airplane.distance(40.6413, -73.7781), abs=resolution)


@pytest.mark.parametrize(
    'str_input, expected', [
        (JFK_AIRPORT, JFK_AIRPORT_COORD),
        (EIFEL_TOWER, EIFEL_TOWER_COORD)
    ]
)
def test_convert_coordinates(str_input, expected):
    assert expected == convert_str_coordinates(str_input)


@patch('challenges.challenge360_int.requests.get')
def test_functional_mock_requests(mocked_get):
    mocked_get.return_value.json.return_value = TEST_RESPONSE
    result = ch360.main(JFK_AIRPORT)

    assert 'JFK1    ' == result.callsign
