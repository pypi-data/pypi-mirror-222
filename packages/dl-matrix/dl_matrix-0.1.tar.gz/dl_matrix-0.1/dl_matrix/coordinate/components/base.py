from typing import Dict, Any
import numpy as np
from pydantic import BaseModel, Field


class Component(BaseModel):
    @classmethod
    def create(cls, *args):
        fields = cls.__annotations__.keys()
        kwargs = {f: arg for f, arg in zip(fields, args)}
        return cls(**kwargs)

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Component":
        return cls(**d)

    def to_dict(self) -> Dict[str, Any]:
        return self.dict()

    @classmethod
    def from_tuple(cls, tup: tuple) -> "Component":
        return cls(*tup)

    def tuple(self) -> tuple:
        return tuple(self.dict().values())

    def __eq__(self, other):
        return self.dict() == other.dict()

    @staticmethod
    def calculate_t_coordinate(message, message_dict, children_ids) -> float:
        sibling_time_differences = [
            message_dict[child_id].message.create_time - message.message.create_time
            for child_id in children_ids
        ]
        return np.mean(sibling_time_differences)

    @staticmethod
    def flattened_to_string(coordinate: np.ndarray) -> str:
        """
        Converts a flattened coordinate to a string format.

        Args:
            coordinate: The flattened coordinate represented as a numpy array.

        Returns:
            A string representation of the coordinate.
        """
        return np.array2string(coordinate, separator=",")

    @staticmethod
    def string_to_flattened(coordinate: str) -> np.ndarray:
        """
        Converts a string coordinate to a flattened numpy array.

        Args:
            coordinate: The string representation of the coordinate.

        Returns:
            A flattened numpy array.
        """
        return np.fromstring(coordinate[1:-1], sep=",")
