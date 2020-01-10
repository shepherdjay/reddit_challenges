from typing import List

#def yahtzee_upper(dice_roll: List):
#  results = []
#  for value in dice_roll:
#    results.append(dice_roll.count(value) * value)
#  return max(results)

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


if __name__ == '__main__':
  assert yahtzee_upper([2, 3, 5, 5, 6])[0] == 10
  assert yahtzee_upper([1, 1, 1, 1, 3])[0] == 4
  assert yahtzee_upper([1, 1, 1, 3, 3])[0] == 6
  assert yahtzee_upper([1, 2, 3, 4, 5])[0] == 5
  assert yahtzee_upper([6, 6, 6, 6, 6])[0] == 30
  print("Tests pass")

  
  assert yahtzee_upper([1654, 1654, 50995, 30864, 1654, 50995, 22747,
    1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654,
    30864, 4868, 30864])[0] == 123456

  print("Optional pass")
