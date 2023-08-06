from typing import Any, Dict, List, Optional
from .mapping import ChainMap
from pydantic import BaseModel, Field
from uuid import uuid4
from enum import Enum
import pandas as pd


class ChainTreeType(str, Enum):
    """
    Represents the type of conversation tree.
    """

    FULL = "full"
    SUBGRAPH = "subgraph"
    NODE_IDS = "node_ids"
    ATTRIBUTE_FILTER = "attribute_filter"


class ChainQuery(BaseModel):
    """
    Represents a conversation tree query.
    Attributes:r
    conversation_tree_type (ConversationTreeType): The type of conversation tree.
    node_ids (List[str]): A list of node IDs to include in the conversation tree.
    attribute_filter (Dict[str, Any]): A dictionary where the key is the node attribute and the value is the desired attribute value.
    """

    conversation_tree_type: ChainTreeType = Field(
        None, description="The type of conversation tree."
    )

    node_ids: Optional[List[str]] = Field(
        None, description="A list of node IDs to include in the conversation tree."
    )

    attribute_filter: Optional[Dict[str, Any]] = Field(
        None,
        description="A dictionary where the key is the node attribute and the value is the desired attribute value.",
    )

    class Config:
        schema_extra = {
            "example": {
                "conversation_tree_type": "full",
                "node_ids": ["node_id_1", "node_id_2"],
                "attribute_filter": {"content": "Hello"},
            }
        }


