# https://www.reddit.com/r/dailyprogrammer/comments/8df7sm/20180419_challenge_357_intermediate_kolakoski/
from typing import Tuple


def nillson_recurse():
    yield 2
    output = 1
    for x in nillson_recurse():
        for _ in range(x):
            yield output
        output = 3 - output


def nillson_generator():
    yield 1
    yield 2
    for x in nillson_recurse():
        yield x


def kolokaski_ratio(n: int) -> Tuple:
    ones = 0
    twos = 0
    gen = nillson_generator()
    for _ in range(n):
        result = next(gen)
        if result == 1:
            ones += 1
        elif result == 2:
            twos += 1
    return ones, twos


if __name__ == '__main__':
    print('CHALLENGE MODE')
    print(kolokaski_ratio(1000000))
    print(kolokaski_ratio(100000000))

    print('BONUS MODE - GET A CUP OF COFFEE')
    print(kolokaski_ratio(1000000000000))
    print(kolokaski_ratio(100000000000000))
