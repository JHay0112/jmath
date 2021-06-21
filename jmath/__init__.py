'''
    jmath/__init__.py

    Author: Jordan Hay
    Date: 2021-06-17

    Initialises jmath
'''

# Define related components
__all__ = [
    "linearalgebra",
    "uncertainties",
    "physics",
    "discrete"
]

# Import core components
from .linearalgebra import *
from .uncertainties import *
from .discrete import *