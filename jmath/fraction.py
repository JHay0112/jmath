'''
    jmath/fraction.py

    Fractions, because sometimes floats are gross

    Author: Jordan Hay
    Date: 2021-07-01
'''

# - Imports

from . import exceptions

# - Classes

class Fraction:
    """
        Fraction

        numerator (int) - Fraction numerator (top bit)
        denominator (int) - Fraction denominator (bottom bit)

        Author: Jordan Hay
        Date: 2021-07-01
    """
    def __init__(self, numerator, denominator):
        
        self.numerator = numerator
        self.denominator = denominator
        # Check that denominator is not zero
        self.check_denominator()

    def check_denominator(self):
        """Checks that denominator is not zero"""
        if self.denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

    def simplify(self):
        """Simplify the fraction"""
        if isinstance(self.numerator/self.denominator, int):
            # If division of the numerator by the denominator can be done wholly
            self.numerator = self.numerator/self.denominator
            self.denominator = 1
        elif self.denominator % self.numerator == 0:
            # Try divide the denominator by the numerator wholly
            self.denominator = self.denominator/self.numerator
            self.numerator = 1

    def flip(self):
        """Returns a flipped version of the fraction"""
        return Fraction(self.denominator, self.numerator)

    def evaluate(self):
        """Returns an evaluated form"""
        return self.numerator/self.denominator

    def __mul__(self, other):
        """
            Multiply fractions

            other (int/Fraction) - Object to multiply by
        """
        if isinstance(other, Fraction):
            # Fractions
            new_num = self.numerator * other.numerator
            new_den = self.denominator * other.denominator
            new_frac = Fraction(new_num, new_den)
            return new_frac
        elif isinstance(other, int):
            # Integers
            new_num = self.numerator * other
            new_frac = Fraction(new_num, self.denominator)
            return new_frac
        else:
            raise exceptions.InvalidFractionOperation(f"{type(other)} cannot be used to multiply a fraction.")

    def __rmul__(self, other):
        """Reversed multiplication"""
        return self * other

    def __truediv__(self, other):
        """
            Divide fractions

            other (int/Fraction) - Object to divide by
        """
        if isinstance(other, Fraction):
            # Fractions
            return self * other.flip()
        elif isinstance(other, int):
            # Integers
            return self * Fraction(1, other)
        else:
            raise exceptions.InvalidFractionOperation(f"{type(other)} cannot be used to divide a fraction.")

    def __add__(self, other):
        """
            Add fractions

            other (int/Fraction) - Object to add
        """
        if isinstance(other, Fraction):
            # Fractions
            # Multiply both denominators by the other
            new_den = self.denominator * other.denominator
            new_num = self.numerator * other.denominator + other.numerator * self.denominator
            return Fraction(new_num, new_den)
        elif isinstance(other, int):
            # Add an ints worth of denominator to numerator
            new_num = self.numerator + other * self.denominator
            return Fraction(new_num, self.denominator)
        else:
            raise exceptions.InvalidFractionOperation(f"{type(other)} cannot be added to a fraction.")

    def __radd__(self, other):
        """Reversed addition"""
        return self + other

    def __sub__(self, other):
        """
            Subtract fractions

            other (int/Fraction) - Object to subtract
        """
        if isinstance(other, Fraction):
            # Fractions
            # Make other negative
            new_num = -other.numerator
            # Add them
            return self + Fraction(new_num, other.denominator)
        elif isinstance(other, int):
            # Integers
            # Make other negative
            new_int = -other
            return self + new_int
        else:
            raise exceptions.InvalidFractionOperation(f"{type(other)} cannot be subtracted from a fraction.")

    def __rsub__(self, other):
        """Reversed fraction subtraction"""
        return self - other