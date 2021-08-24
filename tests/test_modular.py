"""
    Test modular arithmetic 
"""

# - Imports

from ..jmath.modular import extended_gcd, modular_inverse
from .tools import random_integer, repeat
from math import gcd

# - Tests

@repeat
def test_gcd():
    """Tests extended gcd function."""
    n1 = random_integer(0, 100)
    n2 = random_integer(0, 100)
    g, m, n = extended_gcd(n1, n2)

    assert g == gcd(n1, n2)
    assert g == m*n1 + n*n2

@repeat
def test_modular_inverse():
    """Tests modular inverse calculator."""
    a = random_integer(0, 100)
    b = random_integer(a, 100)
    a_inverse = modular_inverse(a, b)

    # If a is not relatively prime with b then there is no inverse
    if gcd(a, b) != 1:
        assert a_inverse == None
    else:
        assert 1 == a*a_inverse % b