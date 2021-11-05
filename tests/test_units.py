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