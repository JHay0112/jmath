'''
    Defines the unit class and its behaviour
'''

# - Imports

from .default import conversion_table

# - Classes

class Unit:
    '''
        A value with an associated unit.

        Parameters
        ----------

        unit
            String identifier of unit e.g. "m"        
    '''

    def __init__(self, unit: str):

        self.value = None
        self.units = {unit: 1}

    def __str__(self):
        """String representation."""

        # Produce a strign of the units
        unit_str = ""

        for unit, power in self.units.items():
            if power != 1:
                unit_str += f"{unit}^{power} "
            else:
                unit_str += f"{unit} "

        unit_str = unit_str[:-1]

        if self.value is None:
            # Just show string of units
            return unit_str
        else:
            # Show value + unit_str
            return f"{self.value} [{unit_str}]"
