'''
    jmath/uncertainties.py

    Author: Jordan Hay
    Date: 2021-06-17

    For dealing with values and their associated uncertainties
'''

# - Modules

import math

# - Classes
class Uncertainty:

    def __init__(self, value, uncertainty):
        """
            A value with an associated uncertainty

            value (float) - The absolute value
            uncertainty (float) - The absolute uncertainty

            Author: Jordan Hay
            Date: 2021-03-17
        """
        self.value = value
        self.uncertainty = uncertainty

    def abs_uncertainty(self): 
        """Returns the absolute uncertainty"""
        return(self.uncertainty)

    def rel_uncertainty(self): 
        """Returns the relative uncertainty as proportion"""
        return(self.uncertainty/self.value)

    def apply(self, func):
        """
            Applies a mathematical function to the value using the bruteforce method to calculate the new uncertainty

            func (function) - The function to apply
        """
        # Apply function to the value
        val = func(self.value)
        # Apply the function to the value plus the uncertainty and then take away the new val
        unc = func(self.value + self.uncertainty) - val

        return Uncertainty(val, unc)

    def __str__(self):
        """String representation"""
        # Calculates the amount to round by for correct formatting
        rounding = -int(math.floor(math.log10(abs(self.uncertainty))))
        # Rounded values
        rounded_uncertainty = round(self.uncertainty, rounding)
        rounded_value = round(self.value, rounding)

        return(f"{rounded_value} ± {rounded_uncertainty}")

    def __add__(self, other):
        """
            Uncertainty addition

            other (int/float/Uncertainty) - Object to be added
        """
        # Check type of other
        if type(other) == Uncertainty:
            # Add values
            val = self.value + other.value
            # Add absolute uncertainties
            unc = self.abs_uncertainty() + other.abs_uncertainty()
        else: # Presume int or float
            # Add values
            val = self.value + other
            # Final uncertainty stays the same
            unc = self.abs_uncertainty()

        # Return Uncertainty
        return(Uncertainty(val, unc))

    def __radd__(self, other): 
        """Flipped uncertainty addition"""
        return(self + other) 

    def __sub__(self, other):
        """
            Uncertainty subtraction

            other (int/float/Uncertainty) - The object to subtract
        """
        # Check type of other
        if type(other) == Uncertainty:
            # Add values
            val = self.value - other.value
            # Add absolute uncertainties
            unc = self.abs_uncertainty() + other.abs_uncertainty()
        else: # Presume int or float
            # Add values
            val = self.value - other
            # Final uncertainty stays the same
            unc = self.abs_uncertainty()

        # Return Uncertainty
        return(Uncertainty(val, unc))

    def __rsub__(self, other): 
        """Flipped uncertainty subtraction"""
         # Check type of other
        if type(other) == Uncertainty:
            # Add values
            val = other.value - self.value
            # Add absolute uncertainties
            unc = self.abs_uncertainty() + other.abs_uncertainty()
        else: # Presume int or float
            # Add values
            val = other - self.value
            # Final uncertainty stays the same
            unc = self.abs_uncertainty()

        # Return Uncertainty
        return(Uncertainty(val, unc))

    def __mul__(self, other):
        """
            Uncertainty multiplication

            other (int/float/Uncertainty) - Uncertainty to multiply by
        """
        # Check type of other
        if type(other) == Uncertainty:
            # Get final value
            val = self.value * other.value
            # Add relative uncertainties and multiply the sum by final value
            unc = val * (self.rel_uncertainty() + other.rel_uncertainty())
        else: # Presume int or float
            # Get final value
            val = self.value * other
            # Multiply final by current relative uncertainty
            unc = val * self.rel_uncertainty()

        # Return Uncertainty
        return(Uncertainty(val, unc))

    def __rmul__(self, other): 
        """Flipped uncertainty multiplication"""
        return(self * other) 

    def __truediv__(self, other):
        """
            Uncertainty multiplication

            other (int/float/Uncertainty) - Object to divide by
        """
        # Check type of other
        if type(other) == Uncertainty:
            # Get final value
            val = self.value / other.value
            # Add relative uncertainties and multiply the sum by final value
            unc = val * (self.rel_uncertainty() + other.rel_uncertainty())
        else: # Presume int or float
            # Get final value
            val = self.value / other
            # Multiply final by current relative uncertainty
            unc = val * self.rel_uncertainty()

        # Return Uncertainty
        return(Uncertainty(val, unc))

    def __rtruediv__(self, other): 
        """Flipped uncertainty division"""
        # Check type of other
        if type(other) == Uncertainty:
            # Get final value
            val = other.value / self.value
            # Add relative uncertainties and multiply the sum by final value
            unc = val * (self.rel_uncertainty() + other.rel_uncertainty())
        else: # Presume int or float
            # Get final value
            val = other / self.value
            # Multiply final by current relative uncertainty
            unc = val * self.rel_uncertainty()

        # Return Uncertainty
        return(Uncertainty(val, unc))