class ChainTree(BaseModel):
    """

    Represents a conversation as a tree of messages.
    """

    id: str = Field(default_factory=lambda: str(uuid4()))

    title: str = Field(None, description="The title of the conversation.")

    create_time: float = Field(
        None, description="The timestamp for when the conversation was created."
    )
    update_time: float = Field(
        None, description="The timestamp for when the conversation was last updated."
    )

    mapping: Dict[str, ChainMap] = Field(
        None,
        description="A dictionary mapping node IDs to their corresponding message nodes.",
    )

    moderation_results: Optional[List[Dict[str, Any]]] = Field(
        None, description="Moderation results associated with the conversation."
    )
    current_node: Optional[str] = Field(None, description="The ID of the current node.")

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "id": "0",
                "title": "Conversation 1",
                "create_time": "2023-06-30T13:45:00",
                "update_time": "2023-06-30T13:45:00",
                "mapping": {
                    "0": {
                        "id": "0",
                        "message": {
                            "id": "0",
                            "text": "Hello World!",
                            "author": "User1",
                            "create_time": "2023-06-30T13:45:00",
                            "update_time": "2023-06-30T13:45:00",
                            "end_turn": True,
                            "weight": 1,
                            "metadata": {
                                "tags": ["greeting"],
                                "sentiment": 0.5,
                                "sentiment_score": 0.5,
                            },
                        },
                        "parent": None,
                        "children": ["1"],
                        "connections": [
                            {
                                "id": "0",
                                "source": "0",
                                "target": "1",
                                "weight": 1,
                                "metadata": {
                                    "tags": ["greeting"],
                                    "sentiment": 0.5,
                                    "sentiment_score": 0.5,
                                },
                            }
                        ],
                        "coordinate": {
                            "id": "0",
                            "depth": {
                                "x": 0.0,
                                "s_x": 0.0,
                                "c_x": 0.0,
                            },
                            "sibling": {
                                "y": 0.0,
                                "a_y": 0.0,
                            },
                            "sibling_count": {
                                "z": 0.0,
                                "m_z": 0.0,
                            },
                            "time": {
                                "t": 0.0,
                                "p_y": 0.0,
                            },
                        },
                        "embedding": {
                            "id": "0",
                            "term_id": "Term1",
                            "message_id": "Message1",
                            "cluster_label": 0,
                            "umap_embeddings": [0.0, 0.0, 0.0, 0.0, 0.0],
                            "embedding": [0.0, 0.0, 0.0, 0.0, 0.0],
                            "n_neighbors": 1,
                        },
                        "next": "1",
                        "prev": None,
                    },
                    "1": {
                        "id": "1",
                        "message": {
                            "id": "1",
                            "text": "Hello World!",
                            "author": "User1",
                            "create_time": "2023-06-30T13:45:00",
                            "update_time": "2023-06-30T13:45:00",
                            "end_turn": True,
                            "weight": 1,
                            "metadata": {
                                "tags": ["greeting"],
                                "sentiment": 0.5,
                                "sentiment_score": 0.5,
                            },
                        },
                        "parent": "0",
                        "children": ["2"],
                        "connections": [
                            {
                                "id": "1",
                                "source": "1",
                                "target": "2",
                                "weight": 1,
                                "metadata": {
                                    "tags": ["greeting"],
                                    "sentiment": 0.5,
                                    "sentiment_score": 0.5,
                                },
                            }
                        ],
                        "coordinate": {
                            "id": "1",
                            "depth": {
                                "x": 0.0,
                                "s_x": 0.0,
                                "c_x": 0.0,
                            },
                            "sibling": {
                                "y": 0.0,
                                "a_y": 0.0,
                            },
                            "sibling_count": {
                                "z": 0.0,
                                "m_z": 0.0,
                            },
                            "time": {
                                "t": 0.0,
                                "p_y": 0.0,
                            },
                        },
                        "embedding": {
                            "id": "1",
                            "term_id": "Term1",
                            "message_id": "Message1",
                            "cluster_label": 0,
                            "umap_embeddings": [0.0, 0.0, 0.0, 0.0, 0.0],
                            "embedding": [0.0, 0.0, 0.0, 0.0, 0.0],
                            "n_neighbors": 1,
                        },
                        "next": "2",
                        "prev": "0",
                    },
                    "2": {
                        "id": "2",
                        "message": {
                            "id": "2",
                            "text": "Hello World!",
                            "author": "User1",
                            "create_time": "2023-06-30T13:45:00",
                            "update_time": "2023-06-30T13:45:00",
                            "end_turn": True,
                            "weight": 1,
                            "metadata": {
                                "tags": ["greeting"],
                                "sentiment": 0.5,
                                "sentiment_score": 0.5,
                            },
                        },
                        "parent": "1",
                        "children": [],
                        "connections": [],
                        "coordinate": {
                            "id": "2",
                            "depth": {
                                "x": 0.0,
                                "s_x": 0.0,
                                "c_x": 0.0,
                            },
                            "sibling": {
                                "y": 0.0,
                                "a_y": 0.0,
                            },
                            "sibling_count": {
                                "z": 0.0,
                                "m_z": 0.0,
                            },
                            "time": {
                                "t": 0.0,
                                "p_y": 0.0,
                            },
                        },
                        "embedding": {
                            "id": "2",
                            "term_id": "Term1",
                            "message_id": "Message1",
                            "cluster_label": 0,
                            "umap_embeddings": [0.0, 0.0, 0.0, 0.0, 0.0],
                            "embedding": [0.0, 0.0, 0.0, 0.0, 0.0],
                            "n_neighbors": 1,
                        },
                        "next": None,
                        "prev": "1",
                    },
                },
                "moderation_results": [
                    {
                        "id": "0",
                        "message_id": "0",
                        "moderator_id": "0",
                        "moderator_name": "Moderator1",
                        "timestamp": "2023-06-30T13:45:00",
                        "tags": ["greeting"],
                        "sentiment": 0.5,
                        "sentiment_score": 0.5,
                    }
                ],
                "current_node": "0",
            }
        }

    def __init__(self, **data: Any):
        super().__init__(**data)
        if self.mapping is None:
            self.mapping = {}
        if self.moderation_results is None:
            self.moderation_results = []
        if self.current_node is None:
            self.current_node = None

    def retrieve_all_conversation_messages(self) -> List[ChainMap]:
        return list(self.mapping.values())

    def retrieve_all_conversation_messages_ids(self) -> List[str]:
        return list(self.mapping.keys())

    def retrieve_all_conversation_messages_contents(self) -> List[str]:
        return [message.message.content for message in self.mapping.values()]

    def retrieve_all_conversation_messages_authors(self) -> List[str]:
        return [message.message.author for message in self.mapping.values()]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ChainTree":
        return cls(**data)

    def to_dict(self) -> Dict[str, Any]:
        return self.dict()

    def to_csv(self, path: str) -> None:
        df = pd.DataFrame.from_dict(self.mapping, orient="index")
        df.to_csv(path, index=False)


class ChainTreeIndex(BaseModel):
    conversation: ChainTree

    def to_dict(self) -> Dict[str, Any]:
        return {"conversation": self.conversation.dict()}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ChainTreeIndex":
        return cls(conversation=ChainTree.from_dict(data["conversation"]))
