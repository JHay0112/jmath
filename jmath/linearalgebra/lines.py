'''
    Line defined by vectors and point.
'''

# - Imports

from . import Vector, Point
from ..exceptions import VectorsNotSameSize

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

        if self.point == None:
            self.point = Point([0 for i in self.vector.components])

        if len(self.point) != len(self.vector):
            raise VectorsNotSameSize()

    def __len__(self) -> int:
        """Returns size of direction vector"""
        return len(self.vector.components)