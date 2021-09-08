'''
    Vector Objects
'''

# - Imports

import math
from functools import wraps
from typing import List, Callable, Any, Union
from ..exceptions import VectorsNotSameSize
from .lines import Line
from .planes import Plane

# - Classes
class Vector:
    """
        n-dimensional Vectors

        Parameters
        ----------

        components
            Scalar vector components

        Examples
        --------

        >>> Vector(3, 2, 1) + Vector(2, 1, 1)
        Vector(5, 3, 2)

        >>> Vector(3, 1, 0) - Vector(9, 8, 8)
        Vector(-6, -7, -8)

        >>> 3 * Vector(1, 2, -4)
        Vector(3, 6, -12)
        >>> Vector(3, 6, 9)/3
        Vector(1, 2, 3)

        >>> Vector(10, 2, 1) @ Vector(1, 2, 3)
        17

        >>> Vector(1, 1).magnitude()
        2

    """
    def __init__(self, *components: List[float]):

        # If components[0] is list store that list
        if(type(components[0]) == list):
            self.components = components[0]
        else:
            # Else it's *args
            self.components = list(components)

    def __repr__(self) -> str:
        """Programming Representation"""
        return f"Vector{self.__str__()}"

    def __str__(self) -> str:
        """String representation"""
        string = "("
        for component in self.components:
            string += f"{component}, "
        string = string[:-2] + ")"
        return string

    def __getitem__(self, index: int) -> float:
        """Subscripting."""
        return self.components[index]

    def __same_size(func: Callable[["Vector", "Vector"], Any]) -> Callable[["Vector", "Vector"], Any]:
        """
            Wrapper that checks if vectors are the same size.

            Parameters
            ----------

            func
                Function to check

            Raises
            ------

            VectorsNotSameSize
                If the vectors are not the same size this error will be raised.
        """
        @wraps(func)
        def inner(*args, **kwargs):
            if len(args[0]) == len(args[1]):
                return func(*args, **kwargs)
            else:
                raise VectorsNotSameSize()

        return inner

    def __eq__(self, vector: "Vector") -> bool:
        """Tests equality of vectors"""
        if isinstance(vector, Vector) or isinstance(vector, Point):
            return vector.components == self.components
        else:
            return False

    @__same_size
    def __add__(self, vector: "Vector") -> "Vector":
        """Add vectors together"""

        # Add the foreign components to local components and return
        return Vector([i + j for i, j in zip(self.components, vector.components)])

    @__same_size
    def __sub__(self, vector: "Vector") -> "Vector":
        """Subtract vectors from each other"""
        
        # Subtract the foreign components from local components and return
        return Vector([i - j for i, j in zip(self.components, vector.components)])

    @__same_size
    def __matmul__(self, vector: "Vector") -> float:
        """The dot product of two vectors"""
        return sum([i * j for i, j in zip(self.components, vector.components)])

    def __mul__(self, scalar: float) -> "Vector":
        """Scalar multiplication"""

        new_components = [scalar * component for component in self.components]
        return Vector(new_components)

    def __rmul__(self, scalar: float) -> "Vector":
        """Reverse scalar multiplication"""
        return self * scalar

    def __truediv__(self, scalar: float) -> "Vector":
        """Scalar division"""
        return 1/scalar * self

    def __rtruediv__(self, scalar: float) -> "Vector":
        """Reverse scalar division"""
        return self * 1/scalar

    def __len__(self) -> int:
        """Amount of components in vector"""
        return len(self.components)

    def unit(self) -> "Vector":
        """Returns a unit vector in the same direction as the vector."""
        return self/self.magnitude()

    def negative(self) -> "Vector":
        """Returns a vector of the same magnitude pointing in the opposite direction."""
        neg_comp = [-component for component in self.components]
        return Vector(neg_comp)

    @__same_size
    def projection(self, vector: Union["Vector", "Line", "Plane"]) -> "Vector":
        """
            Returns projection of current vector onto the passed vector or line.

            Parameters
            ----------

            vector
                Vector or line to calculate the projection onto.

            Raises
            ------

            VectorsNotSameSize
                If the vectors are not the same size this error will be raised.
        """
        if isinstance(vector, Plane):
            plane = vector
            # Compute projections onto both vectors and add
            return self.projection(plane.vectors[0]) + self.projection(plane.vectors[1])
        else:
            # Not plane, check for line
            if isinstance(vector, Line):
                vector = vector.vector
            # Compute projection
            return (self @ vector)/(vector @ vector) * vector

    def magnitude(self) -> float:
        """Calculates the vector magnitude."""
        # Store magnitude while computing
        magnitude = 0

        # For every vector component
        for c in self.components:
            # Pythagorean theorom
            # hypotenuse = sqrt(a**2 + b**2)
            magnitude = math.sqrt(magnitude ** 2 + c ** 2)

        return(magnitude)

    @__same_size
    def angle_between(self, vector: "Vector") -> float:
        """
            Determines the angle (in radians) between two vectors to 5 d.p.

            Parameters
            ----------

            vector
                Vector or line to calculate angle between.

            Raises
            ------

            VectorsNotSameSize
                If the vectors are not the same size this error will be raised.
        """

        if isinstance(vector, Line):
            vector = vector.vector

        return round(math.acos((self @ vector)/(self.magnitude() * vector.magnitude())), 5)

class Point(Vector):
    """
        Points based on vector framework. Can be thought of as a vector from origin.

        Parameters
        ----------

        components
            Coordinates in n-space
    """
    def __init__(self, *components: List[float]):
        return super().__init__(*components)
    
    def on_line(self, line: "Line") -> bool:
        """
            Determines whether a point is on a line, returns bool.

            Parameters
            ----------

            line
                Line to determine if on
        """
        results = []
        # For every component in both
        for i in range(len(self)):
            scalor = (self.components[i] - line.point.components[i])/line.vector.components[i]
            results.append(round(scalor, 3))
        # Go through results, if any don't match, return false
        return all(result == results[0] for result in results)