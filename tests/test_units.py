'''
    "Unit" Testing
'''

# - Imports

from ..jmath.units import Unit, define_conversion, define_alias
from ..jmath.uncertainties import Uncertainty
from .tools import repeat, random_integer

# - Testing

def test_unit_creation():
    """Tests that units are created as expected."""
    # Standard units
    unit = Unit("m")
    assert unit.units["m"] == 1
    assert str(unit) == "1 [m]"
    # Inverse units
    # Per metre
    unit = 1/unit
    assert unit.units["m"] == -1
    assert str(unit) == "1.0 [m^(-1)]"

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

@repeat
def test_conversion():
    """Tests that unit conversion happens as expected."""
    a = Unit("a")
    b = Unit("b")
    coeffecient = random_integer()
    define_conversion(a, b, coeffecient)

    assert a.convert_to(b).value, 16 == (a*coeffecient).value
    assert b.convert_to(a).value == (b/coeffecient).value
    assert round(a.convert_to(b).convert_to(a), 15) == a
    assert round(b.convert_to(a).convert_to(b), 15) == b

@repeat
def test_uncertain_units():
    """Tests that units and uncertainties play nice."""
    a = random_integer(10, 99)
    b = random_integer(0, 9)
    unc = Uncertainty(a, b)
    unit = unc * Unit("m")

    assert str(unit) == f"({a} ± {b}) [m]"