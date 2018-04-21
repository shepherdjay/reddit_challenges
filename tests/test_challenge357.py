import pytest

from challenges.challenge357_int import kolokaski_ratio, nillson_generator

KOLOKASKI = '12211212212211211221211212211'


@pytest.mark.known
@pytest.mark.parametrize(
    'input, exp_output', [
        (10, (5, 5)),
        (100, (49, 51)),
        (1000, (502, 498)),
    ]
)
def test_kolokaski_expected(input, exp_output):
    assert exp_output == kolokaski_ratio(input)


@pytest.mark.parametrize(
    'input', [
        pytest.param(1000000, marks=pytest.mark.challenge),
        pytest.param(100000000, marks=pytest.mark.challenge),
        pytest.param(1000000000000, marks=pytest.mark.bonus),
        pytest.param(100000000000000, marks=pytest.mark.bonus)
    ]
)
def test_kolokaski_unknown(input):
    output = kolokaski_ratio(input)
    assert pytest.approx(1, rel=1.0e-04) == (output[0] / output[1])


@pytest.mark.parametrize(
    'k, expected', [
        (5, KOLOKASKI[5]),
        (4, KOLOKASKI[4]),
        (2, KOLOKASKI[2]),
        (7, KOLOKASKI[7]),
    ]
)
def test_nillson(k, expected):
    gen = nillson_generator()
    output = 0
    for _ in range(k + 1):
        output = next(gen)

    assert expected == str(output)
