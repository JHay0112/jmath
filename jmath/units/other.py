'''
    Defines a set of other useful units.
'''

# - Imports

from .units import Unit
from .conversion import define_conversion, define_alias
from .si import joule, kelvin, metre, second, kilogram, c, e
from math import pi

# - Main

# Angles
radian = Unit("rad")
degree = Unit("°")
define_conversion(radian, degree, 180/pi)

# Temperature
centigrade = Unit("°C")
define_conversion(centigrade, kelvin, lambda x: x + 273.15)
define_conversion(kelvin, centigrade, lambda x: x - 273.15)

# Physics
# -- Light Speed
lightspeed = Unit("c")
define_conversion(lightspeed, metre/second, c)
# -- Electron Volts
electron_volt = Unit("eV")
define_conversion(electron_volt, joule, e)
# -- Electron Volt Mass Energy
electron_volt_mass = electron_volt/(lightspeed**2)
define_conversion(electron_volt_mass, electron_volt, 1)
define_conversion(electron_volt_mass, kilogram, e/(c**2))
define_conversion(electron_volt_mass, joule, e)