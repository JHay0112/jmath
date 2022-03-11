'''
    Tests the auto-differentiation module
'''

# - Imports

from ..jmath.autodiff import analyse, Variable, Function, x, y, z, a, b, c
from .tools import random_integer, repeat

# - Tests

@repeat
def test_linear_derivatives():
    '''Tests the derivatives of linear functions.'''
    m = random_integer()
    c = random_integer()
    y = m*x + c
    assert y.d(x) == m