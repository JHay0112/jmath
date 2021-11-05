'''
    Defines the unit class and its behaviour
'''

# - Imports

from typing import Union, Dict
from .default import conversion_table

# - Classes

class Unit:
    '''
        A value with an associated unit.

        Parameters
        ----------

        unit
            String identifier of unit e.g. "m"        
    '''

    def __init__(self, unit: str = None):
        
        self.value = 1
        
        if unit is not None:
            self.units = {unit: 1}
        else:
            self.units = {}

    def __str__(self):
        """String representation."""

        # Produce a strign of the units
        unit_str = ""

        for unit, power in self.units.items():
            if power != 1:
                unit_str += f"({unit}^{power})"
            else:
                unit_str += f"{unit}"

        # Show value + unit_str
        return f"{self.value} [{unit_str}]"

    def __hash__(self):
        """Hashing based on string representation."""
        return hash(str(self))

    def copy(self, value: float = None) -> "Unit":
        """
            Produces a copy of the unit.

            Parameters
            ----------

            value
                Optional overwrite of value.
        """
        # Placeholder unit
        new_unit = Unit()
        # If value is not none then write new value
        if value is not None:
            new_unit.value = value
        else:
            # Else keep the current
            new_unit.value = self.value
        # Copy units over
        new_unit.units = dict(self.units)

        # Return
        return new_unit

    def union(self, other: "Unit") -> "Unit":
        """
            Constructs the union of two units.
            Ignores values.

            Parameters
            ----------

            other
                The other set to construct the union with.
        """

        # Place holder unit
        new_unit = Unit()
        
        # Construct mix of dicts
        # Copy own dict
        units = dict(self.units)
        # Now go through other dict
        for unit, power in other.units.items():
            # Check if not in dict
            if unit not in units:
                units[unit] = power
            else:
                # If already in calculate the new power
                new_power = units[unit] + power
                # If zero then remove
                if new_power == 0:
                    units.pop(unit)
        # New units constructed
        # Replace in the placeholder unit
        new_unit.units = units

        return new_unit

    def __or__(self, other: "Unit") -> "Unit":
        """Union operator."""
        return self.union(other)

    def __mul__(self, other: Union[int, float, "Unit"]) -> "Unit":
        """Multiplication. Also used for unit value instantiaton."""
        # Floats/ints
        if isinstance(other, (float, int)):
            # Return new unit with value
            return self.copy(self.value * other)
        else:
            # Presuming the other one is a unit
            # Calculate new unit with union
            new_unit = self | other
            # Multiply new unit by value
            return new_unit * other.value * self.value

    def __rmul__(self, other: Union[int, float, "Unit"]) -> "Unit":
        """Reversed multiplication, same as normal."""
        return self * other