.. highlight:: python

Tutorial
--------

Trying out some Sphinx directives:

Inline markup
"""""""""""""
text
*text*
**text**
``text``

:emphasis:`text`
:strong:`text`
:literal:`text`
:subscript:`text`
:superscript:`text`
:title-reference:`text`


Lists and Quote-like block
""""""""""""""""""""""""""
* This is a bulleted list.
* It has two items, the second
  item uses two lines.

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.

* this is
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues

#################
This is a heading
#################

*****************
Chapters
*****************

=================
Sections
=================

-----------------
Subsections
-----------------

^^^^^^^^^^^^^^^^^
subsubsections
^^^^^^^^^^^^^^^^^

"""""""""""""""""
paragraphs
"""""""""""""""""

Hyperlinks
""""""""""
This is a paragraph that contains `a link`_.

.. _a link: http://example.com/


Footnotes
"""""""""
Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

.. rubric:: Footnotes

.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.


Citations
"""""""""
Lorem ipsum [Ref]_ dolor sit amet.

.. [Ref] Book or article reference, URL or whatever.

Comments
""""""""
..
   This whole indented block
   is a comment.

   Still in the comment.

Testing Code blocks
"""""""""""""""""""

.. code-block:: python
   :emphasize-lines: 3,5

   def some_function():
       interesting = False
       print('This line is highlighted.')
       print('This one is not...')
       print('...but this one is.')

Example code block::

    #main.py 
    from classes import Recipe, Ingredient
    recipe = Recipe(name='Lasagna')
    tomatoes = Ingredient('tomatoes')
    c = Ingredient('grated cheese')
    recipe.add_ingredients([tomatoes,c])
    recipe.ingredients
    [tomatoes, grated cheese]

.. literalinclude:: example.py



Testing LateX
"""""""""""""

Example math:

.. math::
    (a + b)^2 = a^2 + 2ab + b^2 

    x - \frac{x^{3}}{6} + \frac{x^{5}}{120} + \mathcal{O}\left(x^{6}\right)

    \int_{0}^{2 \pi}\int_{0}^{\pi}\int_{0}^{R} r^{2} \sin{\left (\theta \right )}\, dr\, d\theta\, d\phi


Testing sphinx directives 
"""""""""""""""""""""""""
.. warning::
   some warning
   Warning!

.. note::
   This function is not suitable for sending spam e-mails.

.. seealso::

   Module :py:mod:`zipfile`
      Documentation of the :py:mod:`zipfile` standard module.

   `GNU tar manual, Basic Tar Format <http://link>`_
      Documentation for tar archive files, including GNU tar extensions.

.. rubric:: title

.. centered:: LICENSE AGREEMENT

.. hlist::
   :columns: 3

   * A list of
   * short items
   * that should be
   * displayed
   * horizontally

.. glossary::

   environment
      A structure where information about all documents under the root is
      saved, and used for cross-referencing.  The environment is pickled
      after the parsing stage, so that successive runs only need to read
      and parse new and changed documents.

   source directory
      The directory which, including its subdirectories, contains all
      source files for one Sphinx project.

.. productionlist::
      try_stmt: try1_stmt | try2_stmt
   try1_stmt: "try" ":" `suite`
            : ("except" [`expression` ["," `target`]] ":" `suite`)+
            : ["else" ":" `suite`]
            : ["finally" ":" `suite`]
   try2_stmt: "try" ":" `suite`
            : "finally" ":" `suite`
