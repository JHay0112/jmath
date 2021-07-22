"""
    jmath/approximation/euler_method.py

    Author: Jordan Hay
    Date: 2021-07-23

    Euler method for approximate differntial equations
"""

# - Imports

from typing import Callable, Dict

# - Functions

def euler_step(f: Callable[[float, float], float], t_k: float, y_k: float, h: float) -> float:
	"""
        Computes the euler step function for a given function

        Parameters:

        f (function) - The derivate to approximate the integral of
        t_k (float)
        y_k (float)
        h (float) - Step size
	"""
	y_k1 = y_k + f(t_k, y_k)*h
	return y_k1

def iterate_euler_step(f: Callable[[float, float], float], t_0: float, y_0: float, n: int, h: float) -> Dict[float, float]:
	"""
        Iterates upon the euler step function returning a dict of t values mapped to y values

        f (function) - The derivate to approximate the integral of
        t_0 (float) - The starting t value
        y_0 (float) - The starting y value
        n (int) - Number of steps to do
        h (float) - Step size
	"""
	euler_vls = {}
	t_k = t_0
	y_k = y_0
	for k in range(n + 1):
		euler_vls[t_k] = y_k
		y_k = euler_step(f, t_k, y_k, h)
		t_k += h

	return euler_vls
		
def euler_step_interval(f: Callable[[float, float], float], t_0: float, y_0: float, t_f: float, n: int) -> Dict[float, float]:
	"""
        Iterates euler step function using its own timestep

        f (function) - Function to approximate the integral of
        t_0 (float) - Starting t value
        y_0 (float) - Starting y value
        t_f (float) - Final t value
        n (int) - Number of steps
	"""
	h = (t_f - t_0)/n
	return iterate_euler_step(f, t_0, y_0, n, h)