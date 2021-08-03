"""
    Newton's method for approximating the roots of equations.
"""

# - Imports

from ..uncertainties import Uncertainty
from typing import Callable
from warnings import warn

# - Functions

def newton_method(f: Callable[[float], float], f_prime: Callable[[float], float], x_0: float, threshold: float = 0.5e-6, max_iter: int = 100) -> float:
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
    # Create a placeholder new x such that the threshold is not triggered
    x_new = x_n + 2*threshold 
    # Iterator counter
    i = 0

    # While the distance between points is greater than the threshold
    while abs(f(x_new) - f(x_n)) >= threshold:

        x_new = x_n
        # Compute new x_n
        x_n = x_n - f(x_n)/f_prime(x_n)

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

def newton_sqrt(n: float) -> float:
    """
        Uses Newton's Method to compute square roots.

        Parameters
        ----------
        
        n
            The number to approximate the square root of.
    """
    f = lambda x : x**2 - n
    f_prime = lambda x : n*x
    return newton_method(f, f_prime, n)