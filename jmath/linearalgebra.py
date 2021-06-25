'''
    jmath/linearalgebra.py

    Author: Jordan Hay
    Date: 2021-06-17

    Vectors
'''

# - Components

from . import exceptions

# - Modules

import matplotlib.pyplot as plt # Visualisation
import operator # Python operators
import math # Mathematical functions, e.g. sqrt()
from functools import wraps

# - Classes
class Vector:

    def __init__(self, *components):
        """
            n-dimensional Vectors

            *components (floats) - Scalar vector components

            Author: Jordan Hay
            Date: 2020-11-02
        """

        # If components[0] is list store that list
        if(type(components[0]) == list):
            self.components = components[0]
        else:
            # Else it's *args
            self.components = components

    def __str__(self):
        """String representation"""
        string = "("
        for component in self.components:
            string += f"{component}, "
        string = string[:-2] + ")"
        return string

    def same_size(func):
        """
            Wrapper that checks if vectors are the same size

            func (function) - Function to check
        """
        @wraps(func)

        def inner(*args, **kwargs):
            if len(args[0]) == len(args[1]):
                return func(*args, **kwargs)
            else:
                raise exceptions.VectorsNotSameSize()

        return inner

    @same_size
    def __add__(self, vector):
        """
            Add vectors together

            vector (Vector) - Vector to add
        """

        # Add the foreign components to local components and return
        return(Vector(list(map(operator.add, self.components, vector.components))))

    @same_size
    def __sub__(self, vector):
        """
            Subtract vectors from each other

            vector (Vector) - Vector to subtract
        """
        # Subtract the foreign components from local components and return
        return(Vector(list(map(operator.sub, self.components, vector.components))))

    @same_size
    def __matmul__(self, vector):
        """
            The dot product of two vectors

            vector (Vector) - Vector to dot with
        """
        dot = 0
        for i in range(len(self.components)):
            dot += self.components[i] * vector.components[i]
        return dot

    def __mul__(self, scalar):
        """
            Scalar multiplication

            scalar (float) - Scalar amount to multiply by
        """

        new_components = [scalar * component for component in self.components]
        return Vector(new_components)

    def __rmul__(self, scalar):
        """Reverse scalar multiplication"""
        return self * scalar

    def __len__(self):
        """Amount of components in vector"""
        return len(self.components)

    @same_size
    def projection(self, vector):
        """
            Returns projection of current vector onto passed vector

            vector (Vector/Line) - Vector or line to calculate the projection onto
        """
        if isinstance(vector, Line):
            vector = vector.vector

        return (self @ vector)/(vector @ vector) * vector

    def magnitude(self):
        """Calculates the vector magnitude"""
        # Store magnitude while computing
        magnitude = 0

        # For every vector component
        for c in self.components:
            # Pythagorean theorom
            # hypotenuse = sqrt(a**2 + b**2)
            magnitude = math.sqrt(magnitude ** 2 + c ** 2)

        return(magnitude)

    def draw(self, x = 0, y = 1):
        """
            Draws a 2D vector with matplot lib

            x (int) - Index of component to plot on the x-axis
            y (int) - Index of component to plot on the y-axis
        """
        ax = plt.axes()
        ax.arrow(0, 0, self.components[x], self.components[y], head_width=0.05, head_length=0.05)
        plt.show()

class Line:

    def __init__(self, vector):
        """
            Defines a line from a vector

            vector (Vector) - Direction vector for line

            Author: Jordan Hay
            Date: 2021-06-24
        """
        self.vector = vector

    def point_on_line(self, point):
        """
            Determines whether a point is on a line

            point (Vector) - Point to determine if on line
        """

        

class Plane:

    def __init__(self, point, vector1, vector2):
        """
            Defines a plane 

            point (Vector) - Point on the plane
            vector1 (Vector) - Direction vector
            vector 2 (Vector) - Direction vector

            Author: Jordan Hay
            Date: 2021-06-24
        """
        self.point = point
        self.vectors = [vector1, vector2]