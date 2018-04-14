import pytest

from challenges.challenge356 import find_goldbach


@pytest.mark.parametrize(
    'input', [11, 35]
)
def test_functional(input):
    output = find_goldbach(input)
    assert 3 == len(output)
    assert input == sum(output)


def test_nosolution():
    expected = None
    assert expected == find_goldbach(7)
