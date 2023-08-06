from typing import List, Tuple, Dict, Any, Callable, Optional
from utils import (
    should_connect_default,
    calculate_weight_bert_distance,
    should_connect_semantic,
    calculate_weight_sum,
)
import networkx as nx


class HyperGraphComplexCreator:
    @staticmethod
    def calculate_weight_sum(nodes: Tuple[Any, ...], _: Tuple[Any, ...]) -> int:
        """Calculate weight as the sum of node values."""
        return sum(nodes[1:])

    @staticmethod
    def should_connect_default(_: Tuple[Any, ...], __: Tuple[Any, ...]) -> bool:
        """Default connection strategy - connect all nodes."""
        return True

    @staticmethod
    def create_fully_connected_sequence(
        nodes: List[Tuple[Any, ...]],
        calculate_weight: Optional[Callable] = calculate_weight_sum,
        should_connect: Optional[Callable] = should_connect_default,
        directed: bool = True,
        multigraph: bool = False,
        self_loops: bool = False,
        node_attributes: Optional[Dict[Any, Dict[str, Any]]] = None,
        edge_attributes: Optional[Dict[Tuple[Any, Any], Dict[str, Any]]] = None,
    ) -> List[Tuple[Any, Any, int, Dict[str, Any]]]:
        """
        Takes a list of nodes and returns a sequence that represents a fully connected graph.
        """
        if not all(isinstance(node, tuple) and len(node) >= 2 for node in nodes):
            raise ValueError(
                "Each node should be a tuple with at least two elements: an identifier and one or more values."
            )

        if calculate_weight is not None and not callable(calculate_weight):
            raise ValueError(
                "If provided, calculate_weight must be a callable function that takes two nodes and returns an integer."
            )

        if should_connect is not None and not callable(should_connect):
            raise ValueError(
                "If provided, should_connect must be a callable function that takes two nodes and returns a boolean."
            )

        if not isinstance(directed, bool):
            raise ValueError("The directed argument must be a boolean value.")

        sequence_without_attributes = []
        for i in range(len(nodes)):
            start = i + 1 if not self_loops else i
            for j in range(start, len(nodes)):
                if should_connect and should_connect(nodes[i], nodes[j]):
                    weight = (
                        calculate_weight(nodes[i], nodes[j])
                        if calculate_weight
                        else None
                    )
                    edge = (nodes[i][0], nodes[j][0])
                    sequence_without_attributes.append((edge[0], edge[1], weight))

        if not multigraph:
            sequence_without_attributes = list(set(sequence_without_attributes))

        sequence = []
        for edge in sequence_without_attributes:
            edge_attr = (
                edge_attributes.get((edge[0], edge[1]), {}) if edge_attributes else {}
            )
            node_attr_1 = node_attributes.get(edge[0], {}) if node_attributes else {}
            node_attr_2 = node_attributes.get(edge[1], {}) if node_attributes else {}
            sequence.append((*edge, node_attr_1, node_attr_2, edge_attr))

        return sequence

    @staticmethod
    def create_tetrahedron_complex(
        sequence: List[Tuple[str, str]]
    ) -> Tuple[
        List[Tuple[str, str]],
        List[Tuple[str, str, str]],
        List[Tuple[str, str, str, str]],
    ]:
        # Validate input sequence
        if not sequence or not isinstance(sequence, list):
            raise ValueError("Input sequence must be a non-empty list.")

        """
        Generates a simplicial complex from the given sequence of key-value pairs and
        filters out any sub-complexes that do not form a tetrahedron.

        Args:
            sequence: A list of key-value pairs representing the input sequence.

        Returns:
            A tuple of lists, representing the edges (1-simplex), triangles (2-simplex), and tetrahedrons (3-simplex) of the simplicial complex.
        """

        # Create the simplicial complex as a list of 1-simplices (edges) by connecting adjacent vertices in the sequence.
        # In mathematical notation, for a given sequence v_1, v_2, ..., v_n, we generate the edges (v_1, v_2), (v_2, v_3), ..., (v_{n-1}, v_n).
        simplicial_complex = [
            (sequence[i][0], sequence[i + 1][0]) for i in range(len(sequence) - 1)
        ]

        simplicial_complex = list(set(simplicial_complex))

        # Initialize the lists that will hold the edges (1-simplices), triangles (2-simplices), and tetrahedrons (3-simplices) of the simplicial complex.
        edge_complex = []
        triangle_complex = []
        tetrahedron_complex = []

        # Loop over all pairs of edges in the simplicial complex to find possible tetrahedrons.
        for a, b in simplicial_complex:
            for c, d in simplicial_complex:
                # A tetrahedron is formed if all four nodes a, b, c, d are distinct, i.e., they form a 3-simplex.
                if (
                    {a, b, c, d} == set([a, b, c, d])
                    and a != b
                    and a != c
                    and a != d
                    and b != c
                    and b != d
                    and c != d
                ):
                    # If the nodes form a tetrahedron, add all six possible edges (1-simplices) among the nodes to the edge complex.
                    edge_complex.extend(
                        [(a, b), (a, c), (a, d), (b, c), (b, d), (c, d)]
                    )
                    # Also add all four possible triangles (2-simplices) to the triangle complex.
                    triangle_complex.extend(
                        [(a, b, c), (a, b, d), (a, c, d), (b, c, d)]
                    )
                    # Finally, add the tetrahedron (3-simplex) to the tetrahedron complex.
                    tetrahedron_complex.append((a, b, c, d))

        # Remove duplicate simplices from each complex to ensure they are sets, i.e., each simplex appears only once in each complex.
        edge_complex = list(set(edge_complex))
        triangle_complex = list(set(triangle_complex))
        tetrahedron_complex = list(set(tetrahedron_complex))

        # Return the edge, triangle, and tetrahedron complexes as a tuple.
        return edge_complex, triangle_complex, tetrahedron_complex


