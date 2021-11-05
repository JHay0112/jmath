'''
    "Unit" Testing
'''

# - Imports

from ..jmath.units import Unit
from .tools import repeat, random_integer

# - Testing

def test_unit_creation():
    """Tests that units are created as expected."""
    unit = Unit("m")
    assert unit.units["m"] == 1
    assert str(unit) == "1 [m]"

def test_unit_union():
    """Tests that units can be unioned."""
    # Simple test
    metres = Unit("m")
    newtons = Unit("N")
    newton_metres = newtons | metres
    assert str(newton_metres) == "1 [Nm]"

def test_unit_combination():
    """Test unit combination through multiplication."""
    metres = Unit("m")
    newtons = Unit("N")
    newton_metres = newtons * metres
    assert str(newton_metres) == "1 [Nm]"

@repeat
def test_unit_multiplication():
    """Tests multipling units."""
    metres = Unit("m")
    coeffecient = random_integer()
    assert str(metres * coeffecient) == f"{coeffecient} [m]"