from typing import Tuple
import random


def roll(number: int) -> int:
    return random.randint(1, number)


def dice_roller(input_string: str) -> Tuple:
    rolls, sides = input_string.split('d')
    results = [roll(int(sides)) for _ in range(0, int(rolls))]
    return sum(results), results


if __name__ == '__main__':
    try:
        print("Welcome to dice roller, type ctrl+c to quit")
        while True:
            ndm = input("Please input dice roll in format NdM: ")
            total, rolls = dice_roller(ndm)
            print(f"{total}: {rolls}")
    except KeyboardInterrupt:
        exit()
