
Tutorial
--------

A short tutorial on using roastchicken.

Example code block::

    #main.py 
    import roastchicken as rs

    recipes = rs.get_recipes_all()
    print(recipes)

    li = range(10)
    for i in li:
        print i

Testing LateX
"""""""""""""

Example math:

.. math::
    (a + b)^2 = a^2 + 2ab + b^2 

    x - \frac{x^{3}}{6} + \frac{x^{5}}{120} + \mathcal{O}\left(x^{6}\right)

    \int_{0}^{2 \pi}\int_{0}^{\pi}\int_{0}^{R} r^{2} \sin{\left (\theta \right )}\, dr\, d\theta\, d\phi

