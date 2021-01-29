'''
    jmath.py

    Author: Jordan Hay
    Date: 2020-11-02
    Version: 0.7.1

    Jordan's Math Module

    Creating my own maths tools in Python as a challenge.
'''

# - Modules

import math # Mathematical functions, e.g. sqrt()
import operator # Python operators
import matplotlib.pyplot as plt # Visualisation

# - Classes

# -- Vector
# Author: Jordan Hay
# Date: 2020-11-02
# Version: 0.5.3
# A vector with n dimensions
class Vector:

    # --- __init__()
    # Initialise Vector object
    #
    # self
    # *components (List/*args) - Scalar vector components, e.g. x, y, z
    def __init__(self, *components):

        # If components[0] is list store that list
        if(type(components[0]) == list):
            self._components = components[0]
        else:
            # Else it's *args
            self._components = components

    # --- __add__()
    # Add another Vector object to this Vector
    #
    # self
    # vector (Vector) - The foreign Vector to add
    def __add__(self, vector):

        # Add the foreign components to local components and return
        return(Vector(list(map(operator.add, self._components, vector.components()))))

    # --- __sub__()
    # Subtract another Vector object from this vector
    #
    # self
    # vector (Vector) - The foreign Vector to subtract
    def __sub__(self, vector):

        # Subtract the foreign components from local components and return
        return(Vector(list(map(operator.sub, self._components, vector.components()))))

    # --- components()
    # Returns the components of the vector
    #
    # self
    def components(self):

        return(self._components)

    # --- magnitude()
    # Returns the magnitude of the vector as calculated from the components
    #
    # self
    def magnitude(self):

        # Store magnitude while computing
        magnitude = 0

        # For every vector component
        for c in self._components:
            # Pythagorean theorom
            # hypotenuse = sqrt(a**2 + b**2)
            magnitude = math.sqrt(magnitude ** 2 + c ** 2)

        return(magnitude)

    # --- draw()
    # Draws a 2D arrow
    #
    # self
    # x (int) - The dimension to plot on the x-axis
    # y (int) - The dimension to plot on the y-axis
    def draw(self, x = 0, y = 1):

        ax = plt.axes()
        ax.arrow(0, 0, self._components[x], self._components[y], head_width=0.05, head_length=0.05)
        plt.show()

# -- Node
# Author: Jordan Hay
# Date: 2021-01-29
# Version: 1.0.2
# Node of a Graph
class Node:

    # --- __init__()
    # Initialise the Node
    #
    # self
    # *neighbours (Nodes) - Neighbouring nodes
    def __init__(self, *neighbours):

        self._neighbours = list(neighbours)

    # --- neighbours()
    # Returns the neighbouring nodes
    #
    # self
    def neighbours(self): 
        
        return(self._neighbours)

    # --- add_neighbours()
    # Add new neighbouring nodes
    #
    # self
    # *neighbours (Nodes) - Neighbouring nodes
    def add_neighbours(self, *neighbours):

        self._neighbours.extend(neighbours)

    # --- remove_neighbours()
    # Remove existing neighbouring nodes
    #
    # self
    # *neighbours (Nodes) - Neighbouring nodes
    def remove_neighbours(self, *neighbours):

        self._neighbours = list(set(self._neighbours) - set(neighbours))

# -- Graph
# Author: Jordan Hay
# Date: 2021-01-29
# Version: 1.0.0
class Graph:

    # --- __init__()
    # Initialise a graph
    #
    # self
    # check (bool) - Default true, runs check that all nodes are correctly formatted
    def __init__(self, check = True):

        self._check = check
        self._nodes = []

    # --- check()
    # Check node formation
    #
    # self
    def check(self):
        # Check if check enabled
        if(self._check):
            # For every node
            for node in self._nodes:
                # For every neighbour to the node
                for neighbour in node.neighbours():
                    # If the neighbour doesn't know that this node is a neighbour
                    if(node not in neighbour.neighbours()):
                        # Add this node
                        neighbour.add_neighbours(node)

    # --- add_nodes()
    # Add nodes to the graph
    #
    # self
    # *nodes (Nodes) - Graph nodes
    def add_nodes(self, *nodes):

        self._nodes.extend(nodes)
        self.check()

# -- PhysEnv
# Author: Jordan Hay
# Date: 2020-11-08
# Version: 0.1.0
# Physical Environment
class PhysEnv:

    # --- __init___()
    # Initialise the Physics Environment
    #
    # self
    # *forces (Vectors) - The forces that exist within the physics environment, e.g. Gravity
    def __init__(self, *forces):

        # Store forces *args
        self._forces = forces
        # Initialise empty list of PhysObj's
        self._objects = []
        # Set time to zero
        self._time = 0

    # --- time()
    # Returns time
    #
    # self
    def time(self):

        return(self._time)

    # --- forces_vector()
    # The Vector object that represents all the forces present in the systems
    #
    # self
    def forces_vector(self):

        # Store the first vector
        forces_vector = self._forces[0]

        # Check if any other forces present
        if(len(self._forces) > 1):
            # If so iterate through the list and add them (except for the first)
            for i in range(1, len(self._forces)):
                forces_vector += self._forces[i]

        # Return computed vector
        return(forces_vector)

    # --- set_time()
    # Set the time to a value
    #
    # self
    # new_time (Float) - The value to set time
    def set_time(self, new_time):

        self._time = new_time

    # --- increment_time()
    # Increment the time by an amount
    #
    # self
    # increment (Float) - The amount to increase the time by
    def increment_time(self, increment):

        self._time += increment

    # --- add_object()
    # Add PhysObj to list
    #
    # self
    # new_obj (PhysObj) - The object to add
    def add_object(self, new_obj):

        self._objects.append(new_obj)

# -- PhysObj
# Author: Jordan Hay
# Date: 2020-11-06
# Version: 0.0.1
# Physical Object
class PhysObj:

    # --- __init__()
    # Initialise the PhysObj Object
    #
    # self
    # env (PhysEnv) - The environment the object exists in
    # init_vel (Vector) - An initial velocity vector
    # mass (Int) - The mass of the object
    def __init__(self, env, init_vel = Vector(0, 0, 0), mass = 1):

        # Assign object variables
        self._env = env
        self._init_vel = init_vel
        self._mass = mass

        # Add self to list in PhysEnv
        self._env.add_object(self)