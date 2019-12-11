#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    cont = {}

    batches = 0

    for key_r in recipe:
        if key_r in ingredients:
            batches = 1
        else:
            batches = 0
            return batches

    for key_i in ingredients:
        cont.update({key_i: 0})
        cont[key_i] = ingredients[key_i] // recipe[key_i]

    batches = min(cont.values())

    print(cont)
    return batches


print(recipe_batches({"milk": 5, "honey": 5}, {"milk": 15, "honey": 14}))

if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
