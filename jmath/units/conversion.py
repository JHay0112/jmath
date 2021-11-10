'''
    Unit Spaces.
    For management of unit conversions and aliases.
'''

# - Imports

from typing import Callable, Union, Optional, TYPE_CHECKING
from ..exceptions import NoConversion

# - Types

if TYPE_CHECKING:
    # Only import for type checking
    from .units import Unit

# - Classes

class UnitSpace:
    '''
        Management for units and unit conversions.
    '''
    def __init__(self):

        self.conversion_table = {}
        self.alias_table = {}
        self.units = {}

    def __getitem__(self, item: str) -> 'Unit':
        """Get Item from Units."""
        return self.units[item]

    def __setitem__(self, item: str, new_value: 'Unit'):
        """Set Item in Units."""
        self.units[item] = new_value

    def __getattr__(self, item: str) -> 'Unit':
        """Get Attributes of Object."""
        try:
            # Get it the normal way
            return self.__getattribute__(item)
        except AttributeError:
            # Get it from items
            if type(item).__name__ == "Unit":
                item = item.unit_str()
            return self.units[item]

    def __setattr__(self, item: str, new_value: 'Unit'):
        """Set Attribute of Object."""
        if type(new_value).__name__ == "Unit":
            # If not an attribute then add to units
            # Ensure unit space is set correctly
            new_value.unit_space = self
            self.units[item] = new_value
        else:
            # Else call setattribute
            super().__setattr__(item, new_value)

    def define_alias(self, base_unit: Union['Unit', str], end_unit: 'Unit'):
        """
            Defines an alias from unit to another.

            Parameters
            ----------

            base_unit
                The unit to start at.
            end_unit
                The unit to end at.
        """
        if type(base_unit).__name__ == "Unit":
            # For units
            base_unit = base_unit.copy(1)
            end_unit = end_unit.copy(1)

            # Add to alias table
            self.alias_table[base_unit.unit_str()] = end_unit

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
                if new_end_unit.unit_str() not in self.alias_table:
                    # Create the base unit
                    new_base_unit = base_unit.copy()
                    new_base_unit.units.pop(unit)
                    # Now alias
                    self.alias_table[new_end_unit.unit_str()] = new_base_unit
        elif isinstance(base_unit, str):
            # Creating a human alias
            self.units[base_unit] = end_unit

    def alias(self, unit: 'Unit') -> Optional['Unit']:
        """
            Produces the alias of a unit.

            Parameters
            ----------

            unit
                The unit to find the alias of.
        """
        unit = unit.unit_str()

        if unit in self.alias_table:
            return self.alias_table[unit]
        else:
            return None

    def define_conversion(self, from_unit: 'Unit', to_unit: 'Unit', factor: Union[float, 'Unit', Callable[[float], float]]):
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

        if from_unit.unit_str() not in self.units.keys():
            self.units[from_unit.unit_str()] = from_unit
        if to_unit.unit_str() not in self.units.keys():
            self.units[to_unit.unit_str()] = to_unit

        # If factor is float/int then make a lambda
        if not callable(factor):
            # Create reverse
            reversed = lambda x: x / factor
            # Add reversed to table
            self.define_conversion(to_unit, from_unit, reversed)
            # Create standard factor
            func = lambda x: x * factor
        else:
            func = factor

        # Overwrite units to be "base" units 
        to_unit = to_unit.copy(1)
        from_unit = from_unit.copy(1)

        # Add to conversion table
        if from_unit.unit_str() not in self.conversion_table:
            self.conversion_table[from_unit.unit_str()] = {to_unit.unit_str(): func}
        else:
            self.conversion_table[from_unit.unit_str()][to_unit.unit_str()] = func

    def convert(self, from_unit: 'Unit', to_unit: 'Unit') -> Optional['Unit']:
        '''
            Converts a unit to another unit if possible.

            Parameters
            ----------

            from_unit
                The unit to convert from
            to_unit
                The unit to convert to

            Raises
            ------

            NoConversion
                Raises the no conversion error if there is no way to conver the unit.
        '''

        # Trivial conversion case
        if from_unit.units == to_unit.units:
            return from_unit

        new_unit = to_unit.copy(1)

        # Convert numeric value
        try:
            new_unit.value = self.conversion_table[from_unit.unit_str()][to_unit.unit_str()](from_unit.value)
        except KeyError:
            raise NoConversion(from_unit, to_unit)

        # Incase used in formula
        return new_unit

# - Globals

universal = UnitSpace()
# For compatibility
conversion_table = universal.conversion_table
alias_table = universal.alias_table
define_conversion = universal.define_conversion
define_alias = universal.define_alias