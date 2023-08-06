from typing import Dict, Any, Optional, List, Tuple, Union
from enum import Enum
from pydantic import BaseModel, Field, root_validator


class ModerationStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    REJECTED_AND_NOTIFIED = "rejected_and_notified"


class ModerationResult(BaseModel):

    """
    Represents a moderation result.

    Attributes:
        id (str): The ID of the moderation result.
        status (ModerationStatus): The status of the moderation result.
        moderator_id (str): The ID of the moderator.
        notes (str): The notes of the moderation result.

    """

    id: str = Field(..., description="The ID of the moderation result.")
    status: Optional[ModerationStatus] = Field(
        None, description="The status of the moderation result."
    )

    moderator_id: Optional[str] = Field(None, description="The ID of the moderator.")

    notes: Optional[str] = Field(
        None, description="The notes of the moderation result."
    )

    @root_validator(pre=True)
    def check_status(cls, values):
        status = values.get("status")
        if status is None:
            values["status"] = ModerationStatus.PENDING
        return values

    def __str__(self):
        return f"{self.id} ({self.status})"

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the ModerationResult instance to a dictionary.

        Returns:
            A dictionary.
        """
        return {
            "id": self.id,
            "status": self.status,
            "moderator_id": self.moderator_id,
            "notes": self.notes,
        }
