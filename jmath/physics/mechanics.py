'''
    jmath/physics/mechanics.py

    Author: Jordan Hay
    Date: 2021-06-17

    Tools for mechanical systems
'''

# - Modules

from ..linearalgebra import Vector

# - Classes
class PhysEnv:

    def __init__(self, *forces):
        """
            Creates an environment for physical objects

            *forces (Vectors) - The forces that exist in the environment and apply to all objects

            Author: Jordan Hay
            Date: 2021-06-22
        """

        # Store forces *args
        self.forces = forces
        # Initialise empty list of PhysObj's
        self.objects = []
        # Set time to zero
        self.time = 0

    def forces_vector(self):
        """Computes the resultant vector of all the forces in the system"""

        # Store the first vector
        forces_vector = self.forces[0]

        # Check if any other forces present
        if(len(self.forces) > 1):
            # If so iterate through the list and add them (except for the first)
            for i in range(1, len(self.forces)):
                forces_vector += self.forces[i]

        # Return computed vector
        return(forces_vector)

    def increment_time(self, increment):
        """
            Increments the time by the given value

            increment (float) - The amount to increase the time by
        """
        self.time += increment

    def add_object(self, new_obj):
        """
            Add a new Physics Object to the environment

            new_obj (PhysObj) - Object to add to environment
        """

        self.objects.append(new_obj)
class PhysObj:

    def __init__(self, env, init_vel = Vector(0, 0, 0), mass = 1):
        """
            Creates an object with physical properties

            env (PhysEnv) - The environment that the object exists in
            init_vel (Vector) - The initial velocity of the object
            mass (int) - The mass of the object
        """

        # Assign object variables
        self.env = env
        self.init_vel = init_vel
        self.mass = mass

        # Add self to list in PhysEnv
        self.env.add_object(self)