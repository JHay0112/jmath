'''
    Trigonometric Functions
'''

# - Imports

from ..units import Unit
from ..uncertainties import Uncertainty
from .tools import generic_function, Supported
import math
from typing import Union, Callable
from functools import wraps

# - Functions

@wraps(generic_function)
def sin(input: Supported) -> Supported:
    '''
        Computes the sine of the input.

        Parameters
        ----------

        input
            Value to compute sine of
    '''
    return generic_function(input, math.sin)