'''
    Tests the approximate definite integral functions provided in jmath.approximation
'''

# - Imports

from .tools import random_integer, repeat
from ..jmath.approximation import trapezium_rule, right_hand_rule, left_hand_rule

# - Tests

@repeat
def test_on_increasing_func():
    """Tests that on an increasing linear function the left hand rule underestimates, the right hand rule over estimates, and trapezium rule is exact"""
    coeffecient = random_integer(1, 100)
    linear_function = lambda x : coeffecient*x
    lower_bound = random_integer(0, 99)
    upper_bound = random_integer(lower_bound, 100)
    samples = upper_bound - lower_bound
    
    # Find exact area since it is linear
    exact_area = 0.5*upper_bound*linear_function(upper_bound) - 0.5*lower_bound*linear_function(lower_bound)

    # Use approximations
    trapezium_area = trapezium_rule(linear_function, lower_bound, upper_bound, samples)
    left_area = left_hand_rule(linear_function, lower_bound, upper_bound, samples)
    right_area = right_hand_rule(linear_function, lower_bound, upper_bound, samples)

    # Assert trapezium and exact match to 5 dp
    assert round(trapezium_area, 5) == round(exact_area, 5)

    # Assert left less than trapezium less than right
    assert left_area < trapezium_area < right_area

@repeat
def test_on_decreasing_func():
    """Tests that on a decreasing linear function the left hand rule overestimates, the right hand rule underestimates, and trapezium rule is exact"""
    coeffecient = random_integer(-100, -1)
    linear_function = lambda x : coeffecient*x
    lower_bound = random_integer(0, 99)
    upper_bound = random_integer(lower_bound, 100)
    samples = upper_bound - lower_bound
    
    # Find exact area since it is linear
    exact_area = 0.5*upper_bound*linear_function(upper_bound) - 0.5*lower_bound*linear_function(lower_bound)

    # Use approximations
    trapezium_area = trapezium_rule(linear_function, lower_bound, upper_bound, samples)
    left_area = left_hand_rule(linear_function, lower_bound, upper_bound, samples)
    right_area = right_hand_rule(linear_function, lower_bound, upper_bound, samples)

    # Assert trapezium and exact match to 5 dp
    assert round(trapezium_area, 5) == round(exact_area, 5)

    # Assert left moe than trapezium more than right
    assert left_area > trapezium_area > right_area