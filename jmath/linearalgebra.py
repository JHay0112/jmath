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

# -- Vector
# Author: Jordan Hay
# Date: 2020-11-02
# A vector with n dimensions
class Vector:

    # --- __init__()
    # Initialise Vector object
    #
    # self
    # *components (List/*args) - Scalar vector components, e.g. x, y, z
    def __init__(self, *components):

        # If components[0] is list store that list
        if(type(components[0]) == list):
            self._components = components[0]
        else:
            # Else it's *args
            self._components = components

    # --- __add__()
    # Add another Vector object to this Vector
    #
    # self
    # vector (Vector) - The foreign Vector to add
    def __add__(self, vector):

        # Add the foreign components to local components and return
        return(Vector(list(map(operator.add, self._components, vector.components()))))

    # --- __sub__()
    # Subtract another Vector object from this vector
    #
    # self
    # vector (Vector) - The foreign Vector to subtract
    def __sub__(self, vector):

        # Subtract the foreign components from local components and return
        return(Vector(list(map(operator.sub, self._components, vector.components()))))

    # --- components()
    # Returns the components of the vector
    #
    # self
    def components(self):

        return(self._components)

    # --- magnitude()
    # Returns the magnitude of the vector as calculated from the components
    #
    # self
    def magnitude(self):

        # Store magnitude while computing
        magnitude = 0

        # For every vector component
        for c in self._components:
            # Pythagorean theorom
            # hypotenuse = sqrt(a**2 + b**2)
            magnitude = math.sqrt(magnitude ** 2 + c ** 2)

        return(magnitude)

    # --- draw()
    # Draws a 2D arrow
    #
    # self
    # x (int) - The dimension to plot on the x-axis
    # y (int) - The dimension to plot on the y-axis
    def draw(self, x = 0, y = 1):

        ax = plt.axes()
        ax.arrow(0, 0, self._components[x], self._components[y], head_width=0.05, head_length=0.05)
        plt.show()