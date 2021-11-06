'''
    Defines a set of other useful units.
'''

# - Imports

from .units import Unit
from .conversion import define_conversion, define_alias
from .si import kelvin
from math import pi

# - Globals

# Angles
radian = Unit("rad")
degree = Unit("°")
define_conversion(radian, degree, 180/pi)

# Temperature
centigrade = Unit("°C")
define_conversion(centigrade, kelvin, lambda x: x + 273.15)
define_conversion(kelvin, centigrade, lambda x: x - 273.15)