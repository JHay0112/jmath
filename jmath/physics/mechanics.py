'''
    jmath/physics/mechanics.py

    Author: Jordan Hay
    Date: 2021-06-17

    Tools for mechanical systems
'''

# - Modules

from ..linearalgebra import Vector, Point
from ..exceptions import ZeroDistance

# - Constants

GRAVITATIONAL_CONSTANT = 6.67e-11
COULOMBS_CONSTANT = 8.99e9

# - Functions

def gravitational_force(mass1: float, mass2: float, distance: float) -> float:
    """
        Calculates the force of gravity between two masses
    
        Parameters:

        mass1 (float) - The mass of one object in kg
        mass2 (float) - The mass of the other object in kg
        distance (float) - The distance between the objects in m
    """
    return GRAVITATIONAL_CONSTANT * mass1 * mass2 / (distance**2)

def electrostatic_force(charge1: float, charge2: float, distance: float) -> float:
    """
        Calculates the electrostatic force between two charges

        Parameters:

        charge1 (float) - The charge in coulombs
        charge2 (float) - The other charge in coulombs
        distance (float) - The distance between the charges in m
    """
    return COULOMBS_CONSTANT * charge1 * charge2 / (distance**2)

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

    def increment_time(self, increment: float) -> None:
        """
            Increments the time by the given value

            Parameters:

            increment (float) - The amount to increase the time by
        """
        self.time += increment

    def add_object(self, new_obj: 'PhysObj') -> None:
        """
            Add a new Physics Object to the environment

            Parameters:

            new_obj (PhysObj) - Object to add to environment
        """
        self.objects.append(new_obj)

class PhysObj:
    """
        Creates an object with physical properties.

        Parameters:

        env (PhysEnv) - The environment that the object exists in
        position (Point) - The initial position of the object
        velocity (Vector) - The initial velocity of the object in metres per second
        mass (float:1) - The mass of the object in kilograms
        charge (float:0) - The electric charge of the object in coulombs
    """
    def __init__(self, env: PhysEnv, position: Point, velocity: Vector, mass: float = 0, charge: float = 0):

        # Assign object variables
        self.env = env
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.charge = charge

        # Add self to list in PhysEnv
        self.env.add_object(self)

    def non_zero_distance(func):
        """Wrapper that checks that there is not zero distance between objects."""
        def inner(*args, **kwargs):

            distance = args[0].position - args[1].position

            if distance.magnitude() != 0:
                return func(*args, **kwargs)
            else:
                raise ZeroDistance()

        return inner

    def momentum(self) -> Vector:
        """Calculates the momentum of the object"""
        return self.mass * self.velocity

    def force(self) -> Vector:
        """Calculates all the forces currently on the object"""
        total_force = 0 * self.position # Zero vector same magnitude as the rest
        for obj in self.env.objects:
            if obj != self:
                # Sum every force on the object
                # Gravity so far implemented
                total_force += self.gravity(obj)
                total_force += self.electrostatic(obj)

        return total_force

    def acceleration(self) -> Vector:
        """Calculates the current acceleration on the object"""
        # F = ma -> a = F/m
        return self.force() / self.mass

    @non_zero_distance
    def gravity(self, other: 'PhysObj') -> Vector:
        """
            Calculates the force of gravity between two objects

            Parameters:

            other (PhysObj) - Other physics object
        """
        if not (self.mass == 0 or other.mass == 0):
            # Distance vector between the objects
            distance = other.position - self.position # Points from self to other mass
            return gravitational_force(self.mass, other.mass, distance.magnitude()) * distance.unit()
        else:
            return self.position * 0 # Zero vector of correct size

    @non_zero_distance
    def electrostatic(self, other: 'PhysObj') -> Vector:
        """
            Calculates the force given by charge between two objects

            Parameters:

            other (PhysObj) - Other physics object
        """
        if not (self.charge == 0 or other.charge == 0):
            # Distance vector between the objects
            distance = self.position - other.position # Points away if both same charge, points together if different charge
            return electrostatic_force(self.charge, other.charge, distance.magnitude()) * distance.unit()
        else:
            return self.position * 0 # Zero vector of correct size