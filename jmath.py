'''
    jmath.py

    Author: Jordan Hay
    Date: 2020-11-02
    Version: 0.4.4

    Jordan's Math Module

    Creating my own maths tools in Python as a challenge.
'''

# - Modules

import math # Mathematical functions, e.g. sqrt()
import operator # Python operators

# - Classes

# -- Vector
# Author: Jordan Hay
# Date: 2020-11-02
# Version: 0.4.2
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
        return(Vector(list(map(operator.add, self._components, vector.get_components()))))

    # --- __sub__()
    # Subtract another Vector object from this vector
    #
    # self
    # vector (Vector) - The foreign Vector to subtract
    def __sub__(self, vector):

        # Subtract the foreign components from local components and return
        return(Vector(list(map(operator.sub, self._components, vector.get_components()))))

    # --- get_components()
    # Returns the components of the vector
    #
    # self
    def get_components(self):

        return(self._components)

    # --- get_magnitude()
    # Returns the magnitude of the vector as calculated from the components
    #
    # self
    def get_magnitude(self):

        # Store magnitude while computing
        magnitude = 0

        # For every vector component
        for c in self._components:
            # Pythagorean theorom
            # hypotenuse = sqrt(a**2 + b**2)
            magnitude = math.sqrt(magnitude ** 2 + c ** 2)

        return(magnitude)

# -- PhysEnv
# Author: Jordan Hay
# Date: 2020-11-08
# Version: 0.0.2
# Physical Environment
class PhysEnv:

    # --- __init___()
    # Initialise the Physics Environment
    #
    # self
    def __init__(self):

        # Initialise empty list of PhysObj's
        self._objects = []
        # Set time to zero
        self._time = 0

    # --- get_time()
    # Returns time
    #
    # self
    def get_time(self):

        return(self._time)

    # --- increment_time()
    # Increment the time by an amount
    #
    # self
    # increment (Float) - The amount to increase the time by
    def increment_time(self, increment):

        self._time += increment

    # --- add_object()
    # Add PhysObj to list
    #
    # self
    # new_obj (PhysObj) - The object to add
    def add_object(self, new_obj):

        self._objects.append(new_obj)

# -- PhysObj
# Author: Jordan Hay
# Date: 2020-11-06
# Version: 0.0.1
# Physical Object
class PhysObj:

    # --- __init__()
    # Initialise the PhysObj Object
    #
    # self
    # env (PhysEnv) - The environment the object exists in
    # init_vel (Vector) - An initial velocity vector
    # mass (Int) - The mass of the object
    def __init__(self, env, init_vel = Vector(0, 0, 0), mass = 1):

        # Assign object variables
        self._env = env
        self._init_vel = init_vel
        self._mass = mass

        # Add self to list in PhysEnv
        self._env.add_object(self)

# - Main

# Used for testing components as I develop them
if(__name__ == "__main__"):

    v = Vector(2, 3, 10)
    fv = Vector(1, 2, 3)

    v += fv
    v -= fv

    print(v.get_components())