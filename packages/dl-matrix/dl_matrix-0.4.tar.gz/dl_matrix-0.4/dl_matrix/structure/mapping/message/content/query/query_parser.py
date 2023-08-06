from typing import List, Tuple, Dict, Optional, Any
from pydantic import BaseModel, Field, validator
import spacy
from transformers import AutoTokenizer, AutoModel


class QueryParser(BaseModel):
    query: str = Field(..., description="The user query to be processed.")
    processed_words: List[str] = Field(
        default_factory=list,
        description="The processed words extracted from the user query.",
    )
    semantic_vectors: List[List[float]] = Field(
        default_factory=list,
        description="The semantic vectors calculated for each word in the query.",
    )
    grouped_terms: Dict[str, List[Tuple[str, List[float]]]] = Field(
        default_factory=dict,
        description="The terms in the query grouped by field (if specified).",
    )
    named_entities: Dict[str, List[str]] = Field(
        default_factory=dict,
        description="The named entities identified in the user query.",
    )
    sentiment: Tuple[float, float] = Field(
        default_factory=tuple,
        description="The polarity and subjectivity of the user query, represented as a tuple.",
    )
    pos_tags: List[Tuple[str, str]] = Field(
        default_factory=list,
        description="The part-of-speech tags for the words in the user query.",
    )
    chunks: List[str] = Field(
        default_factory=list,
        description="The noun phrases or chunks in the user query.",
    )
    nouns: List[str] = Field(
        default_factory=list, description="The nouns identified in the user query."
    )
    verbs: List[str] = Field(
        default_factory=list, description="The verbs identified in the user query."
    )
    adjectives: List[str] = Field(
        default_factory=list, description="The adjectives identified in the user query."
    )
    adverbs: List[str] = Field(
        default_factory=list, description="The adverbs identified in the user query."
    )
    tokens: List[str] = Field(
        default_factory=list,
        description="The tokens obtained by tokenizing the user query.",
    )
    token_ids: List[int] = Field(
        default_factory=list,
        description="The IDs corresponding to the tokens of the user query.",
    )
    token_count: int = Field(0, description="The count of tokens in the user query.")

    class Config:
        arbitrary_types_allowed = True

    @validator("query")
    def load_spacy_model(cls, v):
        try:
            nlp = spacy.load("en_core_web_md")
            return nlp(v)
        except Exception as e:
            raise ValueError(
                "Failed to load Spacy model. Please ensure 'en_core_web_md' is installed."
            ) from e

    @validator("processed_words", always=True)
    def preprocess(cls, v, values):
        try:
            query = values.get("query")
            return [token.lemma_ for token in query if not token.is_stop]
        except Exception as e:
            raise ValueError("Failed to process the words in the query.") from e

    @validator("semantic_vectors", always=True)
    def compute_semantic_vectors(cls, v, values):
        try:
            tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
            model = AutoModel.from_pretrained("distilbert-base-uncased")
            query = values.get("query")
            inputs = tokenizer(query.text, return_tensors="pt")
            outputs = model(**inputs)
            return outputs.last_hidden_state.detach().numpy().tolist()
        except Exception as e:
            raise ValueError(
                "Failed to compute semantic vectors for the words in the query."
            ) from e

    @validator("grouped_terms", always=True)
    def group_terms(cls, v, values):
        try:
            processed_words = values.get("processed_words")
            semantic_vectors = values.get("semantic_vectors")
            return {
                word: vector for word, vector in zip(processed_words, semantic_vectors)
            }
        except Exception as e:
            raise ValueError("Failed to group the terms in the query.") from e

    @validator("named_entities", always=True)
    def extract_named_entities(cls, v, values):
        try:
            query = values.get("query")
            return {
                ent.label_: [e.text for e in query.ents if e.label_ == ent.label_]
                for ent in query.ents
            }
        except Exception as e:
            raise ValueError("Failed to extract named entities from the query.") from e

    @validator("pos_tags", always=True)
    def extract_pos_tags(cls, v, values):
        try:
            query = values.get("query")
            return [(token.text, token.tag_) for token in query]
        except Exception as e:
            raise ValueError(
                "Failed to extract part of speech tags from the query."
            ) from e

    @validator("chunks", always=True)
    def extract_chunks(cls, v, values):
        try:
            query = values.get("query")
            return list(query.noun_chunks)
        except Exception as e:
            raise ValueError("Failed to extract noun chunks from the query.") from e

    @validator("nouns", "verbs", "adjectives", "adverbs", always=True)
    def extract_pos(cls, v, values, field):
        try:
            query = values.get("query")
            pos_mapping = {
                "nouns": "NOUN",
                "verbs": "VERB",
                "adjectives": "ADJ",
                "adverbs": "ADV",
            }
            return [
                token.text for token in query if token.pos_ == pos_mapping[field.name]
            ]
        except Exception as e:
            raise ValueError(f"Failed to extract {field.name} from the query.") from e

    @validator("tokens", "token_ids", "token_count", always=True)
    def extract_tokens_and_ids(cls, v, values, field):
        try:
            query_text = values.get("query").text
            tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
            inputs = tokenizer(query_text, return_tensors="pt")
            if field.name == "tokens":
                return tokenizer.convert_ids_to_tokens(inputs.input_ids[0])
            elif field.name == "token_ids":
                return inputs.input_ids[0].tolist()
            elif field.name == "token_count":
                return inputs.input_ids[0].shape[0]
        except Exception as e:
            raise ValueError(f"Failed to extract {field.name} from the query.") from e
