'''
    Approximations of the results of differential equations.
'''

# - Imports

from typing import Callable
from ..uncertainties import Uncertainty

# - Functions

def differentiate(f: Callable[[float], float], x: float, h: float = 1e-6) -> Uncertainty:
    """
        Numerically differentiate the given function at a point x.
        Uses the symmetric difference quotient to approximate.

        Parameters
        ----------

        f
            The function to numerically differentiate.
        x
            The point at which to differentiate at.
        h
            The change in x to approximate with.
    """

    derivative = (f(x + h) - f(x- h))/(2*h)

    return Uncertainty(derivative, h ** 2)

