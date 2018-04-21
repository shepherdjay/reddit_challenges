# https://www.reddit.com/r/dailyprogrammer/comments/8df7sm/20180419_challenge_357_intermediate_kolakoski/
from typing import Tuple

NILLSON_P = {}


def counter(input_string: str) -> Tuple:
    ones = 0
    twos = 0
    for character in input_string:
        if int(character) == 1:
            ones += 1
        elif int(character) == 2:
            twos += 1
    return ones, twos


def nillson_recurse():
    yield 2
    output = 1
    for x in nillson_recurse():
        for i in range(x):
            yield output
        output = 3 - output


def nillson_generator():
    yield 1
    yield 2
    for x in nillson_recurse():
        yield x


def nillson(n: int):
    gen = nillson_generator()
    for _ in range(n+1):
        value = next(gen)
    return str(value)


def kolokaski_ratio(n: int) -> Tuple:
    seq = '0122'
    iter_n = 2
    while len(seq) <= n:
        iter_n += 1
        if iter_n % 2 != 0:
            seq += ('1' * int(seq[iter_n]))
        else:
            seq += ('2' * int(seq[iter_n]))
    return counter(seq[1:n + 1])


if __name__ == '__main__':
    print('CHALLENGE MODE')
    print(kolokaski_ratio(1000000))
    print(kolokaski_ratio(100000000))

    print('BONUS MODE - GET A CUP OF COFFEE')
    print(kolokaski_ratio(1000000000000))
    print(kolokaski_ratio(100000000000000))
