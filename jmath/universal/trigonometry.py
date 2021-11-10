'''
    Trigonometric Functions
'''

# - Imports

from ..units import Unit, annotate, other, si
from ..uncertainties import Uncertainty
from .tools import generic_function, Supported
import math
from typing import Union, Callable
from functools import wraps

# - Functions

@annotate
def sin(input: other.radian) -> Supported:
    '''
        Computes the sine of the input.

        Parameters
        ----------

        input
            Value to compute sine of
    '''
    return generic_function(math.sin, input)