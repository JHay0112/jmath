'''
    Tests that unit spaces work, predominantly for leak protection.
'''

# - Imports

from ..jmath.units import Unit, universal, UnitSpace
from .tools import random_integer, repeat

# - Tests

def test_si_leak():
    """Tests to see if SI units are leaking into universal."""
    # Import SI
    from ..jmath.units import si
    # Check to see universal is empty
    assert universal.units == {}

def test_assignment_leak():
    """Tests that units do not leak on assignment."""
    space = UnitSpace()
    a = Unit("a", space)
    space["b"] = Unit("b")
    space.c = Unit("c")
    # Universal set should still be empty
    assert universal.units == {}

@repeat
def test_conversion_leak():
    """Tests that unit conversion does not leak."""
    space = UnitSpace()
    space.a = Unit("a")
    space.b = Unit("b")
    space.define_conversion(space.a, space.b, random_integer())
    assert space.a == space.a.convert_to(space.b).convert_to(space.a)
    assert universal.units == {}

def test_alias_leak():
    """Tests that unit aliases do not leak."""
    space = UnitSpace()
    space.a = Unit("a")
    space.b = Unit("b")
    space.c = Unit("c")
    space.define_alias(space.a * space.b, space.c)
    assert space.a * space.b == space.c 
    assert space.c / space.b == space.a
    assert space.c / space.a == space.b
    assert universal.units == {}