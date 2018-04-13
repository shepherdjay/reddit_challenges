# /r/dailyprogrammer/comments/8bh8dh/20180411_challenge_356_intermediate_goldbachs/
from typing import List
from sympy import primerange
import random


def find_goldbach(n: int) -> List:
    prime_numbers = list(primerange(0, n))
    odd_primes = [prime for prime in prime_numbers if prime % 2 != 0]

    solution_found = False
    while not solution_found:
        solution = random.choices(odd_primes, k=3)
        if sum(solution) == n:
            solution_found = True

    return solution


if __name__ == '__main__':
    challenge_inputs = [111, 17, 199, 287, 53]
    for number in challenge_inputs:
        solution = sorted(find_goldbach(number))
        print(f'{number} = {solution[0]} + {solution[1]} + {solution[2]}')
