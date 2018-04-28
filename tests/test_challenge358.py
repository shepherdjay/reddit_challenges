import pytest

from challenges.challenge358_ez import INPUT1, INPUT2, INPUT3, INPUT4
from challenges.challenge358_ez import whats_on_my_display, split_to_individual, interpret_number


@pytest.mark.parametrize(
    'lines_input, expected_output', [
        (INPUT1, '123456789'),
        (INPUT2, '433805825'),
        (INPUT3, '526837608'),
        (INPUT4, '954105592'),
    ], ids=['123456789', '433805825', '526837608', '954105592']
)
def test_whats_on_my_display(lines_input, expected_output):
    assert expected_output == whats_on_my_display(lines_input)


def test_split_to_individual():
    string_input = "" \
                   "    _ \n" \
                   "  | _|\n" \
                   "  | _|\n"
    expected_output = [
        "   "
        "  |"
        "  |",
        " _ "
        " _|"
        " _|"
    ]

    assert expected_output == split_to_individual(string_input)


def test_interpret_number():
    string_input = "" \
                   "   " \
                   "  |" \
                   "  |"
    expected_output = 1

    assert expected_output == interpret_number(string_input)


if __name__ == '__main__':
    pytest.main()
