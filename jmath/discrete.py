'''
    components/discrete.py

    Author: Jordan Hay
    Date: 2021-06-17

    Discrete mathematical tools
'''

# - Classes

# -- Node
# Author: Jordan Hay
# Date: 2021-01-29
# Node of a Graph
class Node:

    # --- __init__()
    # Initialise the Node
    #
    # self
    # name (str) - Node name
    # *neighbours (Nodes) - Neighbouring nodes
    def __init__(self, name, *neighbours):

        self._name = name
        self._neighbours = list(neighbours)

    # --- name()
    # Returns the node name
    #
    # self
    def name(self):

        return(self._name)

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

    # --- relationships()
    # Human readable computation of what nodes this object is neighbouring
    #
    # self
    def relationships(self):

        relationship = f"[{self._name}]"

        for neighbour in self._neighbours:
            relationship += "\n"
            relationship += f"  ∟[{neighbour.name()}]"

        return(relationship)

# -- Graph
# Author: Jordan Hay
# Date: 2021-01-29
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

        # Check if first "node" is a Node
        if(isinstance(nodes[0], Node)):
            # Therefore *nodes is being used as expected
            # Extend nodes list with *nodes tuple
            self._nodes.extend(nodes)
        else:
            # Else an iterable is being passed as nodes[0]
            self._nodes.extend(nodes[0])

        self.check()

    # --- relationships()
    # Human readable computation of all nodes and their relationship with other nodes
    #
    # self
    def relationships(self):

        relationships = ""

        for node in self._nodes:
            relationships += node.relationships() + "\n"

        return(relationships)