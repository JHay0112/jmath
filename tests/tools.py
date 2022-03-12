'''
    Tools for generating tests.
'''

# - Imports

from random import randint, choice
from typing import List
from functools import wraps

# - Functions

def repeat(func):
    """
        Wrapper that repeats a function 100 times.
    """
    @wraps(func)
    def inner():
        for i in range(100):
            return func()

    return inner

def random_integer(min: int = -100, max: int = 100, non_zero = False) -> int:
    """
        Generates a random integer. Wrapper of random.randint.

        Parameters
        ----------

        min
            The minimum value int to produce.
        max
            The maximum value int to produce.
    """
    r = 0
    while r == 0:
        r = randint(min, max)
        if not non_zero:
            break
    return r

def random_integers(length: int):
    """
        Returns a random value list of set size.

        Parameters
        ----------

        length
            The length of the list to generate
    """
    return [random_integer() for i in range(length)]

def random_list(min: int = 3, max: int = 30) -> List[int]:
    """
        Generates a random length list of random integers.

        Parameters
        ----------

        min
            The minimum length of the list.
        max
            The maximum length of the list.    
    """
    
    length = random_integer(min, max)

    return random_integers(length)

def plus_or_minus() -> int:
    """Returns either 1 or -1"""
    return choice([1, -1])
