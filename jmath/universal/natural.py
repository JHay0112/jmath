'''
    Natural functions associated with Euler's constant e.

    Notes
    -----

    log is from logarithms.py
'''

# - Imports

from .tools import generic_function, Supported
from .logarithms import log
import math

# - Functions

def exp(value: Supported) -> Supported:
    """
        Calculates the exponential (e^x) of a number.

        Parameters
        ----------

        value
            The value to calculate the exponential of.
    """
    return generic_function(math.exp, value, derivative = exp)