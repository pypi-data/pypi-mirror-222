from pydantic import BaseModel
import json
from typing import Dict, Any, Optional, List, Type, Union
from pydantic.fields import Field
from enum import Enum
from .types import RoleType
from .author import Author


class User(Author):
    role = RoleType.USER


class Assistant(Author):
    role = RoleType.ASSISTANT


class System(Author):
    role = RoleType.SYSTEM


class Admin(Author):
    role = RoleType.ADMIN


class Guest(Author):
    role = RoleType.GUEST


class Anonymous(Author):
    role = RoleType.ANONYMOUS


class Moderator(Author):
    role = RoleType.MODERATOR


class Owner(Author):
    role = RoleType.OWNER


class Developer(Author):
    role = RoleType.DEVELOPER


class Creator(Author):
    role = RoleType.CREATOR


class Chat(Author):
    role = RoleType.CHAT


class AuthorList(BaseModel):
    """
    Represents a list of authors.
    """

    authors: List[Author] = Field(..., description="The list of authors.", min_items=1)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "authors": [
                    {
                        "role": "user",
                        "id": "123456789",
                        "entity_name": "John Doe",
                        "description": "The user of the conversation. This is the default role.",
                        "metadata": {},
                    }
                ]
            }
        }

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        self.authors = self.authors or []

    def to_dict(self) -> Dict[str, Any]:
        return self.dict(exclude_none=True)

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
