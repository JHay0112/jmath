"""
    jmath/tests/test_mechanics.py

    Runs tests on Mechanics 

    Author: Jordan Hay
    Date: 2021-07-16
"""

# - Imports

from ..jmath.physics.mechanics import *

# - Tests

def test_gravity():
    """Tests that the graviational force between two objects at a distance is as expected."""
    env = PhysEnv()
    obj1 = PhysObj(env, Point(0, 0), Vector(0, 0), 1)
    obj2 = PhysObj(env, Point(1, 0), Vector(0, 0), 2)
    expected_grav = (GRAVITATIONAL_CONSTANT * 1 * 2)
    # Pointing from obj1 to obj2
    expected_grav_vec = Vector(expected_grav, 0)
    assert obj1.gravity(obj2).components == expected_grav_vec.components
    assert obj2.gravity(obj1).components == expected_grav_vec.negative().components

def test_electrostatic():
    """Tests that the electrostatic force between two object at a distance is as expected"""
    env = PhysEnv()
    obj1 = PhysObj(env, Point(0, 0), Vector(0, 0), charge = 1)
    obj2 = PhysObj(env, Point(0, 2), Vector(0, 0), charge = 1)
    expected_electro = COULOMBS_CONSTANT/4
    # Pointing from obj1 to obj2
    expected_electro_vec = Vector(0, expected_electro)
    assert obj1.electrostatic(obj2).components == expected_electro_vec.components
    assert obj2.electrostatic(obj1).components == expected_electro_vec.negative().components