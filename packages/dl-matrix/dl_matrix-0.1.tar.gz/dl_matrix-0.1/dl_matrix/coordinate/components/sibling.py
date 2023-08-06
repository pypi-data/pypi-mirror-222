from typing import Optional, List, Dict, Any, Callable, Tuple
from pydantic import Field
from .base import Component


class SiblingComponent(Component):
    y: float = Field(..., description="The y-coordinate of the sibling component.")
    a_y: Optional[float] = Field(None, description="The amplitude of the y-coordinate.")

    @classmethod
    def _compute_sibling_component(
        cls, sibling_coords: List[object], i: int
    ) -> Tuple[int, float]:
        """
        Calculate the sibling component for a given message.

        :param sibling_coords: A list of Coordinate objects representing the siblings of the current message.
        :param i: The index of the current message among its siblings.
        :return: A tuple for the sibling component of the current message.
        """
        try:
            sum_y_s_x = sum(
                coord.sibling.y * coord.depth.s_x for coord in sibling_coords
            )
            y_coord = (
                i + 1,
                (sum_y_s_x / sum_y_s_x + 1) if sibling_coords and sum_y_s_x != 0 else 1,
            )
            return y_coord
        except Exception as e:
            print(f"Error computing sibling component: {e}")
            return 0, 0

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "y": 0.0,
                "a_y": 0.0,
            }
        }
