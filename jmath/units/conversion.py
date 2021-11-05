'''
    Provides the standard conversion table, shared for all units
'''

# - Imports

from typing import Callable, TypeVar, Union

# - Types

Unit = TypeVar("Unit")

# - Globals

conversion_table = {}
alias_table = {}

# - Functions

def define_conversion(from_unit: Unit, to_unit: Unit, factor: Union[float, Callable[[float], float]]):
    """
        Defines the conversion between two units
        
        Parameters
        ----------
        
        from_unit
            The unit to convert from.
        to_unit
            The unit to convert to.
        factor
            The factor to multiply by or a function to produce the difference.
            If a factor is passed then the reverse conversion is added by default.
            If a function is passed then the reverse conversion is not added by default.
    """

    global conversion_table

    # If factor is float/int then make a lambda
    if isinstance(factor, (float, int)):
        # Create reverse
        reversed = lambda x: x / factor
        # Add reversed to table
        define_conversion(to_unit, from_unit, reversed)
        # Create standard factor
        factor = lambda x: x * factor

    # Overwrite units to be "base" units 
    to_unit = to_unit.copy(1)
    from_unit = from_unit.copy(1)

    # Add to conversion table
    if from_unit not in conversion_table:
        conversion_table[from_unit] = {to_unit: factor}
    else:
        conversion_table[from_unit][to_unit] = factor

def define_alias(base_unit: Unit, end_unit: Unit):
    """
        Defines an alias for a unit

        Parameters
        ----------

        base_unit
            The base level unit.
        end_unit
            The unit that is an alias for the base unit.
    """

    global alias_table

    # Add to alias table
    alias_table[base_unit.copy(1)] = end_unit.copy(1)
