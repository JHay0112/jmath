'''
    Tools for modular arithmetic
'''

# - Imports

from typing import Tuple, Optional

# - Functions

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
        Recursive extended euclidean algorithm to find the greatest common denominator and its linear combination
        Returns g, m, n such that gcd(a, b) = g = m*a + n*b
        
        Parameters
        ----------
        
        a
            Number to find the greatest common denominator of with b
        b
            Number to find the greatest common denominator of with a
    """
    if a == 0:
        # Trivial case
        return (b, 0, 1)
    else:
        # Call self with a and b % a since this is equivalent as per euclidean algorithm
        g, m, n = extended_gcd(b % a, a)
        # Return gcd, n, and m
        return (g, n - (b // a)*m, m)

def modular_inverse(a: int, set_size: int) -> Optional[int]:
    """
        Finds the modular inverse of a number in a set.

        Parameters
        ----------

        a
            The number to find the modular inverse of
        set_size
            The size of the set to find the inverse in
    """
    g, m, _ = extended_gcd(a, set_size)

    if g != 1:
        # Not relatively prime, not invertible
        return None
    else:
        # Relatively prime, find m inside the set
        return m % set_size