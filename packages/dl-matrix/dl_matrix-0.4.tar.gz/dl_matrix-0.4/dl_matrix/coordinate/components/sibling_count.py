from typing import Optional, List, Dict, Any, Callable
from pydantic import Field
from .base import Component
from uuid import uuid4


class SiblingCountComponent(Component):
    z: float = Field(
        ..., description="The z-coordinate of the sibling count component."
    )
    m_z: Optional[Any] = Field(
        None, description="The maximum z-coordinate of the sibling count component."
    )

    avg_length: Optional[float] = Field(
        None, description="The average length of the sibling count component."
    )

    reply_rate: Optional[float] = Field(
        None, description="The reply rate of the sibling count component."
    )

    @classmethod
    def _compute_sibling_count_component(
        cls,
        children_ids: List[str],
        descendants_count: int,
        _get_message_siblings: Callable[[str], List[Dict[str, Any]]],
    ):
        try:
            z_coord = (
                0 if len(children_ids) == 1 else -0.5 * (len(children_ids) - 1),
                max(
                    sum(1 for _ in _get_message_siblings(sibling_id))
                    * descendants_count
                    for sibling_id in children_ids
                )
                if children_ids
                else 0,
            )
            return z_coord
        except Exception as e:
            print(f"Error computing sibling count component: {e}")
            return 0, 0

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "z": 0.0,
                "m_z": 0.0,
            }
        }
