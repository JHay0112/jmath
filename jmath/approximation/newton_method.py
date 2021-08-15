"""
    Newton's method for approximating the roots of equations.
"""

# - Imports

from ..uncertainties import Uncertainty
from typing import Callable
from warnings import warn

# - Functions

def newton_step(f: Callable[[float], float], f_prime: Callable[[float], float], x_0: float) -> float:
    """
        Performs a single iteration of Newton's Method

        Parameters
        ----------

        f
            The function to determine the root of.
        f_prime
            The derivative of the function to determine the root of.
        x_0
            The starting point for determining the root from.
    """

    return x_0 - f(x_0)/f_prime(x_0)

def newton_method(f: Callable[[float], float], f_prime: Callable[[float], float], x_0: float, threshold: float = 0.5e-6, max_iter: int = 100) -> Uncertainty:
    """
        Newton's Method for approximation of the root of an equation.

        Parameters
        ----------

        f
            The function to determine the root of.
        f_prime
            The derivative of the function to determine the root of.
        x_0
            The starting point for determining the root from.
        threshold
            The threshold error to approximate the root to.
        max_iter
            The maximum iterations to apply.
    """

    # Instantiate x_n from x_0
    x_n = x_0
    # Error calculator
    error = lambda: abs(f(x_n))
    # Iterator counter
    i = 0

    # While the distance between points is greater than the threshold
    while error() >= threshold:

        # Compute new x_n
        x_n = newton_step(f, f_prime, x_n)

        # If iterator is too high
        if i >= max_iter:
            # Warn user
            warn(f"Newton Method reached max iterations of {max_iter}.")
            # Return value of x_n
            return(Uncertainty(x_n, threshold))

        # Increase iterator
        i += 1

    # Error under threshold
    # Return value
    return(Uncertainty(x_n, threshold))

def newton_sqrt(n: float) -> Uncertainty:
    """
        Uses Newton's Method to compute square roots.

        Parameters
        ----------
        
        n
            The number to approximate the square root of.
    """
    f = lambda x : x**2 - n
    f_prime = lambda x : 2*x
    return newton_method(f, f_prime, n)