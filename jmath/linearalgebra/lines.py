'''
    Line defined by vectors and point.
'''

# - Imports

from ..exceptions import VectorsNotSameSize
from typing import TypeVar

# - Globals

# Typing for Vectors and Points
Point = TypeVar("Point")
Vector = TypeVar("Vector")

# - Classes

class Line:
    """
        Defines a line from direction and point vectors.

        Parameters
        ----------

        point
            Position vector for line.
        vector
            Direction vector for line.
    """
    def __init__(self, point: Point, vector: Vector):

        self.point = point
        self.vector = vector

        if len(self.point) != len(self.vector):
            raise VectorsNotSameSize()

    def __len__(self) -> int:
        """Returns size of direction vector"""
        return len(self.vector.components)