class Graph:
    """
    A class representing a graph.

    Attributes:
        nodes: A list of nodes in the graph.
        edges: A list of edges in the graph.
        directed: A boolean value indicating whether the graph is directed or undirected.
        multigraph: A boolean value indicating whether the graph is a multigraph.
        self_loops: A boolean value indicating whether the graph has self-loops.
        node_attributes: A dictionary mapping node identifiers to dictionaries of node attributes.
        edge_attributes: A dictionary mapping edge identifiers to dictionaries of edge attributes.
    """

    def __init__(
        self,
        nodes: List[Any],
        edges: List[Tuple[Any, Any, int, Dict[str, Any]]],
        directed: bool = True,
        multigraph: bool = False,
        self_loops: bool = False,
        node_attributes: Optional[Dict[Any, Dict[str, Any]]] = None,
        edge_attributes: Optional[Dict[Tuple[Any, Any], Dict[str, Any]]] = None,
    ):
        """
        Initializes a graph.

        Args:
            nodes: A list of nodes in the graph.
            edges: A list of edges in the graph.
            directed: A boolean value indicating whether the graph is directed or undirected.
            multigraph: A boolean value indicating whether the graph is a multigraph.
            self_loops: A boolean value indicating whether the graph has self-loops.
            node_attributes: A dictionary mapping node identifiers to dictionaries of node attributes.
            edge_attributes: A dictionary mapping edge identifiers to dictionaries of edge attributes.
        """
        self.nodes = nodes
        self.edges = edges
        self.directed = directed
        self.multigraph = multigraph
        self.self_loops = self_loops
        self.node_attributes = node_attributes
        self.edge_attributes = edge_attributes

    def __str__(self) -> str:
        """
        Returns a string representation of the graph.
        """
        return f"Graph(nodes={self.nodes}, edges={self.edges}, directed={self.directed}, multigraph={self.multigraph}, self_loops={self.self_loops}, node_attributes={self.node_attributes}, edge_attributes={self.edge_attributes})"

    def __repr__(self) -> str:
        """
        Returns a string representation of the graph.
        """
        return self.__str__()

    def to_networkx(self) -> nx.Graph:
        """
        Converts the graph to a NetworkX graph.

        Returns:
            A NetworkX graph.
        """
        # Initialize a NetworkX graph.
        graph = nx.Graph()

        # Add nodes to the graph.
        graph.add_nodes_from(self.nodes)

        # Add edges to the graph.
        graph.add_edges_from(self.edges)

        # Add node attributes to the graph.
        if self.node_attributes:
            nx.set_node_attributes(graph, self.node_attributes)

        # Add edge attributes to the graph.
        if self.edge_attributes:
            nx.set_edge_attributes(graph, self.edge_attributes)

        # Return the NetworkX graph.
        return graph
