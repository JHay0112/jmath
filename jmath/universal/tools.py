'''
    Provides tools for creating universal functions.
'''

# - Imports

from typing import Union, Callable
from ..uncertainties import Uncertainty
from ..units import Unit
from ..autodiff import Variable, Function

# - Typing

Supported = Union[float, int, Uncertainty, Unit, Variable, Function]
Numeric = Union[float, int]

# - Functions

def generic_function(func: Callable[[Numeric], Numeric], input: Supported, *args, derivative: Callable = None) -> Union[Supported, Function]:
    """
        Applies a function with generic cases for special objects.
        
        Parameters
        ----------
        
        func
            The function to apply.
        args
            Arguments to send to the function
        derivatives
            The partial derivatives of the function with respect to its variables
    """

    if isinstance(input, Unit):
        # Units
        # Return function applied to unit value
        return generic_function(func, input.value, *args) * input.copy(1)
    elif isinstance(input, Uncertainty):
        # Uncertainties
        return input.apply(func, *args)
    elif isinstance(input, (Function, Variable)):
        # Auto-diff Variables/Functions
        # Check that there is a derivative
        if derivative is None:
            return NotImplemented
        # Build auto-diff function
        f = Function(func, derivative)
        f.register(input)
        return f
    else:
        # Anything else
        return func(input, *args)