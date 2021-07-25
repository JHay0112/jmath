'''
    jmath/discrete.py

    Discrete mathematical tools.
'''

# - Imports

from typing import Union, List

# - Classes

class Node:
    """
        Node of a graph.

        Parameters
        ----------

        id
            Unique ID string describing the object.
        weight
            Weighting of node.
    """
    def __init__(self, id: str, weight: float = 1):

        self.id = id
        self.weight = weight
        self.neighbours = {}

    def __str__(self) -> str:
        """String representation"""

        return f"[{self.id}:{self.weight}]"

    def __repr__(self) -> str:
        """Programming Representation"""

        return f"Node('{self.id}', {self.weight})"

    def neighbours_list(self) -> list: 
        """Returns the IDs of the neighbouring nodes"""
        return(list(self.neighbours.keys()))

    def add_neighbour(self, neighbour: "Node", weight: float = 1, two_way: bool = False):
        """
            Adds a neighbouring node

            Parameters
            ----------

            neighbour
                Node object describing the neighbour.
            weight
                The weighting of the relationship.
            two_way
                Whether the relationship goes both ways.
        """
        self.neighbours[neighbour] = weight

        if two_way:
            neighbour.add_neighbour(self, weight)

    def remove_neighbour(self, neighbour: "Node"):
        """
            Removes the relationship between the nodes.

            Parameters
            ----------

            neighbour
                Node object describing the neighbour node

            Notes
            -----
            Only removes the neighbourship from THIS NODE.
        """
        self.neighbours.pop(neighbour)

    
    def relationships(self) -> str:
        """Returns human readable string of relationships between node and neighbours."""

        relationship = f"{self}"

        for neighbour, weight in self.neighbours.items():
            relationship += "\n"
            relationship += f"  -{weight}-{neighbour}"

        print(relationship)

class Graph:
    """
        Graph object defined by a set of nodes.
    """
    def __init__(self):

        self.nodes = []

    def add_nodes(self, *nodes):
        """
            Adds node/s to the graph

            Parameters
            ----------

            \*nodes
                Graph nodes to be added.
        """

        # Check if first "node" is a Node
        if(isinstance(nodes[0], Node)):
            # Therefore *nodes is being used as expected
            # Extend nodes list with *nodes tuple
            self.nodes.extend(nodes)
        else:
            # Else an iterable is being passed as nodes[0]
            self.nodes.extend(nodes[0])

    def get_node(self, id) -> Union[Node, None]:
        """
            Returns a node object in the graph based upon its ID. Returns None if not found.

            Parameters
            ----------

            id
                The ID of the node
        """
        # Loop through the nodes
        for node in self.nodes:
            # Check if name matches
            if node.id == id:
                # If so return
                return node
        # No node found so return none
        return None

    def relationships(self) -> str:
        """Prints a human readable description of the relationship between all nodes"""

        for node in self.nodes:
            node.relationships()

    def walk(self, start: Node, stop: Node = None, neighbour: int = 0, default_neighbour: int = 0) -> "Loop":
        """
            "Walks" a loop around the graph, intended for generating loops for self.loops()

            Parameters
            ----------

            start
                Node the walk starts at.
            stop
                Node the walk stops at.
            neighbour
                Initial neighbour to move to.
            default_neighbour
                Neighbour to move to on consequential moves.
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
        loop = Loop(loop)
        return loop

    def intersections(self) -> List[Node]:
        """Returns a list of nodes that have more than one connection"""
        return [node for node in self.nodes if len(node.neighbours) > 1]

    def loops(self) -> List["Loop"]:
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
                walk = self.walk(intersections[i], self.nodes[0], neighbour = j)
                if walk != None:       
                    loops.append(walk)

        return loops

class Loop(Graph):
    """
        A sub-graph structure generated by Graph.loops(), represents a distinct path around the graph.

        Parameters
        ----------

        nodes
            List of node objects that define the loop.
    """
    def __init__(self, nodes: List[Node]):

        super().__init__()
        super().add_nodes(nodes)

    def relationships(self) -> str:
        """Prints a human readable representation of the relationship between nodes"""

        relationships = f"{self.nodes[0]}"

        for i in range(1, len(self.nodes)):
            relationships += "-"
            # Only print if there is a weight
            if self.nodes[i - 1].neighbours[self.nodes[i]] != 0:
                relationships += f"{self.nodes[i - 1].neighbours[self.nodes[i]]}"
                relationships += "-"
            relationships += f"{self.nodes[i]}"

        print(relationships)

    def reorder(self, node: Node):
        """
            Reorders the loop to start at the specified node.

            Parameters
            ----------

            node
                Node to reconfigure to start at.
        """
        # If the loop does not start at the reference node
        if (node != self.nodes[0]):
            # Rearrange to be in terms of the reference node
            index = self.nodes.index(node)
            self.nodes = self.nodes[index:] + self.nodes[:index]