from typing import List, Tuple, Dict, Any, Union
import numpy as np
from sentence_transformers import SentenceTransformer
import hdbscan
from sklearn.cluster import DBSCAN
import logging
import openai
import warnings

with warnings.catch_warnings():
    from numba.core.errors import NumbaWarning

    warnings.simplefilter("ignore", category=NumbaWarning)
    from umap import UMAP


class SemanticSimilarity:
    def __init__(
        self,
        reduce_dimensions=True,
        batch_size=100,
        n_components=3,
        weights=None,
        model_name="all-mpnet-base-v2",
        api_key=None,
    ):
        """Initialize a SemanticSimilarity."""
        self._model_name = model_name
        self._semantic_vectors = []
        self.keywords = []
        self._model = SentenceTransformer(self._model_name)  # Initialize model here
        self.weights = weights if weights is not None else {}
        self.default_options = {
            "n_components": n_components,
            "reduce_dimensions": reduce_dimensions,
            "n_neighbors": None,
        }
        self.batch_size = batch_size
        self.api_key = api_key

    @property
    def model_name(self) -> str:
        return self._model_name

    @model_name.setter
    def model_name(self, model_name: str):
        self._model_name = model_name
        self._model = SentenceTransformer(self._model_name)

    def encode_texts(self, texts: List[str]) -> List[List[float]]:
        """
        Embed a batch of texts as a list of lists of floats using the SentenceTransformer.
        """
        # Preprocess the texts
        self._model.max_seq_length = 512

        # Get embeddings for preprocessed texts
        embeddings = self._model.encode(
            texts,
            batch_size=self.batch_size,
            convert_to_numpy=True,
            show_progress_bar=True,
        )

        return embeddings

    def process_message_dict(
        self, message_dict: Dict[str, Any]
    ) -> Tuple[List[str], List[str]]:
        """
        Extract the message text and ID from the message dictionary.
        """
        message_texts = []
        message_ids = []
        for message in message_dict.values():
            if message.message and message.message.author.role != "system":
                message_texts.append(message.message.content.parts[0])
                message_ids.append(message.id)
        return message_texts, message_ids

    def generate_message_to_embedding_dict(
        self, message_ids: List[str], embeddings: List[np.array]
    ) -> Dict[str, np.array]:
        """
        Generate a dictionary mapping message IDs to embeddings.
        """
        return {message_ids[i]: embeddings[i] for i in range(len(message_ids))}

    def compute_neighbors(self, grid, message_dict: Dict[str, Any]) -> Dict[str, int]:
        """
        For each message, determine the number of neighbors.
        """
        n_neighbors_dict = {}
        for message_id in message_dict:
            n_neighbors_dict[message_id] = grid.determine_n_neighbors(message_id)
        return n_neighbors_dict

    def generate_message_embeddings(
        self,
        grid,
        message_dict: Dict[str, Any],
        options: dict = None,
    ) -> Dict[str, Union[np.array, Tuple[str, str]]]:
        """
        Generate semantic embeddings for the messages in the conversation tree using a sentence transformer.
        """
        # Update default options with user-specified options
        if options is not None:
            self.default_options.update(options)

        # Extract the message text and ID from the message dictionary
        message_texts, message_ids = self.process_message_dict(message_dict)

        # Encode the message texts to obtain their embeddings
        embeddings = self.encode_texts(message_texts)

        # Create a dictionary mapping message IDs to embeddings
        message_embeddings = self.generate_message_to_embedding_dict(
            message_ids, embeddings
        )

        if len(message_dict) > 1:
            n_neighbors_dict = self.compute_neighbors(grid, message_dict)
            self.default_options["n_neighbors"] = np.mean(
                list(n_neighbors_dict.values())
            )
            reduced_embeddings = self.generate_reduced_embeddings(
                embeddings, self.default_options
            )

            message_embeddings = self.generate_message_to_embedding_dict(
                message_ids, reduced_embeddings
            )
            clusters = self.cluster_terms(list(message_embeddings.items()))

            # Assign each message id to a cluster label
            clustered_messages = {}
            for cluster_label, terms in clusters.items():
                for term in terms:
                    # Assuming term is a tuple with more than 2 elements, we only take the first one
                    term_id = term[0]
                    clustered_messages[term_id] = (
                        message_embeddings[term_id],
                        cluster_label,
                        embeddings,
                        n_neighbors_dict[
                            term_id
                        ],  # Add the count of neighbors to the dictionary
                    )

            return clustered_messages

    def cluster_terms(
        self, terms: List[Tuple[str, List[float]]]
    ) -> Dict[int, List[Tuple[str, List[float]]]]:
        try:
            if not terms:
                print("No terms provided for grouping")
                return {}

            # Extract the embeddings from the terms
            embeddings = np.array([embedding for _, embedding in terms])

            # Apply weights if available
            for i, (term, _) in enumerate(terms):
                if term in self.weights:
                    embeddings[i] *= self.weights[term]

            clustering = DBSCAN(
                eps=0.5,
                min_samples=5,
                metric="euclidean",
            ).fit(embeddings)
            # Assign each term to a cluster
            clusters = {i: [] for i in set(clustering.labels_)}
            for i, label in enumerate(clustering.labels_):
                clusters[label].append(terms[i])

            return clusters

        except Exception as e:
            print(f"Error in cluster_terms: {e}")
            return {}

    def generate_reduced_embeddings(
        self, embeddings: np.ndarray, options: dict = None
    ) -> np.ndarray:
        """
        Reduce the dimensionality of the embeddings if necessary.
        """
        # convert embeddings dictionary to numpy array
        if isinstance(embeddings, dict):
            embeddings = np.array(list(embeddings.values()))

        # Update default options with user-specified options
        if options is not None:
            self.default_options.update(options)

        if self.default_options["reduce_dimensions"]:
            embeddings = self.apply_umap(
                embeddings,
                self.default_options["n_neighbors"],
                self.default_options["n_components"],
            )

        return embeddings

    def apply_umap(
        self,
        combined_features: np.ndarray,
        n_neighbors: int,
        n_components: int,
    ):
        umap_embedding = UMAP(
            n_neighbors=int(n_neighbors) + 1,
            n_components=n_components,
            n_epochs=10000,
            min_dist=0.0,
            low_memory=False,
            learning_rate=0.5,
            verbose=True,
            metric="cosine",
            init="random",  # use random initialization instead of spectral
        ).fit_transform(combined_features)

        return umap_embedding

    def apply_hdbscan(
        self,
        umap_embeddings: np.ndarray,
    ):
        hdbscan.dist_metrics.METRIC_MAPPING
        hdbscan_minimal_cluster_size = 100
        hdbscan_min_samples = 5

        cluster = hdbscan.HDBSCAN(
            min_cluster_size=hdbscan_minimal_cluster_size,
            metric="euclidean",
            min_samples=hdbscan_min_samples,
            core_dist_n_jobs=1,
            cluster_selection_epsilon=0.1,
            cluster_selection_method="leaf",
            leaf_size=40,
            algorithm="best",
        ).fit(umap_embeddings)

        return cluster.labels_

    def _embed_object(self, create_object: dict or list) -> dict:
        """
        Embeds the prompt object dictionary.
        :param create_object: The prompt object dictionary.
        :return: The embedded prompt object dictionary.
        """
        try:
            openai.api_key = self.api_key
        except Exception as e:
            logging.error(f"Error setting OpenAI API key: {e}")
            return None

        if isinstance(create_object, dict):
            embedded_object = {}
            for key, value in create_object.items():
                if isinstance(value, dict):
                    embedded_object[key] = self._embed_object(value)
                elif isinstance(value, list):
                    embedded_object[key] = self._embed_object(value)
                else:
                    response = openai.Embedding.create(
                        input=value, engine="text-embedding-ada-002"
                    )
                    vector = response["data"][0]["embedding"]
                    embedded_object[key] = vector
        elif isinstance(create_object, list):
            embedded_object = []
            for item in create_object:
                if isinstance(item, dict):
                    embedded_object.append(self._embed_object(item))
                elif isinstance(item, list):
                    embedded_object.append(self._embed_object(item))
                else:
                    response = openai.Embedding.create(
                        input=item, engine="text-embedding-ada-002"
                    )
                    vector = response["data"][0]["embedding"]
                    embedded_object.append(vector)
        else:
            response = openai.Embedding.create(
                input=create_object, engine="text-embedding-ada-002"
            )
            vector = response["data"][0]["embedding"]
            embedded_object = vector

        return embedded_object
