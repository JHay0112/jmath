'''
    Provides functions to allow for annotation of functions to enforce units.
'''

# - Imports

from functools import wraps
from inspect import getcallargs
from typing import Callable
from .units import Unit

# - Functions

def annotation(func: Callable) -> Callable:
    """
        Converts the units of a function to those specified in function annotations.

        Parameters
        ----------

        func
            The wrapped function to process.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        args = list(args)
        # Go through each annotation
        i = 0
        for arg, val in getcallargs(func, *args, **kwargs).items():
            # Get type
            unit = func.__annotations__[arg]
            # Check it is a unit
            # If its not then we ignore
            if isinstance(unit, Unit):
                # It is so reduce it
                unit = unit.copy(1)
                # Check if value is
                if isinstance(val, Unit):
                    # It is so let us convert it
                    args[i] = val.convert_to(unit)
                else:
                    # It's not, we'll asumme it's correct
                    args[i] = val * unit
            i += 1
        # Run function
        args = tuple(args)
        return_value = func(*args, **kwargs)
        # Now check returned value
        if "return" in func.__annotations__:
            unit = func.__annotations__["return"]
            # Check that the unit is a unit
            # If not then ignore it
            if isinstance(unit, Unit):
                # It is so reduce it
                unit = unit.copy(1)
                # Check if value is a unit
                if isinstance(return_value, Unit):
                    # It is so convert
                    return_value = return_value.convert_to(unit)
                else:
                    # None so assume true
                    return_value *= unit
        # Return value
        return return_value

    # Return wrapper function
    return wrapper