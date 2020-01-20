import hypothesis.strategies as st
import pytest
from hypothesis import given, settings

from challenges.challenge381_ez import yahtzee_upper


@pytest.mark.parametrize('roll_input,exp_score', [
    ([2, 3, 5, 5, 6], 10),
    ([1, 1, 1, 1, 3], 4),
    ([1, 1, 1, 3, 3], 6),
    ([1, 2, 3, 4, 5], 5),
    ([6, 6, 6, 6, 6], 30),
    pytest.param(
        [1654, 1654, 50995, 30864, 1654, 50995, 22747, 1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654,
         30864,
         4868, 30864], 123456, id='Optional')
])
def test_challenge381(roll_input, exp_score):
    assert exp_score == yahtzee_upper(roll_input)[0]


@given(roll_input=st.lists(st.integers(min_value=1), min_size=1))
@settings(max_examples=1_000)
def test_challenge381_hypothesis(roll_input):
    assert sum(roll_input) >= yahtzee_upper(roll_input)[0]
