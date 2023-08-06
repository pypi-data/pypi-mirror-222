from typing import Optional, Dict, Any, List, Tuple, Union
from jax import numpy as jnp
from pydantic import BaseModel, Field
from uuid import uuid4
from .components import (
    DepthComponent,
    SiblingComponent,
    SiblingCountComponent,
    TimeComponent,
)
import numpy as np
import networkx as nx
import torch
import jax.numpy as jnp


class Coordinate(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

    parent: Optional[str] = Field(None, description="The ID of the parent Coordinate.")

    depth: Optional[DepthComponent] = Field(
        None, description="The depth component of the coordinate."
    )
    sibling: Optional[SiblingComponent] = Field(
        None, description="The sibling component of the coordinate."
    )
    sibling_count: Optional[SiblingCountComponent] = Field(
        None, description="The sibling count component of the coordinate."
    )
    time: Optional[TimeComponent] = Field(
        None, description="The time component of the coordinate."
    )

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "id": "Coordinate1",
                "depth": {
                    "x": 0.0,
                    "s_x": 0.0,
                    "c_x": 0.0,
                    "branching_factor": 0.0,
                    "max_siblings": 0,
                    "entropy": 0.0,
                    "variance": 0.0,
                    "total_children": 0,
                },
                "sibling": {
                    "y": 0.0,
                    "a_y": 0.0,
                    "response_time": 0.0,
                    "total_interaction": 0.0,
                },
                "sibling_count": {
                    "z": 0.0,
                    "m_z": 0.0,
                    "avg_length": 50.0,
                    "reply_rate": 30.0,  # in seconds
                },
                "time": {
                    "t": 0.0,
                    "p_y": 0.0,
                    "p_w": 0.0,
                    "response_time": 0.0,
                },
            }
        }

    @classmethod
    def create(
        cls,
        depth_args: list = [],
        sibling_args: list = [],
        sibling_count_args: list = [],
        time_args: list = [],
    ):
        depth = DepthComponent.create(*depth_args) if depth_args else None
        sibling = SiblingComponent.create(*sibling_args) if sibling_args else None
        sibling_count = (
            SiblingCountComponent.create(*sibling_count_args)
            if sibling_count_args
            else None
        )
        time = TimeComponent.create(*time_args) if time_args else None

        return cls(
            depth=depth,
            sibling=sibling,
            sibling_count=sibling_count,
            time=time,
        )

    @staticmethod
    def flatten(coordinate: "Coordinate"):
        values = [
            coordinate.depth.x,
            coordinate.depth.s_x if coordinate.depth.s_x is not None else 0,
            coordinate.depth.c_x if coordinate.depth.c_x is not None else 0,
            coordinate.sibling.y,
            coordinate.sibling.a_y if coordinate.sibling.a_y is not None else 0,
            coordinate.sibling_count.z,
            coordinate.sibling_count.m_z
            if coordinate.sibling_count.m_z is not None
            else 0,
            coordinate.time.t,
            coordinate.time.p_y if coordinate.time.p_y is not None else 0,
        ]
        return np.array(values)

    @staticmethod
    def flatten_list(coordinates: List["Coordinate"]):
        return np.array([Coordinate.flatten(c) for c in coordinates])

    @staticmethod
    def get_coordinate_names():
        return [
            "depth_x",
            "depth_s_x",
            "depth_c_x",
            "sibling_y",
            "sibling_a_y",
            "sibling_count_z",
            "sibling_count_m_z",
            "time_t",
            "time_p_y",
        ]

    @staticmethod
    def unflatten(values: np.ndarray):
        return Coordinate(
            depth=DepthComponent.create(*values[:3]),
            sibling=SiblingComponent.create(*values[3:5]),
            sibling_count=SiblingCountComponent.create(*values[5:7]),
            time=TimeComponent.create(*values[7:]),
        )

    @staticmethod
    def flatten_list(coordinates: List["Coordinate"]):
        return np.array([Coordinate.flatten(c) for c in coordinates])

    @staticmethod
    def unflatten_list(values: np.ndarray):
        return [Coordinate.unflatten(v) for v in values]

    @staticmethod
    def flatten_list_of_lists(coordinates: List[List["Coordinate"]]):
        return np.array([[Coordinate.flatten(c) for c in cs] for cs in coordinates])

    @staticmethod
    def unflatten_list_of_lists(values: np.ndarray):
        return [[Coordinate.unflatten(v) for v in vs] for vs in values]

    @staticmethod
    def coordinate_to_string(coordinate: "Coordinate") -> str:
        """
        Convert a Coordinate object into a string.

        Args:
            coordinate: The Coordinate object.

        Returns:
            A string representing the Coordinate object.
        """
        flattened_coordinate = Coordinate.flatten(coordinate)

        # Convert the flattened coordinate to a string
        str_coordinate = np.array2string(flattened_coordinate, separator=",")

        return str_coordinate

    @staticmethod
    def string_to_coordinate(coordinate_str: str) -> "Coordinate":
        """
        Convert a string into a Coordinate object.

        Args:
            coordinate_str: The string representation of the Coordinate object.

        Returns:
            A Coordinate object.
        """
        # Convert string to numpy array
        coordinate_arr = np.fromstring(coordinate_str, sep=",")

        # Unflatten the array to get the coordinate values
        coordinate_values = Coordinate.unflatten(coordinate_arr)

        # Create coordinate object
        coordinate = Coordinate.create(*coordinate_values)

        return coordinate

    @classmethod
    def from_tuple(clx, data: Dict[str, Any]) -> "Coordinate":
        pass

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Coordinate":
        """
        Creates a Coordinate instance from a dictionary.

        Args:
            data: The dictionary to create the Coordinate instance from.

        Returns:
            A Coordinate instance.
        """
        return cls(**data)

    @staticmethod
    def stack_coordinates(
        coordinates_dict: Dict[str, Union["Coordinate", np.array]]
    ) -> np.array:
        """
        Extract the flattened Coordinate arrays from the dictionary and stack them into a 2D array.

        Args:
            coordinates_dict: The dictionary of Coordinate objects or flattened Coordinate arrays.

        Returns:
            A 2D numpy array containing the flattened representations of the Coordinate objects or arrays in the dictionary.
        """
        return np.stack(list(coordinates_dict.values()), axis=0)

    @staticmethod
    def to_tensor(
        coordinates_dict: Dict[str, Union["Coordinate", np.array]]
    ) -> torch.Tensor:
        """
        Converts a dictionary of Coordinate objects or flattened Coordinate arrays into a PyTorch tensor.

        Args:
            coordinates_dict: The dictionary of Coordinate objects or flattened Coordinate arrays.

        Returns:
            A PyTorch tensor representation of the Coordinate objects or their flattened representations in the dictionary.
        """
        # Use the helper method to stack the Coordinate arrays into a 2D array.
        coordinates_array = Coordinate.stack_coordinates(coordinates_dict)

        # Convert the 2D array to a PyTorch tensor.
        coordinates_tensor = torch.tensor(coordinates_array, dtype=torch.float32)

        return coordinates_tensor

    @staticmethod
    def to_jax(coordinates_dict: Dict[str, Union["Coordinate", np.array]]) -> jnp.array:
        """
        Converts a dictionary of Coordinate objects or flattened Coordinate arrays into a JAX tensor.

        Args:
            coordinates_dict: The dictionary of Coordinate objects or flattened Coordinate arrays.

        Returns:
            A JAX tensor representation of the Coordinate objects or their flattened representations in the dictionary.
        """
        # Use the helper method to stack the Coordinate arrays into a 2D array.
        coordinates_array = Coordinate.stack_coordinates(coordinates_dict)

        # Convert the 2D array to a JAX tensor.
        coordinates_tensor = jnp.array(coordinates_array)

        return coordinates_tensor

    @staticmethod
    def from_tensor(coordinates_tensor: torch.Tensor) -> Dict[str, "Coordinate"]:
        """
        Converts a PyTorch tensor into a dictionary of Coordinate objects.

        Args:
            coordinates_tensor: The PyTorch tensor to convert.

        Returns:
            A dictionary of Coordinate objects.
        """
        # Convert the PyTorch tensor to a numpy array.
        coordinates_array = coordinates_tensor.numpy()

        # Convert the numpy array to a dictionary of Coordinate objects.
        coordinates_dict = Coordinate.from_array(coordinates_array)

        return coordinates_dict

    @staticmethod
    def from_jax(coordinates_tensor: jnp.array) -> Dict[str, "Coordinate"]:
        """
        Converts a JAX tensor into a dictionary of Coordinate objects.

        Args:
            coordinates_tensor: The JAX tensor to convert.

        Returns:
            A dictionary of Coordinate objects.
        """
        # Convert the JAX tensor to a numpy array.
        coordinates_array = coordinates_tensor.numpy()

        # Convert the numpy array to a dictionary of Coordinate objects.
        coordinates_dict = Coordinate.from_array(coordinates_array)

        return coordinates_dict

    @staticmethod
    def from_array(coordinates_array: np.array) -> Dict[str, "Coordinate"]:
        """
        Converts a numpy array into a dictionary of Coordinate objects.

        Args:
            coordinates_array: The numpy array to convert.

        Returns:
            A dictionary of Coordinate objects.
        """
        # Convert the numpy array to a list of Coordinate objects.
        coordinates_list = Coordinate.from_list(coordinates_array)

        # Convert the list of Coordinate objects to a dictionary.
        coordinates_dict = Coordinate.from_list(coordinates_list)

        return coordinates_dict

    @staticmethod
    def from_list(coordinates_list: List["Coordinate"]) -> Dict[str, "Coordinate"]:
        """
        Converts a list of Coordinate objects into a dictionary.

        Args:
            coordinates_list: The list of Coordinate objects.

        Returns:
            A dictionary where the keys are the IDs of the Coordinate objects and the values are the Coordinate objects.
        """
        return {coordinate.id: coordinate for coordinate in coordinates_list}

    @staticmethod
    def from_tensor_to_jax(coordinates_tensor: torch.Tensor) -> jnp.array:
        """
        Converts a PyTorch tensor into a JAX tensor.

        Args:
            coordinates_tensor: The PyTorch tensor to convert.

        Returns:
            A JAX tensor representation of the PyTorch tensor.
        """
        # Convert the PyTorch tensor to a numpy array.
        coordinates_array = coordinates_tensor.numpy()

        # Convert the numpy array to a JAX tensor.
        coordinates_tensor = jnp.array(coordinates_array)

        return coordinates_tensor

    @staticmethod
    def tree_flatten(
        coordinates_dict: Dict[str, "Coordinate"]
    ) -> Tuple[List[np.ndarray], List[Tuple[Any, ...]]]:
        """
        Flattens a dictionary of Coordinate objects.

        Args:
            coordinates_dict: The dictionary of Coordinate objects.

        Returns:
            A tuple containing a list of flattened Coordinate numpy arrays and a list of auxiliary data needed for unflattening.
        """
        # Get the list of Coordinate objects from the dictionary.
        coordinates_list = list(coordinates_dict.values())

        # Flatten the Coordinate objects.
        flattened_coordinates_list = [
            Coordinate.flatten(coord) for coord in coordinates_list
        ]

        # The auxiliary data needed for unflattening is the keys of the original dictionary.
        aux_data = list(coordinates_dict.keys())

        return flattened_coordinates_list, aux_data

    @staticmethod
    def tree_unflatten(
        flattened_coordinates_list: List[np.ndarray], aux_data: List[Any]
    ) -> Dict[str, "Coordinate"]:
        """
        Unflattens a list of flattened Coordinate numpy arrays.

        Args:
            flattened_coordinates_list: The list of flattened Coordinate numpy arrays.
            aux_data: The auxiliary data needed for unflattening (keys of the original dictionary).

        Returns:
            A dictionary of Coordinate objects.
        """
        # Unflatten the Coordinate numpy arrays.
        coordinates_list = [
            Coordinate.unflatten(coord) for coord in flattened_coordinates_list
        ]

        # Convert the list of Coordinate objects to a dictionary.
        coordinates_dict = dict(zip(aux_data, coordinates_list))

        return coordinates_dict

    @staticmethod
    def create_tree(
        root: str, connections: Dict[str, List[str]]
    ) -> Dict[str, List[str]]:
        """
        Creates a tree structure.

        Args:
            root (str): The root node.
            connections (Dict[str, List[str]]): Dictionary representing the connections between nodes.

        Returns:
            Dict[str, List[str]]: A tree structure.
        """
        tree = {root: []}

        for parent, children in connections.items():
            tree[parent] = children
            for child in children:
                if child not in tree:
                    tree[child] = []

        return tree

    @staticmethod
    def list_to_dict(
        coordinates: List["Coordinate"], flatten: bool = False
    ) -> Dict[str, Union["Coordinate", np.array]]:
        """
        Convert a list of Coordinate objects into a dictionary.

        Args:
            coordinates: The list of Coordinate objects.
            flatten: A flag to determine if the Coordinate objects should be flattened.

        Returns:
            A dictionary where the keys are the IDs of the Coordinate objects and the values are the Coordinate objects
            or their flattened representations.
        """
        if flatten:
            return {
                coordinate.id: Coordinate.flatten(coordinate)
                for coordinate in coordinates
            }
        else:
            return {coordinate.id: coordinate for coordinate in coordinates}

    @staticmethod
    def create_graph(
        root: str,
        connections: Dict[str, List[str]],
        coordinates: List["Coordinate"],
        edges: Optional[List[Tuple[str, str, float]]] = None,
        labels: Optional[Dict[str, str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        depth: Optional[Dict[str, Any]] = None,
        siblings: Optional[Dict[str, Any]] = None,
    ) -> nx.Graph:
        """
        Creates a NetworkX graph.

        Args:
            root (str): The root node.
            connections (Dict[str, List[str]]): Dictionary representing the connections between nodes.
            coordinates: The list of Coordinate objects.
            edges: A list of edges between the coordinates. Each edge is represented as a tuple (node1, node2, weight).
            labels: A dictionary with node labels.
            metadata: A dictionary with additional metadata for each node.
            depth: A dictionary with depth information for each node.
            siblings: A dictionary with siblings information for each node.

        Returns:
            A NetworkX graph.
        """
        # Create tree
        tree = Coordinate.create_tree(root, connections)

        graph = Coordinate.flatten_coordinates_to_graph(
            coordinates, edges, labels, metadata, depth, siblings
        )
        return graph, tree

    @classmethod
    def flatten_coordinates_to_graph(
        cls,
        coordinates: List["Coordinate"],
        edges: Optional[List[Tuple[str, str, float]]] = None,
        labels: Optional[Dict[str, str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        depth: Optional[Dict[str, Any]] = None,
        siblings: Optional[Dict[str, Any]] = None,
    ) -> nx.Graph:
        """
        Flatten a list of coordinates and adds each as a node to a NetworkX graph.
        Adds edges, labels, metadata, depth and siblings information between the nodes in the graph.

        Args:
            coordinates: A list of coordinates.
            edges: A list of edges between the coordinates. Each edge is represented as a tuple (node1, node2, weight).
            labels: A dictionary with node labels.
            metadata: A dictionary with additional metadata for each node.
            depth: A dictionary with depth information for each node.
            siblings: A dictionary with siblings information for each node.

        Returns:
            A NetworkX graph with the flattened coordinates as nodes and edges, labels, metadata, depth and siblings information between the nodes.
        """
        # Create graph
        graph = nx.Graph()

        # Add nodes from the flattened coordinates
        for coordinate in coordinates:
            graph.add_node(coordinate.id, coordinate=coordinate)

        # Add edges
        if edges:
            graph.add_weighted_edges_from(edges)

        # Add labels
        if labels:
            nx.set_node_attributes(graph, labels, "label")

        # Add metadata
        if metadata:
            nx.set_node_attributes(graph, metadata, "metadata")

        # Add depth
        if depth:
            nx.set_node_attributes(graph, depth, "depth")

        # Add siblings
        if siblings:
            nx.set_node_attributes(graph, siblings, "siblings")

        return graph

    @staticmethod
    def get_coordinates_from_graph(
        graph: nx.Graph, flatten: bool = False
    ) -> Dict[str, Union["Coordinate", np.array]]:
        """
        Extracts the coordinates from a NetworkX graph.

        Args:
            graph: The NetworkX graph.
            flatten: A flag to determine if the Coordinate objects should be flattened.

        Returns:
            A dictionary where the keys are the IDs of the Coordinate objects and the values are the Coordinate objects
            or their flattened representations.
        """
        coordinates = nx.get_node_attributes(graph, "coordinate")

        if flatten:
            return {
                coordinate.id: Coordinate.flatten(coordinate)
                for coordinate in coordinates.values()
            }
        else:
            return coordinates

    @staticmethod
    def get_edges_from_graph(graph: nx.Graph) -> List[Tuple[str, str, float]]:
        """
        Extracts the edges from a NetworkX graph.

        Args:
            graph: The NetworkX graph.

        Returns:
            A list of edges between the coordinates. Each edge is represented as a tuple (node1, node2, weight).
        """
        return list(graph.edges.data("weight"))
