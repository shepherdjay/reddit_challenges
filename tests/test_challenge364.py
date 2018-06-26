from challenges.challenge364_ez import dice_roller, roll
import pytest
from random import Random
import statistics

random = Random()


@pytest.mark.parametrize(
    "input, exp_rolls", [
        ('3d6', 3), ('4d12', 4), ('1d10', 1), ('5d4', 5)
    ])
def test_dice_roller(input, exp_rolls):
    total, rolls = dice_roller(input)
    assert exp_rolls == len(rolls)


def test_roll():
    results = [roll(50) for _ in range(0, 1000)]
    assert pytest.approx(25, abs=2) == statistics.mean(results)
