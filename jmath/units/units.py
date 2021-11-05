'''
    Defines the unit class and its behaviour
'''

# - Imports

from typing import Union
from .conversion import conversion_table

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
            if power < 0:
                unit_str += f"{unit}^({power})"
            elif power > 1:
                unit_str += f"{unit}^{power} "
            else:
                unit_str += f"{unit}"

        unit_str.strip()

        # Show value + unit_str
        return f"{self.value} [{unit_str}]"

    def __hash__(self):
        """Hashing based on string representation."""
        return hash(str(self))

    def copy(self, value: float = None, flip_powers = False) -> "Unit":
        """
            Produces a copy of the unit.

            Parameters
            ----------

            value
                Optional overwrite of value.
            flip_powers
                Optional flipping of powers.
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

        # If flip signs is true
        if flip_powers:
            # Go through dictionary and flip them
            for unit, power in new_unit.units.items():
                new_unit.units[unit] = -power

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

    def __truediv__(self, other: Union[int, float, "Unit"]) -> "Unit":
        """Float division."""
        # Floats/ints
        if isinstance(other, (float, int)):
            # Returns new unit with new value
            return self.copy(self.value / other)
        else:
            # Presuming other is a unit now
            # Flip its signs
            other = other.copy(flip_powers = True)
            # Compute union
            new_unit = self | other
            # Return new unit 
            return new_unit * self.value/other.value

    def __rtruediv__(self, other: Union[int, float, "Unit"]) -> "Unit":
        """Reversed float division."""
        # Flip own values
        new_unit = self.copy(value = 1/self.value, flip_powers = True)
        # Multiply
        return new_unit * other
        