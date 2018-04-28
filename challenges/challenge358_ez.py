# Challenge Inputs
INPUT1 = "" \
         "    _  _     _  _  _  _  _ \n" \
         "  | _| _||_||_ |_   ||_||_|\n" \
         "  ||_  _|  | _||_|  ||_| _|\n"

INPUT2 = "" \
         "    _  _  _  _  _  _  _  _ \n" \
         "|_| _| _||_|| ||_ |_| _||_ \n" \
         "  | _| _||_||_| _||_||_  _|\n"

INPUT3 = "" \
         " _  _  _  _  _  _  _  _  _ \n" \
         "|_  _||_ |_| _|  ||_ | ||_|\n" \
         " _||_ |_||_| _|  ||_||_||_|\n"

INPUT4 = "" \
         " _  _        _  _  _  _  _ \n" \
         "|_||_ |_|  || ||_ |_ |_| _|\n" \
         " _| _|  |  ||_| _| _| _||_ \n"

NUMBER_MAP = {
    '000001001': 1,
    '010011110': 2,
    '010011011': 3,
    '000111001': 4,
    '010110011': 5,
    '010110111': 6,
    '010001001': 7,
    '010111111': 8,
    '010111011': 9,
}


def interpret_number(string: str) -> int:
    converted_1_0 = []
    for char in string:
        if char == ' ':
            converted_1_0.append('0')
        else:
            converted_1_0.append('1')
    try:
        result = NUMBER_MAP[''.join(converted_1_0)]
    except KeyError:
        result = 0
    return result


def split_to_individual(string: str) -> list:
    split_list = []
    length_of_row = len(string) // 3
    numbers = length_of_row // 3

    for number in range(numbers):
        start_index = number * 3
        end_index = start_index + 3
        split_list.append(
            string[start_index:end_index] +
            string[start_index + length_of_row:end_index + length_of_row] +
            string[start_index + length_of_row * 2: end_index + length_of_row * 2]
        )
    return split_list


def whats_on_my_display(string: str) -> str:
    answer = []
    to_interpret = split_to_individual(string)
    for number_string in to_interpret:
        answer.append(str(interpret_number(number_string)))

    return ''.join(answer)


if __name__ == '__main__':
    challenge_list = [INPUT1, INPUT2, INPUT3, INPUT4]
    for challenge in challenge_list:
        print(whats_on_my_display(challenge))
