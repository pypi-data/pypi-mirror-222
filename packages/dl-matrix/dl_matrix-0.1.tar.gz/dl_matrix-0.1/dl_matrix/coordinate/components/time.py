from typing import Optional, List, Dict, Any, Callable, Tuple
from pydantic import Field
from .base import Component
import numpy as np


class TimeComponent(Component):
    t: Any = Field(..., description="The t-coordinate of the time component.")
    p_y: Optional[Any] = Field(None, description="The phase of the y-coordinate.")
    p_w: Optional[Any] = Field(None, description="The weight of the part.")
    response_time: Optional[Any] = Field(
        None, description="Response time for the message."
    )

    @classmethod
    def _compute_time_component(
        cls,
        message: object,
        message_dict,
        children_ids,
        calc_p_y: bool = True,
        calc_response_time: bool = True,
    ):
        if not message or not message_dict or not children_ids:
            return None

        text_parts = (
            message.message.content.text.split("\n\n")
            if message.message.content.text
            else []
        )
        n_parts = len(text_parts)
        part_weight = round(1.0 / n_parts, 2) if n_parts > 0 else 0
        part_weight = np.log(part_weight) if part_weight > 0 else 0

        sibling_time_differences = cls.calculate_t_coordinate(
            message, message_dict, children_ids
        )
        t = sibling_time_differences * (part_weight if part_weight else 1)

        p_y = len(text_parts) if calc_p_y else None
        response_time = (
            cls.calculate_response_time(message_dict, children_ids)
            if calc_response_time
            else None
        )

        return t, p_y, part_weight, response_time

    @staticmethod
    def calculate_response_time(message_dict, children_ids):
        if len(children_ids) < 2:
            return None
        current_timestamp = message_dict[children_ids[-1]].message.create_time
        previous_timestamp = message_dict[children_ids[-2]].message.create_time
        response_time = current_timestamp - previous_timestamp
        return response_time

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "t": 0.0,
                "p_y": 0.0,
                "p_w": 0.0,
                "response_time": 0.0,
            }
        }
