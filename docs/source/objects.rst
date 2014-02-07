
object
------

code::

    >>> help(object)

    Help on class object in module builtins:
    
    class object
     |  The most base type
    (END)



code::

    >>> help(type)

    Help on class type in module builtins:
    
    class type(object)
     |  type(object) -> the object's type
     |  type(name, bases, dict) -> a new type
     |  
     |  Methods defined here:

    [...]

     |  Data descriptors defined here:

    [...]

     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    (END)


Let's try creating a class just like type, but call it ttype.

    >>> class ttype(object): pass
    >>> t = ttype()


code::

    >>> help(ttype)

    Help on class ttype in module __main__:
    
    class ttype(builtins.object)
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    (END)


So this is not exactly this same as type, apparently ttype inherits from
builtins.object.

What else is there... let me try int: ::

    >>> help(int)
    
    Help on class int in module builtins:
    
    class int(object)
     |  int(x=0) -> integer
     |  int(x, base=10) -> integer
     |  
     |  Convert a number or string to an integer, or return 0 if no arguments
     |  are given.  If x is a number, return x.__int__().  For floating point
     |  numbers, this truncates towards zero.
     |  
     |  If x is not a number or if base is given, then x must be a string,
     |  bytes, or bytearray instance representing an integer literal in the
     |  given base.  The literal can be preceded by '+' or '-' and be surrounded
     |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
     |  Base 0 means to interpret the base from the string as an integer literal.
     |  >>> int('0b100', base=0)
     |  4
     |  
     |  Methods defined here:
    
    [...]
    
     |  Data descriptors defined here:
     |  
     |  denominator
     |      the denominator of a rational number in lowest terms
     |  
     |  imag
     |      the imaginary part of a complex number
     |  
     |  numerator
     |      the numerator of a rational number in lowest terms
     |  
     |  real
     |      the real part of a complex number
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    (END)

So int and type both inherit from object, it seems.

code::

    >>> int.__class__
    <class 'type'>
    >>> type.__class__
    <class 'type'>
    >>> object.__class__
    <class 'type'>
    >>> ttype.__class__
    <class 'type'>

    >>> type(ttype)
    <class 'type'>
    >>> type(type)
    <class 'type'>
    >>> type(int)
    <class 'type'>
    >>> type(object)
    <class 'type'>

Explain this: ::
    >>> type(object)
    <class 'type'>
    >>> type(object())
    <class 'object'>









