'''
    jmath/physics/mechanics.py

    Author: Jordan Hay
    Date: 2021-06-17

    Tools for mechanical systems
'''

# - Modules

from ..linearalgebra import Vector, Point

# - Constants

GRAVITATIONAL_CONSTANT = 6.67e-11
COULOMBS_CONSTANT = 8.99e9

# - Classes
class PhysEnv:
    """
        Creates an environment for physical objects

        Author: Jordan Hay
        Date: 2021-06-22
    """
    def __init__(self):

        # Initialise empty list of PhysObj's
        self.objects = []
        # Set time to zero
        self.time = 0

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

    def __init__(self, env, position, velocity, mass = 1, charge = 0):
        """
            Creates an object with physical properties

            env (PhysEnv) - The environment that the object exists in
            position (Point) - The initial position of the object
            velocity (Vector) - The initial velocity of the object in metres per second
            mass (float:1) - The mass of the object in kilograms
            charge (float:0) - The electric charge of the object in coulombs
        """

        # Assign object variables
        self.env = env
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.charge = charge

        # Add self to list in PhysEnv
        self.env.add_object(self)

    def momentum(self):
        """Calculates the momentum of the object"""
        return self.mass * self.velocity

    def force(self):
        """Calculates all the forces currently on the object"""
        total_force = 0 * self.position # Zero vector same magnitude as the rest
        for obj in self.env.objects:
            # Sum every force on the object
            # Gravity so far implemented
            total_force += self.gravity(obj)
            total_force += self.electrostatic(obj)

        return total_force

    def acceleration(self):
        """Calculates the current acceleration on the object"""
        # F = ma -> a = F/m
        return self.force() / self.mass

    def gravity(self, other):
        """
            Calculates the force of gravity between two objects

            other (PhysObj) - Other physics object
        """
        # Distance vector between the objects
        distance = other.position - self.position

        return (GRAVITATIONAL_CONSTANT * self.mass * other.mass)/(distance.magnitude() ** 2) * distance.unit_vector()

    def electrostatic(self, other):
        """
            Calculates the force given by charge between two objects

            other (PhysObj) - Other physics object
        """
        # Distance vector between the objects
        distance = other.position - self.position

        return (COULOMBS_CONSTANT * self.charge * other.charge)/(distance.magnitude() ** 2) * distance.unit_vector()