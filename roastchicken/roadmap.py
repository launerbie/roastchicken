#!/usr/bin/env python2


def main():
    """ Let's come up with a few things you would like to do with 
    roastchicken. """

    """ Start by creating a new recipe."""
    recipe = Recipe()
    recipe = Recipe(name="Poulet Rôti")

    """ Every recipe has ingredients. """
    recipe.add_ingredients( ingredient )

    """ but it should also be able to take a list of ingredients. """
    recipe.add_ingredients( [ingredient1, ingredient2, ingredient3] )

    """ And you want to print the ingredients nicely, ordered by some 
    sensible ingredient classes. """
    recipe.ingredients 

    """ A recipe should also include instructions on how to use the
    ingredients. """
    recipe.add_instructions(instruction)
    recipe.add_instructions([instruction1, instruction2])

    """ And maybe you want to characterise the recipe with some tags."""
    recipe.add_tags([tag1, tag2])

    """ Or make a price estimate."""
    recipe.cost

    """ Or have it automagically update the ingredient quantities based
    on the number of portions you would like to make."""
    recipe.portions = 4

    """ Maybe you're in a hurry. It would be nice to order recipes by
    an approximate preparation time. """
    recipe.time

    """ Maybe this recipe needs special kitchen equipment."""
    recipe.equipment


if __name__ == "__main__":
    main()
