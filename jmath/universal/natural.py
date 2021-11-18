'''
    Functions related to Euler's Constant, ln/log, exp.
'''

# - Imports

from .tools import generic_function, Supported
import math

# - Functions

def log(value: Supported) -> Supported:
    """
        Calculates the natural log of a number.

        Parameters
        ----------

        value
            The value to compute the natural log of.
    """
    return generic_function(math.log, value)

def exp(value: Supported) -> Supported:
    """
        Calculates the exponential (e^x) of a number.

        Parameters
        ----------

        value
            The value to calculate the exponential of.
    """
    return generic_function(math.exp, value)