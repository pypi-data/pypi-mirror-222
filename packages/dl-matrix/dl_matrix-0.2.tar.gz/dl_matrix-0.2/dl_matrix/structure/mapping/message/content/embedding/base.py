from pydantic import BaseModel, Field, validator
from typing import List, Optional, Any
from sentence_transformers import SentenceTransformer


class Embedding(BaseModel):
    """Defines the embeddings for the Content."""

    message_id: Optional[str] = Field(
        None, description="The unique identifier of the message."
    )

    cluster_label: Optional[int] = Field(
        None, description="The label of the cluster to which this data point belongs."
    )
    umap_embeddings: Optional[List[float]] = Field(
        None,
        description="Embeddings computed using UMAP (Uniform Manifold Approximation and Projection).",
    )
    embedding: Optional[List[float]] = Field(
        None, description="Actual embedding of the content."
    )
    n_neighbors: Optional[int] = Field(
        None,
        ge=1,
        description="The number of neighbors to consider when constructing the UMAP graph. Must be at least 1.",
    )

    class Config:
        schema_extra = {
            "example": {
                "message_id": "Message1",
                "cluster_label": 0,
                "umap_embeddings": [0.0, 0.0, 0.0, 0.0, 0.0],
                "embedding": [0.0, 0.0, 0.0, 0.0, 0.0],
                "n_neighbors": 1,
            }
        }

    @staticmethod
    def encode_texts(texts: List[str]) -> List[float]:
        """ """
        model = SentenceTransformer("paraphrase-distilroberta-base-v1")

        # Preprocess the texts
        model.max_seq_length = 256

        # Get embeddings for preprocessed texts
        embeddings = model.encode(
            texts,
            batch_size=256,  # change this to your batch size
            convert_to_numpy=True,
            show_progress_bar=True,
        )

        return embeddings.tolist()
