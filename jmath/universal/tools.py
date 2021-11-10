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

def generic_function(func: Callable[[float], float], input: Supported) -> Supported:
    """
        Applies a function with generic cases for special objects.
        
        Parameters
        ----------
        
        func
            The function to apply.
        input
            The input to process with the function.
    """
    if isinstance(input, Unit):
        # Units
        # Return function applied to unit value
        return generic_function(func, input.value) * input.copy(1)
    elif isinstance(input, Uncertainty):
        # Uncertainties
        return input.apply(func)
    else:
        # Anything else
        return func(input)