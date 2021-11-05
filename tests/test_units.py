'''
    "Unit" Testing
'''

# - Imports

from ..jmath.units import Unit, define_conversion
from ..jmath.units.default import conversion_table
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

@repeat
def test_unit_multiplication():
    """Tests multipling units."""
    metres = Unit("m")
    coeffecient = random_integer()
    assert str(metres * coeffecient) == f"{coeffecient} [m]"

    metres = Unit("m")
    newtons = Unit("N")
    newton_metres = newtons * metres
    assert str(newton_metres) == "1 [Nm]"