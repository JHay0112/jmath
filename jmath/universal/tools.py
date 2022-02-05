'''
    Provides tools for creating universal functions.
'''

# - Imports

from typing import Union, Callable
from ..uncertainties import Uncertainty
from ..units import Unit
from ..approximation.autodiff import Variable, Function

# - Typing

Supported = Union[float, int, Uncertainty, Unit, Variable]
Numeric = Union[float, int]

# - Functions

def generic_function(func: Callable[[Numeric], Numeric], input: Supported, *args) -> Union[Supported, Function]:
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
    elif isinstance(input, Variable):
        # Auto-diff Variables
        # Build auto-diff function
        auto_func = Function(func)
        # Register variable as input
        auto_func.input(input)
        # Return the function
        return auto_func
    else:
        # Anything else
        return func(input, *args)