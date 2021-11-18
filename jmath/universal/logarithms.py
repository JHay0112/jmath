'''
    Logarithmic Functions
'''

# - Imports

from .tools import generic_function, Supported
import math

# - Functions

def log(value: Supported, base: float = math.e) -> Supported:
    """
        Calculates logarithm of a number.

        Parameters
        ----------

        value
            The value to compute the logarithm of.
    """
    return generic_function(math.log, value)

def log10(value: Supported) -> Supported:
    """
        Calculates the log base 10 of a number.

        Parameters
        ----------

        value
            The number to calculate the log base 10 of.
    """
    return log(value, base = 10)

def log2(value: Supported) -> Supported:
    """
        Calculates the log base 2 of a number.

        Parameters
        ----------

        value
            The number to calculate the log base 2 of.
    """
    return log(value, base = 2)