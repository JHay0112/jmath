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

unit_names = {
    "m": "metre",
    "s": "second",
    "g": "gram",
    "A": "ampere",
    "K": "kelvin",
    "mol": "mole", 
    "cd": "candela", 
    "N": "newton",
    "J": "joule",
    "C": "coulomb",
    "Pa": "pascal", 
    "W": "watt",
    "V": "volt",
    "F": "farad",
    "Ω": "ohm",
    "S": "siemens",
    "Wb": "weber",
    "T": "tesla",
    "H": "henry"
}

units = {unit: Unit(unit, si) for unit in unit_names.keys()}

# Conversion
for prefix, factor in prefixes.items():
    for name, unit in units.items():
        combo = prefix + name
        si.define_conversion(Unit(combo, si), unit, factor)

for unit, name in unit_names.items():
    # Special names
    si.define_alias(name, si[unit])

# Special case for kg
si.kilogram = si.kg

# Standard Forms

si.displacement = si.metre
si.velocity = si.metre/si.second
si.acceleration = si.metre/(si.second**2)

# Aliases

si.define_alias(si.kilogram * si.metre / (si.second ** 2), si.newton)
si.define_alias(si.ampere * si.second, si.coulomb)
si.define_alias(si.newton/(si.metre ** 2), si.pascal)
si.define_alias(si.joule/si.second, si.watt)
si.define_alias(si.watt/si.ampere, si.volt)
si.define_alias(si.coulomb/si.volt, si.farad)
si.define_alias(si.ampere * si.ohm, si.volt)
si.define_alias(si.newton * si.metre/si.coulomb, si.volt)
si.define_alias(si.volt/si.ampere, si.ohm)
si.define_alias(si.ampere/si.volt, si.siemens)
si.define_alias(si.volt * si.second, si.weber)
si.define_alias(si.weber/(si.metre**2), si.tesla)
si.define_alias(si.weber/si.ampere, si.henry)

# Base Constants

c = 3.000e8 * si.metre/si.second
h = 6.626e-34 * si.joule*si.second
e = 1.602e-19 * si.coulomb
k = 1.381e-23 * si.joule/si.kelvin
N = 6.022e23 / si.mole

# Conversions

si.define_conversion(si.kilogram, si.joule, c**2)