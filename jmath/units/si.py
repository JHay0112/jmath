'''
    Defines a set of SI units and their conversion factors.

    Examples
    --------

    >>> from jmath.units import si
    >>> voltage_drop = Uncertainty(3, 0.2) * si.volt
    >>> current = Uncertainty(0.1, 0.02) * si.ampere
    >>> resistance = voltage_drop/current
    >>> print(resistance)
    (30 ± 8) [Ω] 
'''

# - Imports

from .units import Unit
from .conversion import UnitSpace

# - Main

# Unit space

si = UnitSpace()

# Prefixes

prefixes = {
    "Y": 1e24,
    "Z": 1e21,
    "E": 1e18,
    "P": 1e15,
    "T": 1e12,
    "G": 1e9,
    "M": 1e6,
    "k": 1e3,
    "m": 1e-3,
    "μ": 1e-6,
    "n": 1e-9,
    "p": 1e-12,
    "f": 1e-15,
    "a": 1e-18,
    "z": 1e-21,
    "y": 1e-24
}

# Units

unit_names = [
    "m", "s", "g", "A", "K",
    "mol", "cd", "N", "J", "C",
    "Pa", "W", "V", "F", "Ω",
    "S", "Wb", "T", "H"
]

units = {unit: Unit(unit, si) for unit in unit_names}

# Conversion
for prefix, factor in prefixes.items():
    for name, unit in units.items():
        combo = prefix + name
        si.define_conversion(Unit(combo, si), unit, factor)

# Names

metre = units["m"]
second = units["s"]
kilogram = Unit("kg", si)
ampere = units["A"]
kelvin = units["K"]
mole = units["mol"]
candela = units["cd"]
newton = units["N"]
joule = units["J"]
coulomb = units["C"]
pascal = units["Pa"]
watt = units["W"]
volt = units["V"]
farad = units["F"]
ohm = units["Ω"]
siemens = units["S"]
weber = units["Wb"]
tesla = units["T"]
henry = units["H"]

# Standard Forms

displacement = metre
velocity = metre/second
acceleration = metre/(second**2)

# Aliases

si.define_alias(kilogram * metre / (second ** 2), newton)
si.define_alias(ampere * second, coulomb)
si.define_alias(newton/(metre ** 2), pascal)
si.define_alias(joule/second, watt)
si.define_alias(watt/ampere, volt)
si.define_alias(coulomb/volt, farad)
si.define_alias(ampere * ohm, volt)
si.define_alias(volt/ampere, ohm)
si.define_alias(ampere/volt, siemens)
si.define_alias(volt * second, weber)
si.define_alias(weber/(metre**2), tesla)
si.define_alias(weber/ampere, henry)

# Base Constants

c = 3.000e8 * metre/second
h = 6.626e-34 * joule*second
e = 1.602e-19 * coulomb
k = 1.381e-23 * joule/kelvin
N = 6.022e23 / mole

# Conversions

si.define_conversion(kilogram, joule, c**2)