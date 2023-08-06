from pydantic import BaseModel
from typing import Any, Dict, Optional, List, Union
from .author import Author
from .metadata import Metadata
from .content import Content
from .connection import Connection
from pydantic import BaseModel, Field
from uuid import uuid4
from dl_matrix.schema import DocumentRelationship

Data = Union[Dict[str, Any], List[Dict[str, Any]]]


class Message(BaseModel):
    """
    Represents a message in the conversation.
    Attributes:
        id (str): Unique identifier for the message.
        create_time (float): The timestamp for when the message was created.
        author (Optional[Author]): The author of the message, if applicable.
        metadata (Optional[Metadata]): Metadata associated with the message.
        content (Content): The content of the message.
        end_turn (Optional[bool]): Whether the message ends the current turn in the conversation.
        weight (int): A weight for the message's importance or relevance.
        recipient (Optional[str]): The recipient of the message, if applicable.
        relationships (Dict[DocumentRelationship, str]): Relationships associated with the message.
        connections (Dict[str, Connection]): Connections associated with the message.

    """

    id: str = Field(default_factory=lambda: str(uuid4()))

    author: Optional[Author] = Field(
        None, description="The author of the message, if applicable."
    )

    content: Content = Field(..., description="The content of the message.")

    create_time: float = Field(
        None, description="The timestamp for when the message was created."
    )

    end_turn: Optional[bool] = Field(
        None,
        description="Whether the message ends the current turn in the conversation.",
    )

    weight: int = Field(
        1, description="A weight for the message's importance or relevance."
    )

    metadata: Optional[Metadata] = Field(
        None, description="Metadata associated with the message."
    )

    recipient: Optional[str] = Field(
        None, description="The recipient of the message, if applicable."
    )

    relationships: Dict[DocumentRelationship, str] = Field(
        None,
        description="Relationships associated with the message.",
    )

    connections: Dict[str, Connection] = Field(
        None,
        description="Connections associated with the message.",
    )

    def __init__(self, **data: Any):
        super().__init__(**data)
        if self.content is None:
            self.content = Content()
        if self.metadata is None:
            self.metadata = Metadata()
        if self.author is None:
            self.author = Author()

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "id": "Message1",
                "author": {"role": "Role.USER", "metadata": {}},
                "create_time": 1234567890,
                "content": {
                    "content_type": "text",
                    "parts": ["Hello World!"],
                },
                "end_turn": False,
                "weight": 1,
                "metadata": {"key": "value"},
                "recipient": "Node1",
                "relationships": {
                    "NEXT": "Message2",
                    "PREVIOUS": "Message0",
                    "SOURCE": "Node1",
                    "PARENT": "Node1",
                    "CHILD": "Message2",
                },
            }
        }

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the Message instance to a dictionary.
        Returns:
            A dictionary.
        """
        return {
            "id": self.id,
            "create_time": self.create_time,
            "end_turn": self.end_turn,
            "weight": self.weight,
            "metadata": self.metadata.dict() if self.metadata else None,
            "recipient": self.recipient,
            "content": self.content.dict(),
            "author": self.author.dict() if self.author else None,
        }


# Q: How to
