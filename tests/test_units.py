'''
    "Unit" Testing
'''

# - Imports

from ..jmath.units import Unit, define_conversion
from ..jmath.units.default import conversion_table

# - Testing

def test_unit_creation():
    """Tests that units are created as expected."""
    unit = Unit("m")
    assert unit.units["m"] == 1
    assert str(unit) == "m"

def test_unit_union():
    """Tests that units can be unioned."""
    # Simple test
    metres = Unit("m")
    newtons = Unit("N")
    newton_metres = newtons | metres
    assert str(newton_metres) == "Nm"