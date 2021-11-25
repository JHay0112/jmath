'''
    Defines a set of other useful units.
'''

# - Imports

from .units import Unit
from .conversion import UnitSpace
from .si import si, c, e
from math import pi

# - Main

other = UnitSpace()

# Angles
other.radian = Unit("rad")
other.degree = Unit("°")
other.define_conversion(other.radian, other.degree, 180/pi)

# Temperature
other.centigrade = Unit("°C")
other.define_conversion(other.centigrade, si.kelvin, lambda x: x + 273.15)
other.define_conversion(si.kelvin, other.centigrade, lambda x: x - 273.15)

# Physics
# -- Light Speed
other.lightspeed = Unit("c")
other.define_conversion(other.lightspeed, si.metre/si.second, c)
# -- Electron Volts
other.electron_volt = Unit("eV")
other.define_conversion(other.electron_volt, si.joule, e)
# -- Electron Volt Mass Energy
other.electron_volt_mass = other.electron_volt/(other.lightspeed**2)
other.define_conversion(other.electron_volt_mass, other.electron_volt, 1)
other.define_conversion(other.electron_volt_mass, si.kilogram, e/(c**2))
other.define_conversion(other.electron_volt_mass, si.joule, e)