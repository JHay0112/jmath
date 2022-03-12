'''
    Hyperbolic functions.
'''

# - Imports

from .tools import generic_function, Supported
import math

# - Functions

def cosh(value: Supported) -> Supported:
    """
        Computes the hyberbolic cosine of a value.

        Parameters
        ----------

        value   
            The number to compute the hyberbolic cosine of.
    """
    return generic_function(math.cosh, value, derivative = sinh)

def acosh(value: Supported) -> Supported:
    """
        Computes the inverse hyberbolic cosine of a value.

        Parameters
        ----------

        value   
            The number to compute the inverse hyberbolic cosine of.
    """
    return generic_function(math.acosh, value)

def sinh(value: Supported) -> Supported:
    """
        Computes the hyberbolic sine of a value.

        Parameters
        ----------

        value   
            The number to compute the hyberbolic sine of.
    """
    return generic_function(math.sinh, value, derivative = cosh)

def asinh(value: Supported) -> Supported:
    """
        Computes the inverse hyberbolic sine of a value.

        Parameters
        ----------

        value   
            The number to compute the inverse hyberbolic sine of.
    """
    return generic_function(math.asinh, value)

def tanh(value: Supported) -> Supported:
    """
        Computes the hyberbolic tangent of a value.

        Parameters
        ----------

        value   
            The number to compute the hyberbolic tangent of.
    """
    return generic_function(math.tanh, value)

def atanh(value: Supported) -> Supported:
    """
        Computes the inverse hyberbolic tangent of a value.

        Parameters
        ----------

        value   
            The number to compute the inverse hyberbolic tangent of.
    """
    return generic_function(math.atanh, value)