'''
    Provides tools for creating universal functions.
'''

# - Imports

from typing import Union, Callable
from ..uncertainties import Uncertainty
from ..units import Unit

# - Typing

Supported = Union[float, int, Uncertainty, Unit]

# - Functions

def generic_function(func: Callable[[float], float], input: Supported, *args) -> Supported:
    """
        Applies a function with generic cases for special objects.
        
        Parameters
        ----------
        
        func
            The function to apply.
        args
            Arguments to send to the function
    """
    if isinstance(input, Unit):
        # Units
        # Return function applied to unit value
        return generic_function(func, input.value, *args) * input.copy(1)
    elif isinstance(input, Uncertainty):
        # Uncertainties
        return input.apply(func, *args)
    else:
        # Anything else
        return func(input, *args)