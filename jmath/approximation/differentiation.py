'''
    Approximations of the results of differential equations.
'''

# - Imports

from typing import Callable, Dict, Tuple, List
from ..uncertainties import Uncertainty

# - Globals

LOCAL_MINIMUM = "Local Minimum"
LOCAL_MAXIMUM = "Local Maximum"
SADDLE = "Saddle"

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

        Notes
        -----

        Occasional accuracy issues for n > 1, investigation ongoing.
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

    # Output dictionary
    output = {}

    # Single partial derivatives
    f_x = lambda x1, y1: differentiate(lambda x2: f(x2, y1), x1)
    f_y = lambda x1, y1: differentiate(lambda y2: f(x1, y2), y1)
    # Second partial derivatives
    f_xx = lambda x1, y1: differentiate(lambda x2: f(x2, y1), x1, n = 2)
    f_yy = lambda x1, y1: differentiate(lambda y2: f(x1, y2), y1, n = 2)
    # Mixed second partial derivatives
    f_xy = lambda x1, _: differentiate(lambda y2: f_x(x1, y2), x1)
    f_yx = lambda _, y1: differentiate(lambda x2: f_y(x2, y1), y1)

    for point in crit_points:
        x, y = point
        # Assert equality of derivatives at critical points
        # Since SPT only works for f_xy == f_yx
        assert round(f_xy(x, y), 6) == round(f_yx(x, y), 6)

        # Calculate d
        d = round(f_xx(x, y) * f_yy(x, y) - f_xy(x, y) ** 2, 6)

        # Classify
        if d == 0:
            output[point] = None
        elif d < 0:
            output[point] = SADDLE
        else: # d > 0
            if f_xx(x, y).value > 0:
                output[point] = LOCAL_MINIMUM
            elif round(f_xx(x, y).value, 6) == 0:
                output[point] = None
            else: # f_xx < 0
                output[point] = LOCAL_MAXIMUM

    return output
