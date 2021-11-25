'''
    Test Universal Functions
'''

# - Imports

from .tools import repeat, random_integer
from ..jmath.universal.tools import generic_function, Supported
from ..jmath.uncertainties import Uncertainty
from ..jmath.units import Unit
from typing import Tuple, Callable

# - Tests

def function_pair() -> Tuple[Callable[[float], float], Callable[[Supported], Supported]]:
    """Produces a function and its generic version."""
    a = random_integer()
    f = lambda x: a * x
    genf = lambda x: generic_function(f, x)
    return f, genf

@repeat
def test_numeric():
    """Tests that numeric values work with generic functions."""
    a = random_integer()
    f, genf = function_pair()
    assert f(a) == genf(a)

@repeat
def test_uncertainty():
    """Tests that uncertain values work with generic functions."""
    a = random_integer(1, 100)
    b = random_integer(0, a - 1)
    unc = Uncertainty(a, b)
    f, genf = function_pair()
    assert unc.apply(f).value == genf(unc).value
    assert unc.apply(f).abs_uncertainty() == genf(unc).abs_uncertainty()

@repeat
def test_unit():
    """Tests that unit values work with generic functions."""
    a = random_integer() * Unit("TEST")
    f, genf = function_pair()
    assert f(a) == genf(a)
