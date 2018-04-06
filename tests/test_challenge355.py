from challenges.challenge355 import make_pies, map_ingredients, make_pie, PUMPKIN, APPLE, iterate_pies_of_type
import pytest

INPUT1 = '10,14,10,42,24'
INPUT2 = '12,4,40,30,40'
INPUT3 = '12,14,20,42,24'

INGREDIENTS_DICT_1 = {'pumpkin': 10, 'apple': 14, 'eggs': 10, 'milk': 42, 'sugar': 24}
INGREDIENTS_DICT_2 = {'pumpkin': 12, 'apple': 4, 'eggs': 40, 'milk': 30, 'sugar': 40}
INGREDIENTS_DICT_3 = {'pumpkin': 12, 'apple': 14, 'eggs': 20, 'milk': 42, 'sugar': 24}


@pytest.mark.parametrize(
    'ingredients,exp_pumpkin,exp_apple', [
        (INPUT1, 3, 0),
        (INPUT2, 5, 3),
        (INPUT3, 5, 1)
    ])
def test_make_pies(ingredients, exp_pumpkin, exp_apple):
    act_pumpkin, act_apple = make_pies(ingredients)

    assert exp_pumpkin + exp_apple == act_pumpkin + act_apple


@pytest.mark.parametrize(
    'ingredients_string,exp_dictionary', [
        (INPUT1, INGREDIENTS_DICT_1),
        (INPUT2, INGREDIENTS_DICT_2),
        (INPUT3, INGREDIENTS_DICT_3)
    ])
def test_map_ingredients(ingredients_string, exp_dictionary):
    assert exp_dictionary == map_ingredients(ingredients_string)


@pytest.mark.parametrize(
    'ingredients_dict,recipe,exp_result,exp_remaining', [
        (INGREDIENTS_DICT_1, PUMPKIN, True, {'pumpkin': 9, 'apple': 14, 'eggs': 7, 'milk': 38, 'sugar': 21}),
        (INGREDIENTS_DICT_3, APPLE, True, {'pumpkin': 12, 'apple': 13, 'eggs': 16, 'milk': 39, 'sugar': 22}),
        ({'pumpkin': 1}, APPLE, False, {'pumpkin': 1})
    ]
)
def test_make_pie(ingredients_dict, recipe, exp_result, exp_remaining):
    act_result, act_remaining_ingredients = make_pie(ingredients_dict, recipe)

    assert exp_result == act_result
    assert exp_remaining == act_remaining_ingredients


def test_iterate_pies_of_type():
    exp_pies_baked, exp_remaining_ingredients = 3, {'pumpkin': 7, 'apple': 14, 'eggs': 1, 'milk': 30, 'sugar': 15}
    act_pies_baked, act_remaining_ingredients = iterate_pies_of_type(INGREDIENTS_DICT_1, 'pumpkin', 4)

    assert exp_remaining_ingredients == act_remaining_ingredients
