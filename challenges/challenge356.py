# /r/dailyprogrammer/comments/8bh8dh/20180411_challenge_356_intermediate_goldbachs/
from itertools import product
from typing import List

from sympy import primerange


def find_goldbach(n: int) -> List:
    odd_primes = [prime for prime in primerange(0, n) if prime % 2 != 0]

    solution_space = product(odd_primes[:], odd_primes[:], odd_primes[:])

    for possible_solution in solution_space:
        if sum(possible_solution) == n:
            return possible_solution


if __name__ == '__main__':
    challenge_inputs = [111, 17, 199, 287, 53]
    for number in challenge_inputs:
        solution = find_goldbach(number)
        print(f'{number} = {solution[0]} + {solution[1]} + {solution[2]}')
