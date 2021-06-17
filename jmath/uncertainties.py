'''
    jmath/uncertainties.py

    Author: Jordan Hay
    Date: 2021-06-17

    For dealing with values and their associated uncertainties
'''

# - Modules

import math

# - Classes

# -- Uncertainty
# Author: Jordan Hay
# Date: 2021-03-17
# A value with an associated uncertainty
class Uncertainty:

    # --- __init__()
    # Initialise the uncertainty
    #
    # self
    # value (float) - The absolute value
    # uncertainty - The absolute uncertainty
    def __init__(self, value, uncertainty):

        self._value = value
        self._uncertainty = uncertainty

    # --- value()
    # Return the value
    #
    # self
    def value(self): return self._value

    # --- abs_uncertainty()
    # Return the absolute uncertainty of the object
    #
    # self
    def abs_uncertainty(self): return(self._uncertainty)

    # --- rel_uncertainty()
    # Return the relative uncertainty (0 to 1)
    #
    # self
    def rel_uncertainty(self): return(self._uncertainty/self._value)

    # --- __str__()
    # Representation of self
    #
    # self
    def __str__(self):

        # Calculates the amount to round by for correct formatting
        rounding = -int(math.floor(math.log10(abs(self._uncertainty))))
        # Rounded values
        rounded_uncertainty = round(self._uncertainty, rounding)
        rounded_value = round(self._value, rounding)

        return(f"{rounded_value} ± {rounded_uncertainty}")

    # --- __add__()
    # Define what happens when an uncertainty is added
    #
    # self
    # other (int/float/Uncertainty) - The other object to add
    def __add__(self, other):

        # Check type of other
        if type(other) == Uncertainty:
            # Add values
            val = self.value() + other.value()
            # Add absolute uncertainties
            unc = self.abs_uncertainty() + other.abs_uncertainty()
        else: # Presume int or float
            # Add values
            val = self.value() + other
            # Final uncertainty stays the same
            unc = self.abs_uncertainty()

        # Return Uncertainty
        return(Uncertainty(val, unc))

    # --- __radd__()
    # Define flipped addition
    #
    # self
    def __radd__(self, other): return(self + other) 

    # --- __sub__()
    # Define subtraction
    #
    # self
    # other (int/float/Uncertainty) - The object to subtract
    def __sub__(self, other):

        # Check type of other
        if type(other) == Uncertainty:
            # Add values
            val = self.value() - other.value()
            # Add absolute uncertainties
            unc = self.abs_uncertainty() + other.abs_uncertainty()
        else: # Presume int or float
            # Add values
            val = self.value() - other
            # Final uncertainty stays the same
            unc = self.abs_uncertainty()

        # Return Uncertainty
        return(Uncertainty(val, unc))

    # --- __rsub__()
    # Define flipped subtraction
    #
    # self
    # other
    def __rsub__(self, other): 

         # Check type of other
        if type(other) == Uncertainty:
            # Add values
            val = other.value() - self.value()
            # Add absolute uncertainties
            unc = self.abs_uncertainty() + other.abs_uncertainty()
        else: # Presume int or float
            # Add values
            val = other - self.value()
            # Final uncertainty stays the same
            unc = self.abs_uncertainty()

        # Return Uncertainty
        return(Uncertainty(val, unc))

    # --- __mul__()
    # Define multiplication
    #
    # self
    # other
    def __mul__(self, other):

        # Check type of other
        if type(other) == Uncertainty:
            # Get final value
            val = self.value() * other.value()
            # Add relative uncertainties and multiply the sum by final value
            unc = val * (self.rel_uncertainty() + other.rel_uncertainty())
        else: # Presume int or float
            # Get final value
            val = self.value() * other
            # Multiply final by current relative uncertainty
            unc = val * self.rel_uncertainty()

        # Return Uncertainty
        return(Uncertainty(val, unc))

    # --- __rmul__()
    # Define flipped multiplication
    #
    # self
    # other
    def __rmul__(self, other): return(self * other) 

    # --- __truediv__()
    # Define division
    #
    # self
    # other
    def __truediv__(self, other):

        # Check type of other
        if type(other) == Uncertainty:
            # Get final value
            val = self.value() / other.value()
            # Add relative uncertainties and multiply the sum by final value
            unc = val * (self.rel_uncertainty() + other.rel_uncertainty())
        else: # Presume int or float
            # Get final value
            val = self.value() / other
            # Multiply final by current relative uncertainty
            unc = val * self.rel_uncertainty()

        # Return Uncertainty
        return(Uncertainty(val, unc))

    # --- __rtruediv__()
    # Define flipped division
    #
    # self
    # other
    def __rtruediv__(self, other): 

        # Check type of other
        if type(other) == Uncertainty:
            # Get final value
            val = other.value() / self.value()
            # Add relative uncertainties and multiply the sum by final value
            unc = val * (self.rel_uncertainty() + other.rel_uncertainty())
        else: # Presume int or float
            # Get final value
            val = other / self.value()
            # Multiply final by current relative uncertainty
            unc = val * self.rel_uncertainty()

        # Return Uncertainty
        return(Uncertainty(val, unc))