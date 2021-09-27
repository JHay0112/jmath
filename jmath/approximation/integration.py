'''
    Approximations of definite integrals
'''

# - Imports

from typing import Callable, Generator

# - Functions

def partition(f: Callable[[float], float], start: float, end: float, divisions: int) -> Generator[float, None, None]:
    '''
        Partitions a function, returning the start and end points of each partition

        Parameters
        ----------

        f
            The function to partition
        start
            Lower limit
        end
            Upper limit
        divisions
            Amount of divisions to cut the function into
    '''
    # Start at the start
    current_position = start
    # Amount to move up per cycle
    delta = (end - start)/divisions

    while current_position < end:

        yield (f(current_position), f(current_position + delta))

        current_position += delta

def left_hand_rule(f: Callable[[float], float], start: float, end: float, divisions: int):
    '''
        Approximates area under curve with the left hand rule.

        Parameters
        ----------

        f
            The function to approximate the area under
        start
            The lower limit of the definite integral.
        end
            The upper limit of the definite integral.
        divisions
            The amount of divisions to use.
    '''

    signed_area = 0
    delta_x = (end - start)/divisions

    # For every partition
    for left, _ in partition(f, start, end, divisions):
        # Calculate the area of a rectangle from the left side of the partition
        signed_area += left

    return signed_area * delta_x