'''
    Provides the standard conversion table, shared for all units
'''

# - Imports

from typing import Callable, TypeVar, Union

# - Types

Unit = TypeVar("Unit")

# - Globals

conversion_table = {}

# - Functions

def define_conversion(from_unit: Union[Unit, str], to_unit: Union[Unit, str], factor: Union[float, Callable[[float], float]]):
    """
        Defines the conversion between two units
        
        Parameters
        ----------
        
        from_unit
            The unit to convert from
        to_unit
            The unit to convert to
        factor
            The factor to multiply by or a function to produce the difference.
            If a factor is passed then the reverse conversion is added by default.
            If a function is passed then the reverse conversion is not added by default.
    """

    global conversion_table
    
    # Change units to strings if appropriate
    if not isinstance(from_unit, str):
        from_unit = from_unit.unit
    if not isinstance(to_unit, str):
        to_unit = to_unit.unit

    # If factor is float/int then make a lambda
    if isinstance(factor, (float, int)):
        # Create reverse
        reversed = lambda x: x / factor
        # Add reversed to table
        define_conversion(to_unit, from_unit, reversed)
        # Create standard factor
        factor = lambda x: x * factor

    # Add to conversion table
    if from_unit not in conversion_table:
        conversion_table[from_unit] = {to_unit: factor}
    else:
        conversion_table[from_unit][to_unit] = factor
