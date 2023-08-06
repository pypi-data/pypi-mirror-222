from typing import List, Optional, Any, Dict
from pydantic import BaseModel, Field, validator
from .types import ContentType
from .production import ProductionWords
from .moderation import ModerationResult
from .embedding import Embedding


class Content(BaseModel):
    content_type: ContentType = Field(
        ContentType.TEXT, description="The type of content (text, image, audio, etc.)"
    )
    text: Optional[str] = Field(None, description="The text content.")

    parts: Optional[List[str]] = Field(
        None, description="The parts of the content (text, image, audio, etc.)"
    )

    part_lengths: Optional[int] = Field(
        None, description="The lengths of the parts of the content."
    )

    embeddings: Optional[Embedding] = Field(
        None, description="Embeddings associated with the content."
    )

    production_words: Optional[ProductionWords] = Field(
        None, description="Production words derived from the content."
    )

    moderation_results: Optional[List[ModerationResult]] = Field(
        None, description="The moderation results for the content."
    )

    def __init__(self, **data: Any):
        super().__init__(**data)
        if self.parts:
            self.text = self.parts[0]
            self.part_lengths = len(self.text.split("\n\n") if self.text else [])

    @validator("parts", pre=True)
    def parts_to_list(cls, v):
        if isinstance(v, str):
            return [v]
        return v

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

        json_schema_extra = {
            "example": {
                "parts": ["Hello"],
                "text": "Hello",
                "content_type": "text",
                "production_words": [],
                "moderation_results": [],
            }
        }

    @classmethod
    def from_text(cls, text: str):
        """Creates a Content object from text."""
        return cls(content_type="text", parts=[text])
