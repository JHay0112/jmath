'''
    Loud implementation of modular functions
'''

# - Imports

from typing import Optional

# - Functions

def gcd(a: int, b: int, i: int = 1) -> int:
    '''
        Loud recursive implementation of the Euclidean Algorithm

        Parameters
        ----------

        a
            A number to find the gcd of with b
        b
            A number to find the gcd of with a
        i 
            Number of iterations of algorithm, default is 1
    '''

    if b > a:
        # Always keep b smaller than a
        a, b = b, a

    # Calculate remainder
    r = a % b
    # Quotient
    q = a // b

    print(f"({i}): {a} = {q}*{b} + {r}")

    if r == 0:
        # Base case
        print(f"\n({i}) implies the gcd is {b}")
        return b
    else:
        # Euclidean step
        # gcd(a, b) == gcd(b, r)
        return gcd(b, r, i + 1)

def modular_inverse_brute_force(a: int, b: int) -> Optional[int]:
    '''
        Brute force modular inverse finder

        Parameters
        ----------

        a
            The number to find the modular inverse of
        b
            The size of the modular set to find the inverse in

        Returns
        -------

        If a modular inverse is found it returns the modular inverse, else it returns None
    '''

    # Base cases
    if a == 1:
        print(f"1 is always its own inverse")
        return 1
    elif a == (b - 1):
        print(f"{b - 1} is always its own inverse in {b}")
        return a
    else:
        # None of the easy cases so brute force it
        for i in range(2, b - 1):
            if (a * i) % b == 1:
                print(f"\n{i} is the modular inverse of {a} in {b}")
                return i
            else:
                 print(f"{a} * {i} mod {b} = {(a * i) % b}")
        else:
            # None found, return None
            print(f"\nOptions exhausted, {a} has no modular inverse in {b}")
            return None
