import pytest

from challenges.challenge360_int import Airplane, find_closest_aeroplane, convert_str_coordinates

JFK_AIRPORT = '40.6413 N 73.7781 W'
EIFEL_TOWER = '48.8584 N 2.2945 E'
JFK_AIRPORT_COORD = (40.6413, -73.7781)
EIFEL_TOWER_COORD = (48.8584, 2.2945)

TEST_RESPONSE = [
    ["aaaaaa", "JFK1    ", "United States", 1526074539, 1526074539, -73.7781, 40.6413, 11200.0, False, 230.0, 130.0,
     None, None, 11200.0, "7500", False, 0],
    ["bbbbbb", "EIF1    ", "France", 1526074539, 1526074539, 2.2945, 48.8584, 11200.0, False, 230.0, 130.0,
     None, None, 11200.0, "7600", False, 0]
]


@pytest.mark.parametrize(
    'lat, long, expected', [
        (*JFK_AIRPORT_COORD, 'aaaaaa'),
        (*EIFEL_TOWER_COORD, 'bbbbbb')
    ]
)
def test_find_closest_aeroplane(lat, long, expected):
    test_airplanes = [Airplane.from_opensky(_) for _ in TEST_RESPONSE]

    closest_airplane = find_closest_aeroplane(lat, long, test_airplanes)

    assert expected == closest_airplane.icaoid


def test_return_airplane_from_opensky():
    jfk = Airplane.from_opensky(TEST_RESPONSE[0])

    assert jfk.icaoid == 'aaaaaa'
    assert jfk.altitude == 11200.0


def test_find_distance():
    jfk = Airplane.from_opensky(TEST_RESPONSE[0])
    assert 11200.0 == jfk.find_distance(40.6413, -73.7781)


@pytest.mark.parametrize(
    'str_input, expected', [
        (JFK_AIRPORT, JFK_AIRPORT_COORD),
        (EIFEL_TOWER, EIFEL_TOWER_COORD)
    ]
)
def test_convert_coordinates(str_input, expected):
    assert expected == convert_str_coordinates(str_input)
