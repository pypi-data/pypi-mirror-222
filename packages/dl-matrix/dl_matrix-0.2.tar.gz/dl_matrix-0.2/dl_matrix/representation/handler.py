from typing import List, Dict, Union
from dl_matrix.context import MultiLevelContext, DataFrameStore
from dl_matrix.similarity import SemanticSimilarity
from dl_matrix.schema import ChainDocument, ChainDocumentStore
from pydantic import BaseModel
from dl_matrix.coordinate import Coordinate
import numpy as np
import pandas as pd


class ChainHandler(BaseModel):
    chain_documents: List[ChainDocument] = []

    flattened_dict_id_coord: Dict[str, Coordinate] = {}

    semantic_similarity_model = SemanticSimilarity()

    docstore = ChainDocumentStore()

    class Config:
        arbitrary_types_allowed = True

    def initialize_storage_context(self, main_df):
        return MultiLevelContext.from_defaults(main_df_store=DataFrameStore(main_df))

    def add_local_embeddings(
        self, tetra_dict: Union[Dict[str, Coordinate], List[ChainDocument]]
    ) -> None:
        """
        Adds local embeddings to the document store.
        Raises a ValueError if the tetra_dict is invalid.
        """
        docstore = ChainDocumentStore()
        if all(isinstance(doc, ChainDocument) for doc in tetra_dict):
            for doc in tetra_dict:
                self.chain_documents.append(doc)
                docstore.add_documents(self.chain_documents)
                self.flattened_dict_id_coord[doc.id_] = doc.coordinate
        elif isinstance(tetra_dict, tuple) and len(tetra_dict) == 2:
            coordinates, relationships = tetra_dict
            self.flattened_dict_id_coord.update(coordinates)
            docstore.add_documents(self.chain_documents)

        else:
            raise ValueError(
                "Invalid tetra_dict type, should be instance of TreeDocument or tuple."
            )

    def create_and_persist_dataframes(self):
        main_df = self.create_dataframe()
        storage_context = self.initialize_storage_context(main_df)
        self.add_coordinates_to_dataframe(storage_context)
        self.handle_local_embeddings(storage_context, main_df)
        storage_context.persist()
        return main_df

    def create_dataframe(self):
        data = [
            {
                "id_": doc.id_,
                "text": doc.text,
                "author": doc.author,
                "coordinate": doc.coordinate,
                "sub_graph": doc.sub_graph,
                "n_neighbors": doc.n_neighbors,
                "umap_embeddings": doc.umap_embeddings,
                "relationships": doc.relationships,
                "cluster_label": doc.cluster_label,
                "create_time": doc.create_time,
            }
            for doc in self.chain_documents
        ]

        main_df = pd.DataFrame(data)
        return main_df

    def add_coordinates_to_dataframe(self, storage_context: MultiLevelContext):
        storage_context.main_df_store.df[
            "coordinate"
        ] = storage_context.main_df_store.df["id_"].apply(
            lambda x: self.flattened_dict_id_coord[x]
        )

    def handle_local_embeddings(
        self, storage_context: MultiLevelContext, main_df: pd.DataFrame
    ):
        if "text" not in main_df:
            raise ValueError("No 'text' column in main_df.")
        if not callable(getattr(self.semantic_similarity_model, "encode_texts", None)):
            raise ValueError(
                "encode_texts method not found in semantic_similarity_model."
            )
        # sort local embeddings by create_time
        self.chain_documents = sorted(self.chain_documents, key=lambda x: x.create_time)

        local_embeddings = [doc.embedding[0] for doc in self.chain_documents]
        storage_context.main_df_store.df["embedding"] = local_embeddings
        n_neighbors_list = [doc.n_neighbors for doc in self.chain_documents]
        if n_neighbors_list:  # Check if n_neighbors_list is not empty
            self.handle_neighbors(
                storage_context, main_df, n_neighbors_list, local_embeddings
            )
        else:
            print("No neighbors found for any documents.")

    def handle_neighbors(
        self,
        storage_context: MultiLevelContext,
        main_df,
        n_neighbors_list,
        local_embeddings,
    ):
        mean_n_neighbors = int(np.mean(n_neighbors_list))
        umap_embeddings = self.semantic_similarity_model.apply_umap(
            local_embeddings,
            mean_n_neighbors,
            3,
        )
        labels = self.semantic_similarity_model.apply_hdbscan(umap_embeddings)
        result3d = self.create_3d_results(main_df, umap_embeddings, labels)
        self.add_coordinates_to_result3d(result3d, storage_context)
        storage_context.result3d_store = DataFrameStore(result3d)

    def create_3d_results(self, main_df, umap_embeddings, labels):
        result3d = pd.DataFrame(umap_embeddings, columns=["x", "y", "z"])
        result3d["content"] = main_df["text"].values.tolist()
        result3d["author"] = main_df["author"].values.tolist()
        result3d["id_"] = main_df["id_"].values.tolist()
        result3d["labels"] = labels
        return result3d

    def add_coordinates_to_result3d(self, result3d, storage_context):
        coord_columns = Coordinate.get_coordinate_names()

        for i, column in enumerate(coord_columns):
            result3d[column] = result3d["id_"].apply(
                lambda x: self.flattened_dict_id_coord[x][i]
            )
