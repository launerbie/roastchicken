#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .classes import Recipe
from .classes import Ingredient

def test_recipe_noname():
    recipe = Recipe()
    assert Recipe().name == None
    assert Recipe().name is None

def test_recipe_name():
    recipe = Recipe(name='Coq au vin')
    assert recipe.name == 'Coq au vin'

def test_recipe_name_unicode():
    recipe = Recipe(name='Crême brûlée')
    assert recipe.name == 'Crême brûlée'

def test_recipe_add_ingredients_list():
    recipe = Recipe()
    tomatoes = Ingredient('tomatoes')
    onions = Ingredient('onions')
    recipe.add_ingredients([tomatoes,onions])


def test_ingredient_name():
    i = Ingredient(name='salt')
    assert i.name == 'salt'

def test_recipe_name_unicode():
    i = Ingredient(name='Crême fraîche')
    assert i.name == 'Crême fraîche'


