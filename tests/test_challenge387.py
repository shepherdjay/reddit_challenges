from challenges.challenge387_ez import warmup, caesar, decrypt, generate_cypher_dict
import pytest


@pytest.mark.parametrize('letter,rotation,expected', [
    ('a', 0, 'a'),
    ('a', 1, 'b'),
    ('a', 5, 'f'),
    ('a', 26, 'a'),
    ('d', 15, 's'),
    ('z', 1, 'a'),
    ('q', 22, 'm')
])
def test_warmup_set(letter, rotation, expected):
    assert warmup(letter, rotation) == expected


def test_cypher_generation_no_rotation():
    result = generate_cypher_dict(0)
    assert result['a'] == 'a'


def test_cypher_generation_rot_13():
    result = generate_cypher_dict(13)
    assert result['a'] == 'n'


@pytest.mark.parametrize('pre_caesar,rotation,expected', [
    ("a", 1, "b"),
    ("abcz", 1, "bcda"),
    ("irk", 13, "vex"),
    ("fusion", 6, "layout"),
    ("dailyprogrammer", 6, "jgorevxumxgsskx"),
    ("jgorevxumxgsskx", 20, "dailyprogrammer"),
])
def test_caesar_challenge(pre_caesar, rotation, expected):
    assert caesar(pre_caesar, rotation) == expected


def test_caesar_bonus_1():
    assert caesar("Daily Programmer!", 6) == "Jgore Vxumxgsskx!"


@pytest.mark.parametrize('to_decrypt,expected', [
    ("Zol abyulk tl puav h ulda.", "She turned me into a newt."),
    (
            "Qv wzlmz bw uiqvbiqv iqz-axmml dmtwkqbg, i aeittwe vmmla bw jmib qba eqvoa nwzbg-bpzmm bquma mdmzg amkwvl, zqopb?",
            "In order to maintain air-speed velocity, a swallow needs to beat its wings forty-three times every second, right?"),
    ("Tfdv ef wlikyvi, wfi uvrky rnrzkj pfl rcc nzky erjkp, szx, gfzekp kvvky.",
     "Come no further, for death awaits you all with nasty, big, pointy teeth.")
])
def test_decrypt_bonus_2(to_decrypt, expected):
    assert decrypt(to_decrypt) == expected
