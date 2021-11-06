'''
    Defines a set of SI units and their conversion factors
'''

# - Imports

from .units import Unit
from .conversion import define_alias, define_conversion, alias_table, conversion_table

# - Globals

# Base Units

metre = Unit("m")
second = Unit("s")
kilogram = Unit("kg")
ampere = Unit("A")
kelvin = Unit("K")
mole = Unit("mol")
candela = Unit("cd")

# Derived Units

newton = Unit("N")
define_alias(kilogram * metre / (second ** 2), newton)

joule = Unit("J")
define_alias(newton * metre, joule)

coulomb = Unit("C")
define_alias(ampere * second, coulomb)

pascal = Unit("Pa")
define_alias(newton/(metre ** 2), pascal)

watt = Unit("W")
define_alias(joule/second, watt)

volt = Unit("V")
define_alias(watt/ampere, volt)

farad = Unit("F")
define_alias(coulomb/volt, farad)

ohm = Unit("Ω")
define_alias(ampere * ohm, volt)
define_alias(volt/ampere, ohm)

siemens = Unit("S")
define_alias(ampere/volt, siemens)

weber = Unit("Wb")
define_alias(volt * second, weber)

tesla = Unit("T")
define_alias(weber/(metre**2), tesla)

henry = Unit("H")
define_alias(weber/ampere, henry)

# Base Constants

c = 3.000e8 * metre/second
h = 6.626e-34 * joule*second
e = 1.602e-19 * coulomb
k = 1.381e-23 * joule/kelvin
N = 6.022e23 / mole

# Unit conversions

# Mass to energy
define_conversion(kilogram, joule, c**2)