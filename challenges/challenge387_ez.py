import string
import statistics

ALPHABET = list(string.ascii_lowercase)
FREQUENCY_TABLE = [3, -1, 1, 1, 4, 0, 0, 2, 2, -5, -2, 1, 0, 2, 3, 0, -6, 2, 2, 3, 1, -1, 0, -5, 0, -7]


def generate_cypher_dict(rotation: int) -> dict:
    cypher_dict = {}
    for count, letter in enumerate(ALPHABET):
        cypher_dict[letter] = ALPHABET[(count + rotation) % 26]
    return cypher_dict


def warmup(letter: str, rotation: int) -> str:
    cypher = generate_cypher_dict(rotation)
    return cypher[letter]


def caesar(pre_caesar: str, rotation: int) -> str:
    cypher = generate_cypher_dict(rotation)
    result = []
    for character in pre_caesar:
        if character.islower():
            result.append(cypher[character])
        elif character.isupper():
            result.append(cypher[character.lower()].upper())
        else:
            result.append(character)
    return ''.join(result)


def compute_score(string_to_score: str) -> int:
    freq_table = dict(zip(ALPHABET, FREQUENCY_TABLE))
    values = [freq_table[letter.lower()] for letter in string_to_score if letter.isalpha()]
    return statistics.mean(values)


def decrypt(to_decrypt: str) -> str:
    scores = []
    for rotation in range(0, 26):
        canidate_decryption = caesar(to_decrypt, rotation)
        score = compute_score(canidate_decryption)
        scores.append((score, canidate_decryption))
    max_score, probable_decrypted = max(scores)
    return probable_decrypted
