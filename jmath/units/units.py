'''
    Defines the unit class and its behaviour
'''

# - Imports

from typing import Union
from .conversion import universal, UnitSpace
from ..uncertainties import Uncertainty

# - Classes

class Unit:
    '''
        A value with an associated unit.

        Parameters
        ----------

        unit
            String identifier of unit e.g. "m" 
        unit_space
            The unit space the unit exists in.

        Examples
        --------

        >>> print(3 * Unit("m")/Unit("s"))
        3 [ms^(-1)]   
    '''

    def __init__(self, unit: str = None, unit_space: UnitSpace = None):
        
        self.value = 1
        
        if unit is not None:
            self.units = {unit: 1}
        else:
            self.units = {}

        self._unit_space = unit_space

    @property
    def unit_space(self):
        """The Unitspace in which the Unit Exists."""
        if self._unit_space is None:
            # If none has been set
            self._unit_space = universal

        return self._unit_space

    @unit_space.setter
    def unit_space(self, new_unit_space: UnitSpace):
        """Set a unitspace"""
        
        # Set new unit space
        self._unit_space = new_unit_space

        # If not in unit space
        if self.unit_str() not in self.unit_space.units.keys():
            # Then add it
            self.unit_space[self.unit_str()] = self

    def __repr__(self):
        """Programming Representation."""

        return str(self)

    def __str__(self):
        """String representation."""

        # Produce a string of the units
        unit_str = self.unit_str()

        if isinstance(self.value, Uncertainty):
            # Special uncertainty display
            return f"({self.value}) [{unit_str}]"
        else:
            # Show value + unit_str
            return f"{self.value} [{unit_str}]"

    def __abs__(self):
        """Returns absolute value."""
        return abs(self.value)

    def __float__(self):
        """Returns float representation."""
        return float(self.value)

    def __int__(self):
        """Returns integer representation."""
        return int(self.value)

    def __round__(self, precision):
        """Rounds to precision."""
        return self.copy(value = round(self.value, precision))

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
        new_unit = Unit(unit_space = self.unit_space)
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

    def unit_str(self) -> str:
        """Produces a string describing the unit."""
        unit_str = ""

        for unit, power in self.units.items():
            if power < 0:
                unit_str += f"{unit}^({power})"
            elif power > 1:
                unit_str += f"{unit}^{power}"
            else:
                unit_str += f"{unit}"

        unit_str.strip()

        return unit_str

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
        new_unit = Unit(unit_space = self.unit_space)
        
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
                else:
                    units[unit] = new_power
        # New units constructed
        # Replace in the placeholder unit
        new_unit.units = units

        # Check for alias
        alias = self.unit_space.alias(new_unit)
        if alias is not None:
            new_unit = new_unit.value * alias

        return new_unit

    def __eq__(self, other: Union["Unit", float, int]) -> bool:
        """Equality comparison."""
        if isinstance(other, (int, float)):
            return self.value == other
        else:
            return (self.value == other.value) and (self.units == other.units)

    def __lt__(self, other: "Unit") -> bool:
        """Less than comparison."""
        return self.value < other.value

    def __leq__(self, other: "Unit") -> bool:
        """Less than or equal comparison."""
        return self.value <= other.value

    def __gt__(self, other: "Unit") -> bool:
        """Greater than comparison."""
        return self.value > other.value

    def __geq__(self, other: "Unit") -> bool:
        """Greather than or equal comparison."""
        return self.value >= other.value

    def __or__(self, other: "Unit") -> "Unit":
        """Union operator."""
        return self.union(other)

    def __mul__(self, other: Union[int, float, "Unit", Uncertainty]) -> "Unit":
        """Multiplication. Also used for unit value instantiaton."""
        # Floats/ints
        if isinstance(other, (float, int, Uncertainty)):
            # Return new unit with value
            return self.copy(self.value * other)
        else:
            # Presuming the other one is a unit
            # Calculate new unit with union
            new_unit = self | other
            # Multiply new unit by value
            return new_unit * other.value * self.value

    def __rmul__(self, other: Union[int, float, "Unit", Uncertainty]) -> "Unit":
        """Reversed multiplication, same as normal."""
        return self * other

    def __truediv__(self, other: Union[int, float, "Unit", Uncertainty]) -> "Unit":
        """Float division."""
        # Floats/ints
        if isinstance(other, (float, int, Uncertainty)):
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

    def __rtruediv__(self, other: Union[int, float, "Unit", Uncertainty]) -> "Unit":
        """Reversed float division."""
        # Flip own values
        new_unit = self.copy(value = 1/self.value, flip_powers = True)
        # Multiply
        return new_unit * other
        
    def __add__(self, other: Union[int, float, "Unit", Uncertainty]) -> "Unit":
        """Addition."""
        if isinstance(other, Unit) and self.units == other.units:
            # Only permit unit addition on equal values
            return self.copy(value = self.value + other.value)
        else:
            # Non unitary addition
            return self.copy(value = self.value + other)

    def __radd__(self, other: Union[int, float, "Unit", Uncertainty]) -> "Unit":
        """Reversed Addition."""
        # Directionless
        return self + other

    def __sub__(self, other: Union[int, float, "Unit", Uncertainty]) -> "Unit":
        """Subtraction."""
        if isinstance(other, Unit) and self.units == other.units:
            # Only permit unit addition on equal values
            return self.copy(value = self.value - other.value)
        else:
            # Non unitary addition
            return self.copy(value = self.value - other)

    def __rsub__(self, other: Union[int, float, "Unit", Uncertainty]) -> "Unit":
        """Reversed Subtraction."""
        if isinstance(other, Unit) and self.units == other.units:
            # Only permit unit addition on equal values
            return self.copy(value = other.value - self.value)
        else:
            # Non unitary addition
            return self.copy(value = other - self.value)

    def __pow__(self, other: Union[float, int]) -> "Unit":
        """Raise to power."""
        # Create a copy
        new_unit = self.copy(value = self.value ** other)
        # Multiply powers
        for unit in new_unit.units.keys():
            new_unit.units[unit] *= other

        return new_unit

    def convert_to(self, other: "Unit"):
        """
            Converts the current unit to the given unit.

            Parameters
            ----------

            other
                The type of unit to convert to.    
        """

        return self.unit_space.convert(self, other)