'''
    jmath/linearalgebra.py

    Author: Jordan Hay
    Date: 2021-06-17

    Vectors
'''

# - Modules

import matplotlib.pyplot as plt # Visualisation
import operator # Python operators
import math # Mathematical functions, e.g. sqrt()

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

    def __add__(self, vector):
        """
            Add vectors together

            vector (Vector) - Vector to add
        """

        # Add the foreign components to local components and return
        return(Vector(list(map(operator.add, self.components, vector.components))))

    def __sub__(self, vector):
        """
            Subtract vectors from each other

            vector (Vector) - Vector to subtract
        """
        # Subtract the foreign components from local components and return
        return(Vector(list(map(operator.sub, self.components, vector.components))))

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