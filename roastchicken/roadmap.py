#!/usr/bin/env python2

import argparse

def main():
    """ Let's come up with a few things you would like to do with 
    roastchicken. """

    recipe = Recipe()

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


def get_options():
    parser = argparse.ArgumentParser()
    #parser.add_argument('filenames', type=str, nargs='+',
    #               help='photometric data to load.')
    #parser.add_argument('-v','--verbose',\
    #               action='store_true',\
    #               help='Increases verbosity.')
    #parser.add_argument('-o','--outputdir', type=str, default='images',\
    #               help='output directory for images.')

    #parser.add_argument('-t','--test',\
    #               action='store_true',\
    #               help='Use test sequence [2,2,2,1,2].')
    #parser.add_argument('-f','--full',\
    #               action='store_true',\
    #               help='print full arrays.')
    #parser.add_argument('-o','--initial', type=int, default=10,\
    #               help='length of initial set')
    #parser.add_argument('-m','--max_turns', type=int, default=100000,\
    #               help='maximum number of turns')
    #parser.add_argument('t_init', type=str, nargs='+',
    #               help='length of initial set')
    #parser.add_argument('-o','--outputdir', type=str, default='images',\
    #               help='output directory for images.')

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_options()
    main()
