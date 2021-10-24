'''
    Loud implementations of prime functions.
'''

# - Imports

from math import sqrt, ceil

# - Functions

def primality_check(n: int):
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
            break
        else:
            print(f"{i} does not divide {n}")

    else:
        print(f"\nThus, {n} is prime")
