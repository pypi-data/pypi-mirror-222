from typing import Any, Dict, Optional
from pydantic import (
    BaseModel,
    Field,
    constr,
    HttpUrl,
)
from enum import Enum
from datetime import datetime
from .types import ConnectionType


class ConnectionDetails(BaseModel):
    target_message_id: constr(min_length=1) = Field(
        ...,
        description="Unique ID of the message that this message is connected to. "
        "It should not be an empty string or contain only whitespaces.",
    )
    timestamp: Optional[datetime] = Field(
        None, description="The timestamp when this connection was made."
    )
    author: Optional[str] = Field(
        None, description="Author of the message that established this connection."
    )
    context_url: Optional[HttpUrl] = Field(
        None,
        description="A URL to provide additional context or source for the connection.",
    )
    connection_weight: float = (
        1.0  # default weight, it can be updated based on the logic
    )

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "target_message_id": "Message1",
                "timestamp": "2023-06-30T13:45:00",
                "author": "User1",
                "context_url": "http://example.com/context1",
            }
        }


class ConnectionTier(BaseModel):
    tier1: Dict[str, ConnectionDetails] = {}
    tier2: Dict[str, ConnectionDetails] = {}
    tier3: Dict[str, ConnectionDetails] = {}

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "tier1": {
                    "target_message_id": "Message1",
                    "timestamp": "2023-06-30T13:45:00",
                    "author": "User1",
                    "context_url": "http://example.com/context1",
                },
                "tier2": {
                    "target_message_id": "Message2",
                    "timestamp": "2023-06-30T13:50:00",
                    "author": "User2",
                    "context_url": "http://example.com/context2",
                },
                "tier3": {
                    "target_message_id": "Message3",
                    "timestamp": "2023-06-30T13:55:00",
                    "author": "User3",
                    "context_url": "http://example.com/context3",
                },
            }
        }


class Connection(BaseModel):
    """A connection between two messages."""

    connection_type: ConnectionType = Field(
        ...,
        description="The type of connection (reply, mention, quote, etc.)",
    )

    connection_details: ConnectionDetails = Field(
        ...,
        description="The details of the connection (target_message_id, timestamp, author, context_url)",
    )

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "connection_type": "REPLY_TO",
                "connection_details": {
                    "target_message_id": "Message1",
                    "timestamp": "2023-06-30T13:45:00",
                    "author": "User1",
                    "context_url": "http://example.com/context1",
                },
            }
        }
