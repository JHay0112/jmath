'''
    Complex form of points.
'''

# - Imports

from .linearalgebra import Point
import math
from typing import Union

# - Classes

class Complex(Point):
    """
        Complex numbers based on vectors.

        Parameters
        ----------

        real
            Real component of a complex number
        imaginary
            Imaginary component of a complex number
    """

    def __init__(self, real: float, imaginary: float):
        
        super().__init__(real, imaginary)

    def __repr__(self) -> str:
        """Programming Representation"""
        return f"ComplexNumber({self.real}, {self.imaginary})"

    def __str__(self) -> str:
        """String representation"""
        operand = ""
        if self.imaginary >= 0:
            operand = "+"
        return f"{self.real()} {operand} {self.imaginary()}j"

    def real(self):
        """Returns the real component of the complex number."""
        return self.components[0]

    def imaginary(self):
        """Returns the imaginary component of the complex number."""
        return self.components[1]

    def quadrant(self) -> Union[int, None]:
        """Returns which quadrant the number is in. Returns None if on a quadrant border."""
        if self.real() > 0 and self.imaginary() > 0:
            # Both greater than zero
            # Quadrant 2
            return 1
        elif self.real() < 0 and self.imaginary() > 0:
            # Real is less than zero and imaginary greater than
            # Quadrant 2
            return 2
        elif self.real() < 0 and self.imaginary() < 0:
            # Real and imaginary less than zero
            # Quadrant 3
            return 3
        elif self.real() > 0 and self.imaginary() < 0:
            # Real greater than zero but imaginary negative
            # Quadrant 4
            return 4
        else:
            # On a border
            return None

    def argument(self) -> float:
        """Computes the argument of the complex number in radians."""
        theta = math.atan(self.imaginary()/self.real())
        # Check quadrant
        if self.quadrant() == 2:
            # If in the second quadrant
            # Add pi
            theta += math.pi
        elif self.quadrant() == 3:
            # If in third quadrant
            # Subtract pi
            theta -= math.pi

        return theta

    def modulus(self) -> float:
        """Rename of magnitude."""
        return self.magnitude()