'''
    jmath/physics/mechanics.py

    Author: Jordan Hay
    Date: 2021-06-17

    Tools for mechanical systems
'''

# - Modules

from ..linearalgebra import Vector

# - Classes

# -- PhysEnv
# Author: Jordan Hay
# Date: 2020-11-08
# Version: 0.1.0
# Physical Environment
class PhysEnv:

    # --- __init___()
    # Initialise the Physics Environment
    #
    # self
    # *forces (Vectors) - The forces that exist within the physics environment, e.g. Gravity
    def __init__(self, *forces):

        # Store forces *args
        self._forces = forces
        # Initialise empty list of PhysObj's
        self._objects = []
        # Set time to zero
        self._time = 0

    # --- time()
    # Returns time
    #
    # self
    def time(self):

        return(self._time)

    # --- forces_vector()
    # The Vector object that represents all the forces present in the systems
    #
    # self
    def forces_vector(self):

        # Store the first vector
        forces_vector = self._forces[0]

        # Check if any other forces present
        if(len(self._forces) > 1):
            # If so iterate through the list and add them (except for the first)
            for i in range(1, len(self._forces)):
                forces_vector += self._forces[i]

        # Return computed vector
        return(forces_vector)

    # --- set_time()
    # Set the time to a value
    #
    # self
    # new_time (Float) - The value to set time
    def set_time(self, new_time):

        self._time = new_time

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