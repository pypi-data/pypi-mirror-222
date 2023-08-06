from typing import Any, Dict, List, Optional, Tuple, Union, Callable
import networkx as nx
from dl_matrix.coordinate.base import (
    Coordinate,
    SiblingCountComponent,
    DepthComponent,
    SiblingComponent,
    TimeComponent,
)
from dl_matrix.structure import ChainTreeIndex, Message
from dl_matrix.relationship import Relationship
from dl_matrix.schema import DocumentRelationship


class Representation(Relationship):
    RELATIONSHIP_WEIGHTS = {
        "siblings": 1,
        "cousins": 2,
        "uncles_aunts": 3,
        "nephews_nieces": 3,
        "grandparents": 4,
        "ancestors": 5,
        "descendants": 5,
        DocumentRelationship.PARENT: 1,
        DocumentRelationship.CHILD: 1,
        DocumentRelationship.PREVIOUS: 1,
        DocumentRelationship.NEXT: 1,
        DocumentRelationship.SOURCE: 1,
    }

    def __init__(
        self,
        conversation_tree: ChainTreeIndex,
        message_dict: Dict[str, Message] = None,
        tetra_dict: Dict[str, Tuple[float, float, float, float]] = None,
        root_component_values: Dict[str, Any] = None,
    ):
        self.conversation = conversation_tree
        self.mapping = conversation_tree.conversation.mapping
        self.message_dict = message_dict
        self.tetra_dict = tetra_dict
        self.conversation_dict = self._conversation_representation()

        # Default root components
        self.default_root_component_values = {
            "depth_args": [0, 0, 0],
            "sibling_args": [0, 0],
            "sibling_count_args": [0, 0],
            "time_args": [0, 0, 0, 0],
        }

        # If root component values are provided, update the default ones
        if root_component_values:
            self.default_root_component_values.update(root_component_values)

        # Construct root coordinate with updated component values
        self.root_coordinate = Coordinate.create(**self.default_root_component_values)

    @property
    def depth(self) -> int:
        """
        Returns the maximum depth of the conversation tree.

        Returns:
            depth: The maximum depth of the conversation tree.
        """
        return self.get_message_depth(self.root_message_id)

    @property
    def root_message_id(self) -> Union[Message, None]:
        """Returns the root message of the conversation, or None if it doesn't exist."""
        for message in self.mapping.values():
            if message.parent is None:
                return self.message_dict[message.id].id if self.message_dict else None
        return None

    def _create_representation(self) -> nx.DiGraph:
        """
        Creates a NetworkX directed graph representation of the conversation tree.
        Each node in the graph is a message, and each edge indicates a response
        relationship between messages. Nodes are annotated with message content
        and authors, and edges are annotated with the response time between
        messages.
        """
        graph = nx.DiGraph()
        prev_node = None

        for mapping_id, mapping in self.mapping.items():
            if mapping.message is None:
                raise ValueError(f"Mapping {mapping_id} does not contain a message")

            # Add the node to the graph
            graph.add_node(mapping_id, **mapping.message.dict())

            # If this isn't the first node, create an edge from the previous node
            if prev_node is not None:
                graph.add_edge(prev_node, mapping_id)

            # If the mapping has a parent, create an edge from the parent
            if mapping.parent is not None:
                graph.add_edge(mapping.parent, mapping_id)

            # Add edges to all references
            for ref_id in mapping.references:
                if ref_id in self.mapping:
                    graph.add_edge(mapping_id, ref_id)

            # Update the previous node
            prev_node = mapping_id

        return graph

    def create_representation(
        self,
        node_ids: Optional[List[str]] = None,
        attribute_filter: Optional[Dict[str, Any]] = None,
    ) -> nx.DiGraph:
        """
        Creates a NetworkX directed graph representation of the conversation tree.
        Each node in the graph is a message, and each edge indicates a response
        relationship between messages. Nodes are annotated with message content
        and authors, and edges are annotated with the response time between
        messages.

        Args:
            node_ids: A list of node IDs to include in the graph.
            attribute_filter: A dictionary of attributes to filter nodes by.

        Returns:
            A NetworkX directed graph representation of the conversation tree.

        """
        # Get the full graph representation
        graph = self._create_representation()

        # If node_ids are provided, use them to create the subgraph
        if node_ids is not None:
            subgraph = graph.subgraph(node_ids)

        # If attribute_filter is provided, select nodes based on attributes
        elif attribute_filter is not None:
            selected_nodes = [
                node
                for node, data in graph.nodes(data=True)
                if all(item in data.items() for item in attribute_filter.items())
            ]
            subgraph = graph.subgraph(selected_nodes)
        # If neither are provided, return the full graph
        else:
            subgraph = graph

        return subgraph

    def initialize_representation(
        self,
        use_graph: bool = False,
        node_ids: Optional[List[str]] = None,
        attribute_filter: Optional[Dict[str, Any]] = None,
        RELATIONSHIP_TYPE=DocumentRelationship,
    ) -> Tuple[str, Callable]:
        """
        This method initializes the graph for the conversation. It either creates the conversation graph or uses the provided graph.

        :param use_graph: A boolean indicating whether to create a new conversation graph or use the existing one.
        :return: The root ID of the graph as a string, and a function to get the children IDs for a given node.
        """
        relationships = {}

        if use_graph:
            # Create the conversation graph
            G = self.create_representation(
                node_ids=node_ids, attribute_filter=attribute_filter
            )
            if G.number_of_nodes() == 0:
                return "", None

            # Get the root node
            root_id = list(nx.topological_sort(G))[0]

            # Get the children IDs for a given node
            get_children_ids = lambda node_id: list(G.successors(node_id))

            # Get the tetra dict
            relationships[root_id] = {RELATIONSHIP_TYPE.SOURCE: root_id}

        else:
            if len(self.conversation_dict) == 0:
                return "", None

            root_id = list(self.conversation_dict)[0]
            get_children_ids = self.get_children_ids
            relationships[root_id] = {RELATIONSHIP_TYPE.SOURCE: root_id}

        tetra_dict = {}
        tetra_dict[root_id] = self.root_coordinate.flatten(self.root_coordinate)

        return (
            relationships,
            get_children_ids,
            tetra_dict,
            root_id,
            self.root_coordinate,
        )

    def _assign_relationships(
        self,
        message_id: str,
        child_id: str,
        children_ids: List[str],
        i: int,
        relationships: Dict[str, Dict[str, str]],
        RELATIONSHIP_TYPE=DocumentRelationship,
    ) -> Dict[str, Dict[str, str]]:
        relationships[child_id] = {
            RELATIONSHIP_TYPE.PARENT: message_id,
            RELATIONSHIP_TYPE.CHILD: [],
            RELATIONSHIP_TYPE.PREVIOUS: children_ids[i - 1] if i > 0 else None,
            RELATIONSHIP_TYPE.NEXT: children_ids[i + 1]
            if i < len(children_ids) - 1
            else None,
        }
        return relationships

    def _sibling_graph(self, children_ids: List[str]) -> nx.Graph:
        """
        Creates a graph from the sibling relationships of a given message.
        """
        G = nx.Graph()
        G.add_nodes_from(children_ids)
        for child_id in children_ids:
            siblings = self._get_message_siblings(child_id)
            for sibling in siblings:
                G.add_edge(child_id, sibling.id)
        return G

    def _assign_coordinates(self, child_id, i, children_ids, sibling_coords, depth):
        message = self.message_dict[child_id]
        if not message:
            raise ValueError(f"Message {child_id} not found in message_dict")

        descendants_count = sum(1 for _ in self._get_message_descendants(child_id))

        depth_args = DepthComponent._compute_depth_component(sibling_coords, depth)
        sibling_args = SiblingComponent._compute_sibling_component(sibling_coords, i)
        sibling_count_args = SiblingCountComponent._compute_sibling_count_component(
            children_ids, descendants_count, self._get_message_siblings
        )

        time_args = TimeComponent._compute_time_component(
            message, self.message_dict, children_ids
        )

        child_coordinate = Coordinate.create(
            depth_args, sibling_args, sibling_count_args, time_args
        )
        flattened_child_coordinate = child_coordinate.flatten(child_coordinate)

        return flattened_child_coordinate

    def get_message_content(self, message_id: str) -> str:
        """
        Get the content of a message with a given id.

        Args:
            message_id: The id of the message.

        Returns:
            The content of the message.
        """
        return self.message_dict[message_id].message.content.text

    def get_message_author_role(self, message_id: str) -> str:
        """
        Get the author role of a message with a given id.

        Args:
            message_id: The id of the message.

        Returns:
            The author role of the message.
        """
        return self.message_dict[message_id].message.author.role

    def get_message_create_time(self, message_id: str) -> str:
        """
        Get the creation time of a message with a given id.

        Args:
            message_id: The id of the message.

        Returns:
            The creation time of the message.
        """
        return self.message_dict[message_id].message.create_time
