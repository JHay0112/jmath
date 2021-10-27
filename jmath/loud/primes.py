'''
    Loud implementations of prime functions.
'''

# - Imports

from math import sqrt, ceil
from .modular import gcd

# - Functions

def primality(n: int):
    '''
        Check that a number is prime.

        Parameters
        ----------

        n
            The number to check if it is prime
    '''

    sqrt_n = ceil(sqrt(n))

    print(f"The greatest number we need to check is {sqrt_n}\n")

    for i in range(2, sqrt_n + 1):

        if n % i == 0:
            print(f"\n{i}|{n} implies {n} is not prime")
            return False
        else:
            print(f"{i} does not divide {n}")

    else:
        print(f"\nThus, {n} is prime")
        return True

def relative_primality(a: int, b: int):
    '''
        Check that a number is relatively prime to another number

        Parameters
        ----------

        a
            The number to check the relative primality of
        b
            The number to check the relative primality with respect to
    '''

    if gcd(a, b) == 1:
        print(f"Thus {a} is relatively prime with respect to {b}.")
        return True
    else:
        print(f"Thus {a} is NOT relatively prime with respect to {b}.")
        return False