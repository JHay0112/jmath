'''
    jmath/physics/circuits.py

    Author: Jordan Hay
    Date: 2021-06-22

    Tools for circuit analysis
'''

# - Modules

from ..discrete import *

# - Classes

class Circuit(Graph):
    
    def add_components(self, *components):
        """
            Add components to circuit

            *components (Components) - Components to add to circuit
        """
        super().add_nodes(*components)
class Component(Node):
    
    def __init__(self, id, weight = 0):
        """
            Base for circuit components

            id (str) - ID of component e.g. R1
            weight (float:0) - Component weighting (resistance for resistors etc.)

            Author: Jordan Hay
            Date: 2021-06-22
        """

        super().__init__(id, weight)

    def connect(self, neighbour):
        """
            Adds a neighbouring component

            neighbour (Component) - Neighbouring component to add
        """
        super().add_neighbour(neighbour, 0, False)

class Resistor(Component):

    def __init__(self, id, resistance):
        """
            Ideal Resistor

            id (str) - ID of component
            resistance (float) - Resistance in Ohms of the resistor

            Author: Jordan Hay
            Date: 2021-06-22
        """
        self.resistance = resistance
        super().__init__(id, resistance)

    def power(self, current):
        """
            Calculate power consumption from current

            current (float) - Current in amps flowing through resistor
        """
        return (current ** 2) * self.resistance
class DCVoltageSource(Component):

    def __init__(self, id, voltage):
        """
            Supplies a DC voltage to a circuit

            id (str) - ID of component
            voltage (float) - Voltage in Volts to supply

            Author: Jordan Hay
            Date: 2021-06-22
        """
        self.voltage = voltage
        super().__init__(id, voltage)