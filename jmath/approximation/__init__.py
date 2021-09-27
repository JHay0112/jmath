'''
    jmath/approximation/__init__.py

    Tools for approximating mathematical equations.

    Default Packages
    -----------------

    jmath.approximation.euler_method
        The Euler Method for approximating the integrals of differential equations.
    jmath.approximation.newton_method
        The Newton Method for approximating the roots of an equation.
    jmath.approximation.differentiation
        Numerical method for approximating differentials of functions.
    jmath.approximation.integration
        Numerical methods for approximating definite integrals.
'''

# - Namespace

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# - Defaults

from .euler_method import euler_step, euler_step_interval, iterate_euler_step
from .newton_method import newton_method
from .differentiation import differentiate
from .integration import left_hand_rule, right_hand_rule, trapezium_rule, discrete_trapezium_rule