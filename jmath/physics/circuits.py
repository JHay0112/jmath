'''
    jmath/physics/circuits.py

    Author: Jordan Hay
    Date: 2021-06-22

    Tools for circuit analysis
'''

# - Modules

from .. import discrete

# - Classes

class Circuit(discrete.Graph):
    
    def add_components(self, *components):
        """
            Add components to circuit

            \*components (Components) - Components to add to circuit
        """
        super().add_nodes(*components)

    def loops(self):
        """Returns a list of the loops in the circuit around the primary node"""
        loops = super().loops()

        # For every loop
        for loop in loops:
            # Reclassify the loops as circuit loops
            loop = Loop(loop.nodes)

        return loops

class Loop(discrete.Loop):

    def __init__(self, components):
        """
            Loop in a circuit

            components (list) - Ordered list of components to classify as a node

            Author: Jordan Hay
            Date: 2021-06-22
        """
        self.components = components
        super().__init__(components)

class Component(discrete.Node):
    
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
class DCSupply(Component):

    def __init__(self, id, voltage, current):
        """
            Supplies a DC voltage and current to a circuit

            id (str) - ID of component
            voltage (float) - Voltage in Volts to supply
            current (float) - CUrrent in Amps to supply

            Author: Jordan Hay
            Date: 2021-06-22
        """
        self.voltage = voltage
        self.current = current
        super().__init__(id, (voltage, current))