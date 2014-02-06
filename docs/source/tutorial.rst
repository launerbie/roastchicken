
Tutorial
--------

A short tutorial on using roastchicken.

Example code block::

    #main.py 

    from classes import Recipe, Ingredient
    recipe = Recipe(name='Lasagna')
    tomatoes = Ingredient('tomatoes')
    c = Ingredient('grated cheese')
    recipe.add_ingredients([tomatoes,c])
    recipe.ingredients
    [tomatoes, grated cheese]


Testing LateX
"""""""""""""

Example math:

.. math::
    (a + b)^2 = a^2 + 2ab + b^2 

    x - \frac{x^{3}}{6} + \frac{x^{5}}{120} + \mathcal{O}\left(x^{6}\right)

    \int_{0}^{2 \pi}\int_{0}^{\pi}\int_{0}^{R} r^{2} \sin{\left (\theta \right )}\, dr\, d\theta\, d\phi

Testing Warning Block
"""""""""""""""""""""
.. warning::
   some warning
   Warning!

