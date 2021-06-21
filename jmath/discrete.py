'''
    jmath/discrete.py

    Author: Jordan Hay
    Date: 2021-06-17

    Discrete mathematical tools
'''

# - Classes

class Node:
    """
        Author: Jordan Hay
        Date: 2021-01-29

        Node of a graph

        id (str) - Unique ID string describing the object
        weight (float:1) - Weighting of node
    """

    def __init__(self, id, weight = 1):
        """Node Constructor"""

        self.id = id
        self.weight = weight
        self.neighbours = {}

    def __str__(self):
        """String representation"""

        return self.id

    def __repr__(self):
        """Programming Representation"""

        return f"Node('{self.id}', {self.weight})"

    def neighbours_list(self): 
        """Returns the IDs of the neighbouring nodes"""
        return(list(self.neighbours.keys()))

    def add_neighbour(self, neighbour, weight = 1, two_way = False):
        """
            Adds a neighbouring node

            neighbour (Node) - Node object describing the neighbour
            weight (float:1) - The weighting of the relationship
            two_way (bool:False) - Whether the relationship goes both ways
        """
        self.neighbours[neighbour] = weight

        if two_way:
            neighbour.add_neighbour(self, weight)

    def remove_neighbour(self, neighbour):
        """
            Removes the relationship between the nodes (ONLY FROM THIS NODE)

            neighbour (Node) - Node object describing the neighbour node
        """
        self.neighbours.pop(neighbour)

    
    def relationships(self):
        """Returns human readable string of relationships between node and neighbours"""

        relationship = f"[{self.id}:{self.weight}]"

        for neighbour, weight in self.neighbours.items():
            relationship += "\n"
            relationship += f"  -{weight}-[{neighbour.id}:{neighbour.weight}]"

        return(relationship)

# -- Graph
# Author: Jordan Hay
# Date: 2021-01-29
class Graph:
    """
        Author: Jordan Hay
        Date: 2021-01-29

        Graph made of nodes
    """

    def __init__(self):
        """Graph constructor"""

        self.nodes = []

    def add_nodes(self, *nodes):
        """
            Adds node/s to the graph

            *nodes (Nodes) - Graph nodes
        """

        # Check if first "node" is a Node
        if(isinstance(nodes[0], Node)):
            # Therefore *nodes is being used as expected
            # Extend nodes list with *nodes tuple
            self.nodes.extend(nodes)
        else:
            # Else an iterable is being passed as nodes[0]
            self.nodes.extend(nodes[0])

    def get_node(self, id):
        """
            Returns a node object in the graph based upon its ID

            id (str) - The ID of the node
        """
        # Loop through the nodes
        for node in self.nodes:
            # Check if name matches
            if node.id == id:
                # If so return
                return node
        # No node found so return none
        return None

    def relationships(self):
        """Returns a human readable description of the relationship between all nodes"""
        relationships = ""

        for node in self.nodes:
            relationships += node.relationships() + "\n"

        return(relationships)

    def walk(self, start, stop = None, neighbour = 0, default_neighbour = 0):
        """
            "Walks" a loop around the graph, intended for generating loops for self.loops()

            start (Node) - Node the walk starts at
            stop (Node) - Node the walk stops at
            neighbour (int:0) - Initial neighbour to move to
            default_neighbour (int:0) - Neighbour to automatically move to
        """

        if stop == None:
            stop = start

        loop = [start]
        node = start.neighbours_list()[neighbour]
        
        while node != stop:
            loop.append(node)
            if len(node.neighbours) != 0:
                node = node.neighbours_list()[default_neighbour]
            else:
                # Dead end
                return None

        # Generate graph representation
        graph = Graph()
        graph.add_nodes(loop)
        return graph

    def loops(self):
        """Finds loops in the graph"""
        loops = []
        intersections = [node for node in self.nodes if len(node.neighbours) > 1 and self.nodes.index(node) != 0]

        # For every neighbour on the primary node
        for i in range(len(self.nodes[0].neighbours)):
            loops.append(self.walk(self.nodes[0], neighbour = i))

        # For the rest of the intersections do not walk the zeroth option
        for i in range(len(intersections)):
            # For every intersection
            for j in range(1, len(intersections[i].neighbours)):
                # For every neighbour on the intersection except 0
                loops.append(self.walk(intersections[i], neighbour = j))

        return loops