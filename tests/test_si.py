"""
    Tests that the SI units module behaves as expected.
    Predominantly testing special cases of alias and conversion.
    For main unit tests see `test_units.py`
"""

# - Import

from ..jmath.units import si

# - Tests

def test_ohms_law():
    """Tests that ohms law behaves correctly"""
    assert si.ampere * si.ohm == si.volt
    assert si.volt / si.ohm == si.ampere
    assert si.volt / si.ampere == si.ohm
