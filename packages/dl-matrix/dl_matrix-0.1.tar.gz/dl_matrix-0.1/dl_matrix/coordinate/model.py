from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field
from dl_matrix.coordinate.base import Coordinate


class CoordinateModel(BaseModel):
    tree: Dict[str, List[str]] = Field(
        ..., description="The tree structure representing the messages."
    )
    coordinates: Dict[str, Coordinate] = Field(
        ..., description="The coordinates representing each message."
    )

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "tree": {
                    "root": ["message1", "message2"],
                    "message1": ["message3", "message4"],
                    "message2": [],
                    "message3": [],
                    "message4": [],
                },
                "coordinates": {
                    "root": {"id": "root", "depth": {"x": 0.0}},
                    "message1": {"id": "message1", "depth": {"x": 1.0}},
                    "message2": {"id": "message2", "depth": {"x": 1.0}},
                    "message3": {"id": "message3", "depth": {"x": 2.0}},
                    "message4": {"id": "message4", "depth": {"x": 2.0}},
                },
            }
        }

    def add_coordinate(self, parent_id: str, coordinate: Coordinate):
        if parent_id not in self.coordinates:
            raise ValueError(f"No parent coordinate with id: {parent_id}")

        self.tree.setdefault(parent_id, []).append(coordinate.id)
        self.coordinates[coordinate.id] = coordinate

    def remove_coordinate(self, id: str):
        if id not in self.coordinates:
            raise ValueError(f"No coordinate with id: {id}")

        del self.coordinates[id]
        for children in self.tree.values():
            if id in children:
                children.remove(id)

    def delete_branch(self, parent_id: str):
        if parent_id not in self.tree:
            raise ValueError(f"No parent coordinate with id: {parent_id}")

        children = self.tree[parent_id]
        for child in children:
            self.delete_branch(child)

        self.remove_coordinate(parent_id)
        del self.tree[parent_id]

    def get_children(self, id: str) -> Optional[List[str]]:
        if id not in self.tree:
            raise ValueError(f"No coordinate with id: {id}")

        return self.tree.get(id, None)

    def get_coordinate(self, id: str) -> Optional[Coordinate]:
        if id not in self.coordinates:
            raise ValueError(f"No coordinate with id: {id}")

        return self.coordinates.get(id, None)

    def get_coordinates(self) -> List[Coordinate]:
        return list(self.coordinates.values())

    def get_coordinates_by_depth(self, depth: float) -> List[Coordinate]:
        return [
            coordinate
            for coordinate in self.coordinates.values()
            if coordinate.depth.x == depth
        ]

    def get_coordinates_by_sibling(self, sibling: float) -> List[Coordinate]:
        return [
            coordinate
            for coordinate in self.coordinates.values()
            if coordinate.sibling.y == sibling
        ]

    def get_coordinates_by_sibling_count(
        self, sibling_count: float
    ) -> List[Coordinate]:
        return [
            coordinate
            for coordinate in self.coordinates.values()
            if coordinate.sibling_count.z == sibling_count
        ]

    def get_coordinates_by_time(self, time: float) -> List[Coordinate]:
        return [
            coordinate
            for coordinate in self.coordinates.values()
            if coordinate.time.t == time
        ]

    def get_coordinates_by_id(self, id: str) -> List[Coordinate]:
        return [
            coordinate
            for coordinate in self.coordinates.values()
            if coordinate.id == id
        ]

    def get_coordinates_by_condition(
        self,
        depth: Optional[float] = None,
        sibling: Optional[float] = None,
        sibling_count: Optional[float] = None,
        time: Optional[float] = None,
        id: Optional[str] = None,
    ) -> List[Coordinate]:
        coordinates = self.get_coordinates()
        if depth is not None:
            coordinates = self.get_coordinates_by_depth(depth)
        if sibling is not None:
            coordinates = self.get_coordinates_by_sibling(sibling)
        if sibling_count is not None:
            coordinates = self.get_coordinates_by_sibling_count(sibling_count)
        if time is not None:
            coordinates = self.get_coordinates_by_time(time)
        if id is not None:
            coordinates = self.get_coordinates_by_id(id)
        return coordinates

    def get_coordinates_by_condition_list(
        self, condition_list: List[Dict[str, Any]]
    ) -> List[Coordinate]:
        coordinates = []
        for condition_dict in condition_list:
            coordinates.extend(self.get_coordinates_by_condition_dict(condition_dict))
        return coordinates

    @classmethod
    def get_coordinates_by_condition_dict(
        cls, condition_dict: Dict[str, Any]
    ) -> List[Coordinate]:
        return cls.get_coordinates_by_condition(**condition_dict)

    @classmethod
    def to_model(
        cls,
        root: str,
        connections: Dict[str, List[str]],
        coordinates: List[Coordinate],
        flatten: bool = False,
    ):
        """
        Create a CoordinateModel from a root, a set of connections and a list of Coordinate objects.

        Args:
            root: The root of the tree.
            connections: The connections in the tree.
            coordinates: A list of Coordinate objects.
            flatten: A flag to determine if the Coordinate objects should be flattened.

        Returns:
            An instance of CoordinateModel.
        """
        tree = Coordinate.create_tree(root, connections)
        coordinates_dict = Coordinate.list_to_dict(coordinates, flatten=flatten)
        return cls(tree=tree, coordinates=coordinates_dict)


def create_coordinate_model(
    root: str,
    connections: Dict[str, List[str]],
    coordinate_properties: List[Dict[str, Any]],
    flatten: bool = False,
) -> CoordinateModel:
    """
    Create a CoordinateModel from a root, a set of connections and a list of coordinate properties.

    Args:
        root: The root of the tree.
        connections: The connections in the tree.
        coordinate_properties: A list of dictionaries, each containing properties for a Coordinate object.
        flatten: A flag to determine if the Coordinate objects should be flattened.

    Returns:
        An instance of CoordinateModel.
    """
    coordinates = [Coordinate(**props) for props in coordinate_properties]
    return CoordinateModel.to_model(root, connections, coordinates, flatten)
