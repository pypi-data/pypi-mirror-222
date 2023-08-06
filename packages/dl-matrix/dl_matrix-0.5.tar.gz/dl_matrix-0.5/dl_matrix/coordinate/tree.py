from typing import List, Dict, Any, Optional, Callable, Tuple
from dl_matrix.coordinate.base import Coordinate
from pydantic import BaseModel


class CoordinateTree(BaseModel):
    coordinate: Coordinate
    children: List["CoordinateTree"] = []

    def __init__(self, coordinate: Dict, children: List["CoordinateTree"] = None):
        super().__init__(coordinate=coordinate, children=children or [])

    def __repr__(self):
        return f"CoordinateTree(coordinate={self.coordinate}, children={self.children})"

    def __iter__(self):
        yield self.coordinate
        for child in self.children:
            yield from child

    def classify_by_depth(self) -> Dict[float, List["CoordinateTree"]]:
        """Classify the nodes by their depth."""
        nodes_by_depth = {}
        for node in self:
            depth = node.coordinate["depth"]["x"]
            if depth not in nodes_by_depth:
                nodes_by_depth[depth] = []
            nodes_by_depth[depth].append(node)
        return nodes_by_depth

    def compute_sibling_sequences(
        self, nodes: List["CoordinateTree"]
    ) -> List[List["CoordinateTree"]]:
        """Compute sequences of uninterrupted siblings."""
        nodes.sort(key=lambda node: node.coordinate["sibling"]["y"])
        sequences = [[nodes[0]]]
        for i in range(1, len(nodes)):
            if (
                nodes[i].coordinate["sibling"]["y"]
                == nodes[i - 1].coordinate["sibling"]["y"] + 1
            ):
                sequences[-1].append(nodes[i])
            else:
                sequences.append([nodes[i]])
        return sequences

    def check_homogeneity(
        self, sequence: List["CoordinateTree"]
    ) -> List[List["CoordinateTree"]]:
        """Check homogeneity within a sequence."""
        homogeneous_groups = [[sequence[0]]]
        for i in range(1, len(sequence)):
            if (
                sequence[i].coordinate["sibling_count"]["z"]
                == sequence[i - 1].coordinate["sibling_count"]["z"]
            ):
                homogeneous_groups[-1].append(sequence[i])
            else:
                homogeneous_groups.append([sequence[i]])
        return homogeneous_groups

    def compute_group_sizes(
        self, groups: List[List["CoordinateTree"]]
    ) -> List[Tuple[int, List["CoordinateTree"]]]:
        """Compute the sizes of the groups."""
        return [(len(group), group) for group in groups]

    def find_maximus_triangle(self) -> List["CoordinateTree"]:
        """Find the Maximus Triangle."""
        nodes_by_depth = self.classify_by_depth()
        maximus_triangle = []
        max_size = 0
        for nodes in nodes_by_depth.values():
            sequences = self.compute_sibling_sequences(nodes)
            for sequence in sequences:
                homogeneous_groups = self.check_homogeneity(sequence)
                for group in homogeneous_groups:
                    size, group = self.compute_group_sizes(homogeneous_groups)
                    if size > max_size:
                        max_size = size
                        maximus_triangle = group
        return maximus_triangle

    @staticmethod
    def depth_first_search(
        tree: "CoordinateTree", predicate: Callable[[Coordinate], bool]
    ) -> Optional[Coordinate]:
        if predicate(tree.coordinate):
            return tree.coordinate
        else:
            for child in tree.children:
                result = CoordinateTree.depth_first_search(child, predicate)
                if result is not None:
                    return result
            return None

    @staticmethod
    def breadth_first_search(
        tree: "CoordinateTree", predicate: Callable[[Coordinate], bool]
    ) -> Optional[Coordinate]:
        queue = [tree]
        while queue:
            node = queue.pop(0)
            if predicate(node.coordinate):
                return node.coordinate
            else:
                queue.extend(node.children)
        return None

    @staticmethod
    def depth_first_search_all(
        tree: "CoordinateTree", predicate: Callable[[Coordinate], bool]
    ) -> List[Coordinate]:
        results = []
        if predicate(tree.coordinate):
            results.append(tree.coordinate)
        for child in tree.children:
            results.extend(CoordinateTree.depth_first_search_all(child, predicate))
        return results

    def set_coordinate(self, index: int, coordinate: Coordinate):
        self[index] = coordinate

    def distance(self, other: "CoordinateTree") -> float:
        return self.coordinate.distance(other.coordinate)


class CoordinateTreeBuilder:
    def __init__(self, coordinate: Coordinate):
        self.coordinate = coordinate
        self.children = []

    def add_child(self, child: "CoordinateTreeBuilder"):
        self.children.append(child)

    def build(self) -> CoordinateTree:
        return CoordinateTree(
            coordinate=self.coordinate,
            children=[child.build() for child in self.children],
        )

    def build_from_dict(self, d: Dict[str, Any]) -> CoordinateTree:
        return CoordinateTree(
            coordinate=self.coordinate,
            children=[child.build_from_dict(child) for child in self.children],
        )


class CoordinateTreeTraverser:
    def __init__(self, tree: CoordinateTree):
        self.tree = tree

    def traverse_depth_first(
        self, predicate: Callable[[Coordinate], bool]
    ) -> Coordinate:
        return CoordinateTree.depth_first_search(self.tree, predicate)

    def traverse_breadth_first(
        self, predicate: Callable[[Coordinate], bool]
    ) -> Coordinate:
        return CoordinateTree.breadth_first_search(self.tree, predicate)

    def traverse_depth_first_all(
        self, predicate: Callable[[Coordinate], bool]
    ) -> List[Coordinate]:
        return CoordinateTree.depth_first_search_all(self.tree, predicate)
