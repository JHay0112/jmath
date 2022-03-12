'''
    Trigonometric Functions
'''

# - Imports

from ..units import annotate, other
from .tools import generic_function, Supported
import math

# - Functions

@annotate
def sin(value: other.radian) -> Supported:
    '''
        Computes the sine of the value.

        Parameters
        ----------

        value
            Value (in radians) to compute the sine of.
    '''
    return generic_function(math.sin, value, derivative = cos)

@annotate
def asin(value: Supported) -> other.radian:
    '''
        Computes the inverse sine of the value.

        Parameters
        ----------

        value
            Value to compute the inverse sine of.

        Returns
        -------

        Unit
            Radians
    '''
    return generic_function(math.asin, value)

@annotate
def cos(value: other.radian) -> Supported:
    '''
        Computes the cosine of the value.

        Parameters
        ----------

        value
            Value (in radians) to compute the cosine of
    '''
    return generic_function(math.cos, value, derivative = lambda x: -sin(x))

@annotate
def acos(value: Supported) -> other.radian:
    '''
        Computes the inverse cosine of the value.

        Parameters
        ----------

        value
            Value to compute the inverse cosine of.

        Returns
        -------

        Unit
            Radians
    '''
    return generic_function(math.acos, value)

@annotate
def tan(value: other.radian) -> Supported:
    '''
        Computes the tangent of the value.

        Parameters
        ----------

        value
            Value (in radians) to compute the tangent of
    '''
    return generic_function(math.tan, value)

@annotate
def atan(value: Supported) -> other.radian:
    '''
        Computes the inverse tangent of the value.

        Parameters
        ----------

        value
            Value to compute the inverse tangent of.

        Returns
        -------

        Unit
            Radians
    '''
    return generic_function(math.atan, value)