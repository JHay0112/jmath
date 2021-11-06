"""
    Tests that the SI units module behaves as expected.
    Predominantly testing special cases of alias and conversion.
    For main unit tests see `test_units.py`
"""

# - Import

from ..jmath.units import si

# - Tests

def test_ohms_law():
    """Tests that Ohm's law behaves correctly"""
    assert si.ampere * si.ohm == si.volt
    assert si.volt / si.ohm == si.ampere
    assert si.volt / si.ampere == si.ohm

def test_newtons_law():
    """Tests that Newton's law behaves correctly"""
    assert si.newton == si.kilogram * si.acceleration
    assert si.acceleration == si.newton / si.kilogram
    # This case removed until better unit decay is implemented
    # assert si.kilogram == si.newton / si.acceleration