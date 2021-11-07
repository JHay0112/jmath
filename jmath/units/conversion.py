'''
    Provides the standard conversion table, shared for all units
'''

# - Imports

from typing import Callable, Union, TYPE_CHECKING

# - Types

if TYPE_CHECKING:
    # Only import for type checking
    from .units import Unit

# - Globals

conversion_table = {}
alias_table = {}

# - Functions

def define_conversion(from_unit: 'Unit', to_unit: 'Unit', factor: Union[float, 'Unit', Callable[[float], float]]):
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
    if not callable(factor):
        # Create reverse
        reversed = lambda x: x / factor
        # Add reversed to table
        define_conversion(to_unit, from_unit, reversed)
        # Create standard factor
        func = lambda x: x * factor
    else:
        func = factor

    # Overwrite units to be "base" units 
    to_unit = to_unit.copy(1)
    from_unit = from_unit.copy(1)

    # Add to conversion table
    if from_unit not in conversion_table:
        conversion_table[from_unit] = {to_unit: func}
    else:
        conversion_table[from_unit][to_unit] = func

def define_alias(base_unit: 'Unit', end_unit: 'Unit'):
    """
        Defines an alias for a unit

        Parameters
        ----------

        base_unit
            The base level unit.
        end_unit
            The unit that is an alias for the base unit.

        Notes
        -----

        Would be good for this to calculate decays of the alias to so that they can revert.
    """

    global alias_table

    base_unit = base_unit.copy(1)
    end_unit = end_unit.copy(1)

    # Add to alias table
    alias_table[base_unit] = end_unit

    # Simple alias decay cases
    # For each sub unit of the base unit
    for unit, power in base_unit.units.items():
        # Create copies
        new_end_unit = end_unit.copy()
        # Invert
        new_end_unit.units[unit] = -power
        
        # Create a case in alias table going back to the base units
        # Make sure it's not already in the table before doing more work
        # We don't want to overwrite other aliases
        if new_end_unit not in alias_table:
            # Create the base unit
            new_base_unit = base_unit.copy()
            new_base_unit.units.pop(unit)
            # Now alias
            alias_table[new_end_unit] = new_base_unit
