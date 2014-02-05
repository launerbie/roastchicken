#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Some roastchicken containers.
"""

class Recipe(object):
    def __init__(self, name=None, ingredients=None):
        self.name = name 

        if ingredients is None:
            self._ingredients = list() 
        else:
            self._ingredients = ingredients 
        #todo: allow only lists consisting of Ingredients

    def add_ingredients(self, ingredients):
        self._ingredients.extend(ingredients)
        #this will allow duplicates. Fix later

    @property
    def ingredients(self):
        return self._ingredients

    def add_instructions(self):
        pass

    def add_tags(self):
        pass

    @property
    def cost(self):
        pass

    def portions(self):
        pass
 
    @property
    def time(self):
        pass

class Ingredient(object):
    def __init__(self, name):
        self.name = name #todo: only strings allowed

    def quantity(self):
        pass

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

