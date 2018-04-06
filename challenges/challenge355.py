# https://www.reddit.com/r/dailyprogrammer/comments/87rz8c/20180328_challenge_355_intermediate_possible/

# Recipes
PUMPKIN = {
    "pumpkin": 1,
    "apple": 0,
    "eggs": 3,
    "milk": 4,
    "sugar": 3
}

APPLE = {
    "pumpkin": 0,
    "apple": 1,
    "eggs": 4,
    "milk": 3,
    "sugar": 2
}


def map_ingredients(ingredients_as_string: str):
    """ Returns dictionary of ingredients from input string """
    pumpkin, apple, eggs, milk, sugar = [int(x) for x in ingredients_as_string.split(',')]
    return {
        "pumpkin": pumpkin,
        "apple": apple,
        'eggs': eggs,
        'milk': milk,
        'sugar': sugar
    }


def make_pie(ingredients_dict, recipe_dict):
    """
    Bakes a Pie
    :param ingredients_dict: Dictionary of current ingredients on hand
    :param recipe_dict: Dictionary of recipe
    :return: Tuple of (bool, dict) whether the pie was baked, dictionary of remaining ingredients
    """
    remaining_ingredients = {}
    for ingredient, amount in recipe_dict.items():
        try:
            remaining_ingredients[ingredient] = ingredients_dict[ingredient] - amount
            if remaining_ingredients[ingredient] < 0:
                return False, ingredients_dict
        except KeyError:
            return False, ingredients_dict
    return True, remaining_ingredients


def iterate_pies_of_type(ingredients_dict, type, pies_to_bake):
    """
    Takes an ingredient dict, type of pie, and the amount of pies to bake
    Returns amount of pies actually baked and remaining ingredients
    """
    if type == 'pumpkin':
        recipe = PUMPKIN
    elif type == 'apple':
        recipe = APPLE
    else:
        raise ValueError('Pie Type Not Known')

    remaining_ingredients = ingredients_dict

    pies_baked = 0
    while pies_baked != pies_to_bake:
        result, remaining_ingredients = make_pie(remaining_ingredients, recipe)
        if result:
            pies_baked += 1
        else:
            break

    return pies_baked, remaining_ingredients


def make_pies(ingredients_as_string):
    ingredients_dict = map_ingredients(ingredients_as_string)
    # solution_array is tuples of (pumpkin, apple)
    solution_array = []

    for x in range(ingredients_dict['pumpkin']):
        # On each loop try to make that many pumpkin and then make the rest apple
        # Update solution space
        pumpkin_pies_baked, pumpkin_rem_ingredients = iterate_pies_of_type(ingredients_dict, 'pumpkin', x)
        for y in range(pumpkin_rem_ingredients['apple']):
            apple_pies_baked, final_rem_ingredients = iterate_pies_of_type(pumpkin_rem_ingredients, 'apple', y)
            solution_array.append((pumpkin_pies_baked, apple_pies_baked))

    sum_pies = [sol[0] + sol[1] for sol in solution_array]

    solution_index = sum_pies.index(max(sum_pies))

    return solution_array[solution_index]


if __name__ == '__main__':
    string = '{} pumpkin pies and {} apple pies'
    print(string.format(*make_pies('10,14,10,42,24')))
    print(string.format(*make_pies('12,4,40,30,40')))
    print(string.format(*make_pies('12,14,20,42,24')))
