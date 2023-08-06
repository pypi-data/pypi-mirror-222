from typing import Optional, Dict, Any, List, Tuple, Union
import numpy as np
from pydantic import Field
from .base import Component


class DepthComponent(Component):
    x: float = Field(..., description="The x-coordinate of the depth component.")
    s_x: Optional[float] = Field(None, description="The scale of the x-coordinate.")
    c_x: Optional[float] = Field(None, description="The center of the x-coordinate.")

    @classmethod
    def _compute_depth_component(
        cls, sibling_coords: List[object], depth: int
    ) -> Tuple[int, float, float]:
        """
        Calculate the depth component for a given message.

        :param sibling_coords: A list of Coordinate objects representing the siblings of the current message.
        :param depth: An integer representing the depth of the current message in the conversation tree.
        :return: A tuple for the depth component of the current message.
        """
        try:
            sum_s_x = sum(coord.depth.s_x for coord in sibling_coords)

            x_coord = (
                depth,
                sum_s_x / len(sibling_coords) if sibling_coords and sum_s_x != 0 else 0,
                max(coord.depth.c_x for coord in sibling_coords)
                if sibling_coords
                else 0,
            )
            return x_coord
        except Exception as e:
            print(f"Error computing depth component: {e}")
            return 0, 0, 0

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "x": 0.0,
                "s_x": 0.0,
                "c_x": 0.0,
                "branching_factor": 0.0,
                "max_siblings": 0,
                "entropy": 0.0,
                "variance": 0.0,
                "total_children": 0,
            }
        }
