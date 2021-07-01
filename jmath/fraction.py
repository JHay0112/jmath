'''
    jmath/fraction.py

    Fractions, because sometimes floats are gross

    Author: Jordan Hay
    Date: 2021-07-01
'''

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