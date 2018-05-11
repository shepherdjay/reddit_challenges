import pytest
from challenges.challenge360_int import Airplane

JFK_AIRPORT = ('40.6413 N', '73.7781 W')
EIFEL_TOWER = ('48.8584 N', '2.2945 E')

TEST_RESPONSE = [
    ["aaaaaa", "JFK1    ", "United States", 1526074539, 1526074539, -73.7781, 40.6413, 11200.0, False, 230.0, 130.0,
     None, None, 11200.0, "7500", False, 0],
    ["bbbbbb", "EIF1    ", "France", 1526074539, 1526074539, 2.2945, 48.8584, 11200.0, False, 230.0, 130.0,
     None, None, 11200.0, "7600", False, 0]
]


@pytest.mark.parametrize(
    'lat, long', [
        EIFEL_TOWER,
        JFK_AIRPORT
    ]
)
def test_find_closest_aeroplane(lat, long):
    pytest.fail('Write Test')


def test_return_airplane_from_opensky():
    jfk = Airplane.from_opensky(TEST_RESPONSE[0])

    assert jfk.icaoid == 'aaaaaa'
    assert jfk.altitude == 11200.0


def test_find_distance():
    jfk = Airplane.from_opensky(TEST_RESPONSE[0])
    assert 11200.0 == jfk.find_distance(40.6413, -73.7781)
