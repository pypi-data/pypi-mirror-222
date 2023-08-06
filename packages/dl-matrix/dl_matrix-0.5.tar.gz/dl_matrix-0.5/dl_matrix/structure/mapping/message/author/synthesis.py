from pydantic import BaseModel
from typing import Dict, Any
from pydantic.fields import Field
import json
from .author import Author


class Synthesis(BaseModel):
    author: Author = Field(..., description="The author of the synthesis technique.")
    epithet: str = Field(..., description="The epithet of the synthesis technique.")
    name: str = Field(..., description="The name of the synthesis technique.")
    technique_name: str = Field(..., description="The name of the synthesis technique.")
    imperative: str = Field(
        ..., description="The imperative of the synthesis technique."
    )
    prompts: Dict[str, Any] = Field(
        ..., description="The prompts of the synthesis technique."
    )

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "author": {
                    "role": "user",
                    "id": "123456789",
                    "entity_name": "John Doe",
                    "description": "The user of the conversation. This is the default role.",
                    "metadata": {},
                },
                "epithet": "Harmony in Diversity",
                "name": "Harmony in Diversity: Creating a Cohesive Whole",
                "technique_name": "Harmony in Diversity: Creating a Cohesive Whole",
                "imperative": "Explore how different pieces of information harmoniously fit together, laying the foundation for a new whole",
                "prompts": {
                    "Harmony in Diversity: Creating a Cohesive Whole": {
                        "branching_options": [
                            "Explore how different pieces of information harmoniously fit together, laying the foundation for a new whole",
                            "Delve into the symphony of merging ideas and discover the magic that emerges from their convergence",
                        ],
                        "dynamic_prompts": [
                            "What valuable insights and perspectives can we glean from the harmonious fusion of diverse ideas?",
                            "In what ways can we seamlessly integrate and synthesize various sources of information to unlock novel possibilities?",
                            "How can we bridge gaps and cultivate common ground among diverse groups, igniting collaborative synergy?",
                            "By uniting talents and skills from various domains, what extraordinary feats can we achieve?",
                        ],
                        "complex_diction": [
                            "synapse",
                            "cohesion",
                            "integration",
                            "synthesis",
                        ],
                    },
                    "Unleashing the Power of Convergence: Where Possibilities Unfold": {
                        "branching_options": [
                            "Embark on an exploratory journey into the uncharted realms of merging perspectives and concepts",
                            "Challenge the boundaries of imagination by embracing the extraordinary potential of combining seemingly unrelated ideas",
                        ],
                        "dynamic_prompts": [
                            "What boundless possibilities arise from the alchemy of merging different ideas, unlocking untapped realms of innovation?",
                            "How can we leverage the unique strengths of diverse approaches to unravel solutions to complex problems?",
                            "By engaging in a tapestry of comparisons and contrasts, what profound lessons can we learn from different solutions?",
                            "What hidden opportunities lie at the intersection of multiple angles, waiting to be discovered and harnessed?",
                        ],
                        "complex_diction": [
                            "innovation",
                            "divergent",
                            "unification",
                            "collaboration",
                        ],
                    },
                },
            }
        }

    def to_dict(self) -> Dict[str, Any]:
        return self.dict(exclude_none=True)

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
