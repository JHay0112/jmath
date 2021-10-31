'''
    Approximations of the results of differential equations.
'''

# - Imports

from typing import Callable, Dict, Tuple, List
from ..uncertainties import Uncertainty

# - Functions

def differentiate(f: Callable[[float], float], x: float, h: float = 1e-6, n: int = 1) -> Uncertainty:
    """
        Numerically differentiate the given function at a point x.
        Uses the symmetric difference quotient to approximate.
        Recurses for n-th derivative.

        Parameters
        ----------

        f
            The function to numerically differentiate.
        x
            The point at which to differentiate at.
        h
            The change in x to approximate with.
        n
            Order of derivative.
    """

    if n > 1:
        return differentiate(lambda x: (f(x + h) - f(x - h))/(2*h), x, h, n - 1)
    else:
        return Uncertainty((f(x + h) - f(x - h))/(2*h), h ** 2)

def second_partials_test(f: Callable[[float, float], float], crit_points: List[Tuple[float, float]]) -> Dict[Tuple[float, float], str]:
    """
        Second Partials Test.
        Classifies the critical points of a function of two variables.


        Parameters
        ----------

        f
            The function to classify the critical points of.
        crit_points
            The critical points of the function.
        
        Returns
        -------

        A dictionary mapping critical point tuples to descriptions of the points.
    """

    f_xx = lambda x, y: differentiate(lambda x: f(x, y), x, n = 2)
    f_yy = lambda x, y: differentiate(lambda y: f(x, y), y, n = 2)

    