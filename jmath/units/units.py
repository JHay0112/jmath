'''
    Defines the unit class and its behaviour
'''

# - Imports

from typing import Union
from .conversion import conversion_table, alias_table
from ..uncertainties import Uncertainty
from ..exceptions import NoConversion

# - Classes

class Unit:
    '''
        A value with an associated unit.

        Parameters
        ----------

        unit
            String identifier of unit e.g. "m" 

        Examples
        --------

        >>> print(3 * Unit("m")/Unit("s"))
        3 [ms^(-1)]   
    '''

    def __init__(self, unit: str = None):

        global conversion_table
        
        self.value = 1
        
        if unit is not None:
            self.units = {unit: 1}
        else:
            self.units = {}

    def __repr__(self):
        """Programming Representation."""

        return str(self)

    def __str__(self):
        """String representation."""

        # Produce a string of the units
        unit_str = ""

        for unit, power in self.units.items():
            if power < 0:
                unit_str += f"{unit}^({power})"
            elif power > 1:
                unit_str += f"{unit}^{power} "
            else:
                unit_str += f"{unit}"

        unit_str.strip()

        if isinstance(self.value, Uncertainty):
            # Special uncertainty display
            return f"({self.value}) [{unit_str}]"
        else:
            # Show value + unit_str
            return f"{self.value} [{unit_str}]"

    def __hash__(self):
        """Hashing based on string representation."""
        return hash(str(self))

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

        global alias_table

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

        # Check for alias
        if new_unit.copy(1) in alias_table:
            new_unit = new_unit.value * alias_table[new_unit.copy(1)]

        return new_unit

    def __eq__(self, other: "Unit") -> bool:
        """Equality comparison."""
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

        global conversion_table

        # Trivial conversion case
        if self.units == other.units:
            return self

        new_unit = Unit()

        # Convert numeric value
        try:
            new_unit.value = conversion_table[self.copy(1)][other.copy(1)](self.value)
        except KeyError:
            raise NoConversion(self, other)

        # Check if units have got into one another
        # Hacky solution but it will do
        while isinstance(new_unit.value, Unit):
            new_unit.value = new_unit.value.value

        # Convert unit value
        new_unit.units = other.units

        # Incase used in formula
        return new_unit