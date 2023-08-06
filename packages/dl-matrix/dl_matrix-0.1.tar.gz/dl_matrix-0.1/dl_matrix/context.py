import pandas as pd
from typing import Optional
import numpy as np
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
import fsspec
import os

DEFAULT_PERSIST_DIR = "dl_matrix/storage"


def concat_dirs(dir1: str, dir2: str) -> str:
    """

    Concat dir1 and dir2 while avoiding backslashes when running on windows.
    os.path.join(dir1,dir2) will add a backslash before dir2 if dir1 does not
    end with a slash, so we make sure it does.

    """
    dir1 += "/" if dir1[-1] != "/" else ""
    return os.path.join(dir1, dir2)


class DataFrameStore:
    def __init__(self, df=pd.DataFrame()):
        self.df = df

    def persist(self, persist_path, fs=None):
        """Persist the DataFrame to a file."""
        self.df.to_csv(persist_path, index=False)

    @classmethod
    def from_persist_dir(cls, persist_dir, fs=None):
        """Load the DataFrame from a file."""
        df = pd.read_csv(persist_dir)
        return cls(df=df)

    def to_dict(self):
        return self.df.to_dict()

    @classmethod
    def from_dict(cls, save_dict):
        df = pd.DataFrame(save_dict)
        return cls(df=df)

    def get_df(self):
        return self.df

    def set_df(self, df):
        self.df = df


class NumpyStore:
    def __init__(self, array=np.array([])):
        self.array = array

    def persist(self, persist_path, fs=None):
        """Persist the numpy array to a file."""
        np.save(persist_path, self.array)

    @classmethod
    def from_persist_dir(cls, persist_dir, fs=None):
        """Load the numpy array from a file."""
        array = np.load(persist_dir)
        return cls(array=array)

    def to_dict(self):
        return self.array.tolist()

    @classmethod
    def from_dict(cls, save_dict):
        array = np.array(save_dict)
        return cls(array=array)

    def get_array(self):
        return self.array


@dataclass
class MultiLevelContext:
    """MultiLevelContext context.

    The MultiLevelContext container is a utility container for storing
    main_df, part_df,result3d.csv and global_embedding.

    It contains the following:

    - main_df_store: DataFrameStore
    - result3d_store: DataFrameStore
    - global_embedding_store: NumpyStore

    """

    main_df_store: DataFrameStore
    result3d_store: DataFrameStore
    global_embedding_store: NumpyStore

    @classmethod
    def from_defaults(
        cls,
        main_df_store: Optional[DataFrameStore] = None,
        result3d_store: Optional[DataFrameStore] = None,
        global_embedding_store: Optional[NumpyStore] = None,
        persist_dir: Optional[str] = None,
        fs: Optional[fsspec.AbstractFileSystem] = None,
    ) -> "MultiLevelContext":
        """Create a MultiLevelContext from defaults."""

        if persist_dir is None:
            main_df_store = main_df_store or DataFrameStore()
            result3d_store = result3d_store or DataFrameStore()
            global_embedding_store = global_embedding_store or NumpyStore()
        else:
            main_df_store = main_df_store or DataFrameStore.from_persist_dir(
                persist_dir + "/main_df.csv", fs=fs
            )
            result3d_store = result3d_store or DataFrameStore.from_persist_dir(
                persist_dir + "/result3d.csv", fs=fs
            )
            global_embedding_store = (
                global_embedding_store
                or NumpyStore.from_persist_dir(
                    persist_dir + "/global_embedding.npy", fs=fs
                )
            )

        return cls(main_df_store, result3d_store, global_embedding_store)

    def persist(
        self,
        persist_dir: str = DEFAULT_PERSIST_DIR,
        main_df_fname: str = "main_df.csv",
        result3d_fname: str = "result3d.csv",
        global_embedding_fname: str = "global_embedding.npy",
        fs: Optional[fsspec.AbstractFileSystem] = None,
    ) -> None:
        """Persist the MultiLevelContext."""
        if not os.path.exists(persist_dir):
            os.makedirs(persist_dir)

        if fs is not None:
            main_df_path = concat_dirs(persist_dir, main_df_fname)
            result3d_path = concat_dirs(persist_dir, result3d_fname)
            global_embedding_path = concat_dirs(persist_dir, global_embedding_fname)
        else:
            main_df_path = str(Path(persist_dir) / main_df_fname)
            result3d_path = str(Path(persist_dir) / result3d_fname)
            global_embedding_path = str(Path(persist_dir) / global_embedding_fname)

        if self.main_df_store is not None:
            self.main_df_store.persist(persist_path=main_df_path, fs=fs)
        if self.result3d_store is not None:
            self.result3d_store.persist(persist_path=result3d_path, fs=fs)
        if self.global_embedding_store is not None:
            self.global_embedding_store.persist(
                persist_path=global_embedding_path, fs=fs
            )

    def to_dict(self) -> dict:
        result = {}
        if self.main_df_store is not None:
            result["main_df"] = self.main_df_store.to_dict()
        if self.result3d_store is not None:
            result["result3d"] = self.result3d_store.to_dict()
        if self.global_embedding_store is not None:
            result["global_embedding"] = self.global_embedding_store.array.tolist()
        return result

    @classmethod
    def from_dict(cls, save_dict: dict) -> "MultiLevelContext":
        """Create a MultiLevelContext from dict."""
        main_df_store = DataFrameStore.from_dict(save_dict["main_df"])
        result3d_store = DataFrameStore.from_dict(save_dict["result3d"])
        global_embedding_store = NumpyStore(np.array(save_dict["global_embedding"]))
        return cls(
            main_df_store=main_df_store,
            result3d_store=result3d_store,
            global_embedding_store=global_embedding_store,
        )
