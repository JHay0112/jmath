'''
    Plane defined by vectors and point.
'''

# - Imports

from ..exceptions import VectorsNotSameSize
from typing import TypeVar

# - Globals

# Typing for Vectors and Points
Point = TypeVar("Point")
Vector = TypeVar("Vector")

class Plane:
    """
        Defines a plane 

        Parameters
        ----------

        point
            Point on the plane.
        vector1
            Direction vector.
        vector2
            Direction vector.

        Raises
        ------

        VectorsNotSameSize
            If the vectors are not the same size this error will be raised.
    """
    def __init__(self, point: Point, vector1: Vector, vector2: Vector):
        
        self.point = point
        self.vectors = [vector1, vector2]

        # Throw error if vectors different sizes
        if len(point) != len(vector1) != len(vector2):
            raise VectorsNotSameSize()

    def __len__(self):
        # Size of point vector
        return len(self.point)