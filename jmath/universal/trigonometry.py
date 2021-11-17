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
            Value (in radians) to compute the sine of.
    '''
    return generic_function(math.sin, input)

@annotate
def asin(input: Supported) -> other.radian:
    '''
        Computes the inverse sine of the input.

        Parameters
        ----------

        input
            Value to compute the inverse sine of.

        Returns
        -------

        Unit
            Radians
    '''
    return generic_function(math.asin, input)

@annotate
def cos(input: other.radian) -> Supported:
    '''
        Computes the cosine of the input.

        Parameters
        ----------

        input
            Value (in radians) to compute the cosine of
    '''
    return generic_function(math.cos, input)

@annotate
def acos(input: Supported) -> other.radian:
    '''
        Computes the inverse cosine of the input.

        Parameters
        ----------

        input
            Value to compute the inverse cosine of.

        Returns
        -------

        Unit
            Radians
    '''
    return generic_function(math.acos, input)

@annotate
def tan(input: other.radian) -> Supported:
    '''
        Computes the tangent of the input.

        Parameters
        ----------

        input
            Value (in radians) to compute the tangent of
    '''
    return generic_function(math.tan, input)

@annotate
def atan(input: Supported) -> other.radian:
    '''
        Computes the inverse tangent of the input.

        Parameters
        ----------

        input
            Value to compute the inverse tangent of.

        Returns
        -------

        Unit
            Radians
    '''
    return generic_function(math.atan, input)