'''
    Provides a class to deal with values with associated uncertainty.
'''

# - Modules

import math
from typing import Callable, Union, List

# - Functions

def half_range(data: List[float]) -> float:
    """
        Calculates the absolute uncertainty associated with a set of data.

        Parameters
        ----------

        data
            List/tuple of the data
    """

    return (max(data) - min(data))/2

def mean(data: List[float]) -> "Uncertainty":
    """
        Calculates the mean of a set of data and it's uncertainty by the half range rule.

        Parameters
        ----------

        data
            List/tuple of data to take the mean of.
    """
    
    return Uncertainty(sum(data)/len(data), half_range(data))

# - Classes
class Uncertainty:
    """
        A value with an associated uncertainty.

        Parameters
        ----------

        value
            The value associated with an uncertainty
        uncertainty
            Uncertainty associated with the value

        Examples
        --------

        >>> Uncertainty(3, 1) + Uncertainty(4, 2)
        Uncertainty(7, 3)

        >>> Uncertainty(10, 1) - Uncertainty(2, 1)
        Uncertainty(8, 2)

        >>> 2 * Uncertainty(2, 1)
        Uncertainty(4, 2.0)

        >>> Uncertainty(2, 1) + Uncertainty(4, 1)
        Uncertainty(8, 6.0)

        >>> Uncertainty(20, 2) / Uncertainty(2, 0.5)
        Uncertainty(10.0, 3.5)
    """
    def __init__(self, value: float, uncertainty: float):
        
        self.value = value
        self.uncertainty = abs(uncertainty)

    def abs_uncertainty(self) -> float: 
        """Returns the absolute uncertainty."""
        return(self.uncertainty)

    def rel_uncertainty(self) -> float: 
        """Returns the relative uncertainty as proportion."""
        try:
            return abs(self.uncertainty/self.value)
        except ZeroDivisionError:
            return 0

    def apply(self, func: Callable[[float], float], *args) -> "Uncertainty":
        """
            Applies a mathematical function to the value using the bruteforce method to calculate the new uncertainty.

            Parameters
            ----------

            func
                The function to apply.
            args
                Additional arguments to send to the function.
        """
        # Apply function to the value
        val = func(self.value, *args)
        # Apply the function to the value plus the uncertainty and then take away the new val
        unc = func(self.value + self.uncertainty, *args) - val

        return Uncertainty(val, unc)

    def __repr__(self):
        """Programming representation"""
        return f"Uncertainty({self.value}, {self.uncertainty})"

    def __str__(self):
        """String representation"""
        # Calculates the amount to round by for correct formatting
        # "Round" uncertainty to one significant digit
        if self.uncertainty != 0:
            rounded_uncertainty = round(self.uncertainty, -int(math.floor(math.log10(abs(self.uncertainty)))))
            # Find index of significant digit
            # If the rounded uncertainty is an integer
            if rounded_uncertainty.is_integer():
                # Then we know the first signifigant digit is at its negative length
                rounding = -len(str(rounded_uncertainty)) + 2
            else:
                # Not integer, so first signifigant digit is at positive length
                rounding = len(str(rounded_uncertainty)) - 2 # Offset for correct position

            if self.value < 0 and rounding < 0:
                # For negative numbers
                # Add extra to rounding
                rounding -= 1
            if self.value > 0 and rounding < 0:
                rounding += 1
            
            # Round the main value with this
            rounded_value = round(self.value, rounding)

        else:
            # If uncertainty is zero
            rounded_value = self.value
            rounded_uncertainty = self.uncertainty

        if rounded_uncertainty.is_integer():
            # Integer matching
            rounded_value = int(rounded_value)
            rounded_uncertainty = int(rounded_uncertainty)

        # Rounded values
        return(f"{rounded_value} ± {rounded_uncertainty}")

    def __contains__(self, other: Union[int, float, "Uncertainty"]) -> bool:
        """
            Checks if uncertainties overlap.
            
            Parameters
            ----------
            
            other
                The int, float, or Uncertainty to check for overlap
        """

        # Float/Int
        if isinstance(other, int) or isinstance(other, float):
            # Check if value lies within uncertainty bounds
            return other <= (self.value + self.uncertainty) and other >= (self.value - self.uncertainty)
        elif isinstance(other, Uncertainty):
            # Check for overlap between values
            # Check for overlap in lower bound
            lower_bound = (self.value - self.uncertainty) in other or (other.value - other.uncertainty) in self
            # Check for overlap in upper bound
            upper_bound = (self.value + self.uncertainty) in other or (other.value + other.uncertainty) in self

            return upper_bound or lower_bound

    def __round__(self, dp: int):
        """Returns the value rounded"""
        return round(self.value, dp)

    def __float__(self):
        """Float form"""
        return self.value

    def __add__(self, other: Union["Uncertainty", float, int]) -> "Uncertainty":
        """Uncertainty addition"""
        # Check type of other
        if type(other) == Uncertainty:
            # Add values
            val = self.value + other.value
            # Add absolute uncertainties
            unc = self.abs_uncertainty() + other.abs_uncertainty()
        elif isinstance(other, (float, int)): # Presume int or float
            # Add values
            val = self.value + other
            # Final uncertainty stays the same
            unc = self.abs_uncertainty()
        else:
            return NotImplemented

        # Return Uncertainty
        return(Uncertainty(val, unc))

    def __radd__(self, other: Union["Uncertainty", float, int]) -> "Uncertainty": 
        """Flipped uncertainty addition"""
        return(self + other) 

    def __sub__(self, other: Union["Uncertainty", float, int]) -> "Uncertainty":
        """Uncertainty subtraction"""
        # Check type of other
        if type(other) == Uncertainty:
            # Add values
            val = self.value - other.value
            # Add absolute uncertainties
            unc = self.abs_uncertainty() + other.abs_uncertainty()
        elif isinstance(other, (float, int)): # Presume int or float
            # Add values
            val = self.value - other
            # Final uncertainty stays the same
            unc = self.abs_uncertainty()
        else:
            return NotImplemented

        # Return Uncertainty
        return(Uncertainty(val, unc))

    def __rsub__(self, other: Union["Uncertainty", float, int]) -> "Uncertainty": 
        """Flipped uncertainty subtraction"""
         # Check type of other
        if type(other) == Uncertainty:
            # Add values
            val = other.value - self.value
            # Add absolute uncertainties
            unc = self.abs_uncertainty() + other.abs_uncertainty()
        elif isinstance(other, (float, int)): # Presume int or float
            # Add values
            val = other - self.value
            # Final uncertainty stays the same
            unc = self.abs_uncertainty()
        else:
            return NotImplemented

        # Return Uncertainty
        return(Uncertainty(val, unc))

    def __mul__(self, other: Union["Uncertainty", float, int]) -> "Uncertainty":
        """Uncertainty multiplication"""
        # Check type of other
        if type(other) == Uncertainty:
            # Get final value
            val = self.value * other.value
            # Add relative uncertainties and multiply the sum by final value
            unc = val * (self.rel_uncertainty() + other.rel_uncertainty())
        elif isinstance(other, (float, int)): # Presume int or float
            # Get final value
            val = self.value * other
            # Multiply final by current relative uncertainty
            unc = val * self.rel_uncertainty()
        else:
            return NotImplemented

        # Return Uncertainty
        return(Uncertainty(val, unc))

    def __rmul__(self, other: Union["Uncertainty", float, int]) -> "Uncertainty": 
        """Flipped uncertainty multiplication"""
        return(self * other) 

    def __truediv__(self, other: Union["Uncertainty", float, int]) -> "Uncertainty":
        """Uncertainty multiplication"""
        # Check type of other
        if type(other) == Uncertainty:
            # Get final value
            val = self.value / other.value
            # Add relative uncertainties and multiply the sum by final value
            unc = val * (self.rel_uncertainty() + other.rel_uncertainty())
        elif isinstance(other, (float, int)): # Presume int or float
            # Get final value
            val = self.value / other
            # Multiply final by current relative uncertainty
            unc = val * self.rel_uncertainty()
        else:
            return NotImplemented

        # Return Uncertainty
        return(Uncertainty(val, unc))

    def __rtruediv__(self, other: Union["Uncertainty", float, int]) -> "Uncertainty": 
        """Flipped uncertainty division"""
        # Check type of other
        if type(other) == Uncertainty:
            # Get final value
            val = other.value / self.value
            # Add relative uncertainties and multiply the sum by final value
            unc = val * (self.rel_uncertainty() + other.rel_uncertainty())
        elif isinstance(other, (float, int)): # Presume int or float
            # Get final value
            val = other / self.value
            # Multiply final by current relative uncertainty
            unc = val * self.rel_uncertainty()
        else:
            return NotImplemented

        # Return Uncertainty
        return(Uncertainty(val, unc))

    def __pow__(self, power: float):
        """Raise to power, brute forced"""
        f = lambda x: x ** power
        return self.apply(f)