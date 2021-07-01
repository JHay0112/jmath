'''
    jmath/fraction.py

    Fractions, because sometimes floats are gross

    Author: Jordan Hay
    Date: 2021-07-01
'''

# - Imports

import exceptions

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
        """"""
        pass

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
            new_frac.simplify()
            return new_frac
        elif isinstance(other, int):
            # Integers
            new_num = self.numerator * other
            new_frac = Fraction(new_num, self.denominator)
            return new_frac
        else:
            raise exceptions.InvalidFractionOperation(f"{type(other)} cannot be used to multiply a fraction")

    def __rmul__(self, other):
        """Reversed multiplication"""
        return self * other