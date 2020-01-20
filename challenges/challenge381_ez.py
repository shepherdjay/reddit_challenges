from typing import List


def yahtzee_upper(dice_roll: List):
    results_dict = {}
    for value in dice_roll:
        current_value = results_dict.get(value, 0)
        results_dict[value] = current_value + value

    cur_max = 0
    for k, v in results_dict.items():
        if v > cur_max:
            cur_max = v

    return cur_max, len(results_dict)
