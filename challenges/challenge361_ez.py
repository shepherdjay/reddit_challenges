from collections import Counter


def main(score_str):
    wins = Counter([win for win in score_str if win.islower()])
    wins.subtract(Counter([loss.lower() for loss in score_str if loss.isupper()]))
    return wins


if __name__ == '__main__':
    score_str = 'dbbaCEDbdAacCEAadcB'
    [print(f'{player}: {wins}') for player, wins in main(score_str).items()]
