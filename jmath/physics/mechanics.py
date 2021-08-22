'''
    jmath/physics/mechanics.py

    Author: Jordan Hay
    Date: 2021-06-17

    Tools for mechanical systems
'''

# - Modules

from ..linearalgebra import Vector, Point
from ..exceptions import ZeroDistance
from typing import Callable
from functools import wraps

# - Constants

GRAVITATIONAL_CONSTANT = 6.67e-11
COULOMBS_CONSTANT = 8.99e9

# - Functions

def gravitational_force(mass1: float, mass2: float, distance: float) -> float:
    """
        Calculates the force of gravity between two masses
    
        Parameters
        ----------

        mass1
            The mass of one object in kg
        mass2
            The mass of the other object in kg
        distance
            The distance between the objects in m
    """
    return GRAVITATIONAL_CONSTANT * mass1 * mass2 / (distance**2)

def electrostatic_force(charge1: float, charge2: float, distance: float) -> float:
    """
        Calculates the electrostatic force between two charges

        Parameters
        ----------

        charge1
            The charge in coulombs
        charge2
            The other charge in coulombs
        distance
            The distance between the charges in m
    """
    return COULOMBS_CONSTANT * charge1 * charge2 / (distance**2)

def kinematic_position(position: Point, velocity: Vector, acceleration: Vector, time: float) -> Point:
    """
        Calculates the new position from position, velocity, acceleration, and time

        Parameters
        ----------

        position
            The initial position.
        velocity
            The inital velocity.
        acceleration
            The acceleration.
        time
            The time to approximate over
    """

    return position + velocity * time - 0.5 * acceleration * time **2

def kinematic_velocity(velocity: Vector, acceleration: Vector, time: float) -> Vector:
    """
        Calculates the new velocity from velocity, acceleration, and time.

        Parameters
        ----------

        velocity
            The inital velocity.
        acceleration
            The acceleration.
        time
            The time to approximate over
    """

    return acceleration * time + velocity

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

            Parameters
            ----------

            increment
                The amount to increase the time by
        """
        self.time += increment

    def add_object(self, new_obj: 'PhysObj') -> None:
        """
            Add a new Physics Object to the environment

            Parameters
            ----------

            new_obj
                Object to add to environment
        """
        self.objects.append(new_obj)

class PhysObj:
    """
        Creates an object with physical properties.

        Parameters
        ----------

        env
            The environment that the object exists in
        position
            The initial position of the object
        velocity
            The initial velocity of the object in metres per second
        mass
            The mass of the object in kilograms
        charge
            The electric charge of the object in coulombs
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

    def __non_zero_distance(func: Callable[["PhysObj", "PhysObj"], Vector]) -> Callable[["PhysObj", "PhysObj"], Vector]:
        """Wrapper that checks that there is not zero distance between objects."""
        @wraps(func)
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

    def increment_position(self, time: float = 0.1):
        """
            Increments the position kinematically over a time interval.
            Also updates velocity.

            Parameters
            ----------

            time
                The time interval to approximate over.
        """
        self.position = kinematic_position(self.position, self.velocity, self.acceleration(), time)
        self.velocity = kinematic_velocity(self.velocity, self.acceleration(), time)

    @__non_zero_distance
    def gravity(self, other: 'PhysObj') -> Vector:
        """
            Calculates the force of gravity between two objects

            Parameters
            ----------

            other
                Other physics object
        """
        if not (self.mass == 0 or other.mass == 0):
            # Distance vector between the objects
            distance = other.position - self.position # Points from self to other mass
            return gravitational_force(self.mass, other.mass, distance.magnitude()) * distance.unit()
        else:
            return self.position * 0 # Zero vector of correct size

    @__non_zero_distance
    def electrostatic(self, other: 'PhysObj') -> Vector:
        """
            Calculates the force given by charge between two objects

            Parameters
            ----------

            other
                Other physics object
        """
        if not (self.charge == 0 or other.charge == 0):
            # Distance vector between the objects
            distance = self.position - other.position # Points away if both same charge, points together if different charge
            return electrostatic_force(self.charge, other.charge, distance.magnitude()) * distance.unit()
        else:
            return self.position * 0 # Zero vector of correct size