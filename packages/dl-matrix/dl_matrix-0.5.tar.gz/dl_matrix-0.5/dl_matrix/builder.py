import json
from typing import Optional, Union, Dict, Any, List, Tuple
from dl_matrix.structure import (
    ChainTreeIndex,
    ChainTree,
    ChainMap,
)
from dl_matrix.parsers import ChainTreeParser
import glob
import re
import os
import pandas as pd
import networkx as nx


class ChainTreeBuilder:
    def __init__(
        self,
        path: str = "conversations.json",
        save_path: Optional[str] = "conversations_combined.json",
        save_path_adjacency_list: Optional[str] = "combined_adjacency_list.json",
        key: Optional[str] = "title",
        prompt_dir: Optional[str] = None,
    ):
        self.path = path
        self.key = key
        self.data = self.load_json(path)
        self.conversations = ChainTreeParser.parse_chain_tree(self.data)
        self.prompt_dir = prompt_dir
        self.save_path = save_path
        self.save_path_adjacency_list = save_path_adjacency_list
        self._adjacency_list: Dict[str, List[str]] = {}
        self._combined_mapping: Dict[str, ChainMap] = {}
        self.graph = nx.DiGraph()

    def create_conversation_trees(
        self, target_num: int = 6
    ) -> Tuple[List[ChainTreeIndex], List[ChainTreeIndex]]:
        greater_than_target = []
        less_than_target = []

        for i, conversation in enumerate(self.conversations):
            if conversation is not None:
                if len(conversation.mapping) >= target_num:
                    greater_than_target.append(
                        ChainTreeIndex(conversation=conversation)
                    )
                else:
                    # Only update title for conversations that are less than target_num
                    conversation.title = str(i)
                    less_than_target.append(ChainTreeIndex(conversation=conversation))

        return greater_than_target

    def as_list(self) -> List[ChainTreeIndex]:
        return self.create_conversation_trees()

    def as_dict(self) -> Dict[str, ChainTreeIndex]:
        if not self.key:
            raise ValueError("Key must be provided when building a dictionary.")
        conversation_trees = self.create_conversation_trees()
        return {
            getattr(conversation, self.key): tree
            for conversation, tree in zip(self.conversations, conversation_trees)
        }

    def get(self, index: int) -> ChainTreeIndex:
        return self.create_conversation_trees()[index]

    def __iter__(self):
        return iter(self.create_conversation_trees())

    def __getitem__(self, index: int) -> ChainTreeIndex:
        return self.get(index)

    def __len__(self) -> int:
        return len(self.create_conversation_trees())

    def load_json(self, source: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        if not os.path.isfile(source):
            raise ValueError(f"{source} does not exist.")
        with open(source, "r") as f:
            data = json.load(f)
        return data

    def save_json(self, path: str, data: Union[Dict[str, Any], List[Dict[str, Any]]]):
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    def save_file(self, path: str, data: List[str]):
        with open(path, "w") as f:
            f.write("\n\n".join(data))

    def load_all_prompts_nested_with_key_selection(self) -> List[dict]:
        """
        Load all prompt objects from the stored JSON files.
        """
        prompt_objects = []
        prompt_files = glob.glob(os.path.join(self.prompt_dir, "**/*.json"))
        if prompt_files:
            prompt_files.sort(
                key=lambda f: int(re.search(r"\d+", os.path.basename(f)).group())
            )
            for prompt_file in prompt_files:
                with open(prompt_file, "r") as f:
                    prompt_object = json.load(f)
                prompt_objects.append(prompt_object[self.key])
            return prompt_objects
        else:
            print("No prompt files found.")
            return None

    def combine_json_files(self, path1: str, path2: str, output_path: str) -> None:
        data1 = self.load_json(path1)
        data2 = self.load_json(path2)

        if not isinstance(data1, list) or not isinstance(data2, list):
            raise ValueError("Both input files should contain a list of JSON objects.")

        combined_data = data1 + data2

        self.save_json(output_path, combined_data)
        print(f"Combined data saved to {output_path}.")

    def load_all_prompts(self) -> List[str]:
        """
        Load all prompts from the stored JSON files.
        """
        prompts = []
        prompt_files = glob.glob(os.path.join(self.prompt_dir, "**/*.json"))
        if prompt_files:
            prompt_files.sort(
                key=lambda f: int(re.search(r"\d+", os.path.basename(f)).group())
            )
            for prompt_file in prompt_files:
                with open(prompt_file, "r") as f:
                    prompt_object = json.load(f)
                prompts.append(prompt_object["prompt"])
            return prompts
        else:
            print("No prompt files found.")
            return None

    def get_message_coord_map(self):
        self.message_coord_map = {}
        for tree in self.create_conversation_trees():
            for message_id, mapping in tree.conversation.mapping.items():
                if (
                    mapping.message is not None
                    and mapping.message.author.role != "system"
                ):
                    self.message_coord_map[message_id] = {
                        "message_id": mapping.message.id,
                        "text": mapping.message.content.text,
                        "author": mapping.message.author.role,
                        "create_time": mapping.message.create_time,
                        "finish_details": mapping.message.metadata.finish_details,
                    }
        self.main_df = pd.DataFrame.from_dict(self.message_coord_map, orient="index")
        return self.main_df.reset_index(drop=True)

    @property
    def combined_mapping(self):
        return self._combined_mapping

    @property
    def adjacency_list(self):
        return self._adjacency_list

    def _update_adjacency_list(self, conversation: ChainTree):
        for mapping_id, mapping in conversation.mapping.items():
            if mapping.message is None:
                continue

            if mapping_id not in self._adjacency_list:
                self._adjacency_list[mapping_id] = []

            if mapping.parent is not None:
                if mapping.parent not in self._adjacency_list:
                    self._adjacency_list[mapping.parent] = []
                self._adjacency_list[mapping.parent].append(mapping_id)

            for ref_id in mapping.references:
                if ref_id in self._combined_mapping:
                    if ref_id not in self._adjacency_list:
                        self._adjacency_list[ref_id] = []
                    self._adjacency_list[ref_id].append(mapping_id)

    def _process_system_messages(self, conversation: ChainTree):
        system_message_id = [
            message_id
            for message_id, message in conversation.mapping.items()
            if message.message.author.role == "system"
        ]
        if system_message_id:
            system_message_id = system_message_id[0]
            self._update_system_message_children(system_message_id, conversation)
            self._update_user_and_assistant_messages(system_message_id, conversation)
            if int(conversation.title) > 1:
                del self._combined_mapping[system_message_id]

    def _update_system_message_children(
        self, system_message_id: str, conversation: ChainTree
    ):
        for child_id in conversation.mapping[system_message_id].children:
            self._combined_mapping[child_id].parent = None
            # only remove the edge if the system_message_id exists in the adjacency list
            if system_message_id in self._adjacency_list:
                if child_id in self._adjacency_list[system_message_id]:
                    self._adjacency_list[system_message_id].remove(
                        child_id
                    )  # remove this edge from the adjacency list
        self._combined_mapping[system_message_id].children = []

    def _update_user_and_assistant_messages(
        self, system_message_id: str, conversation: ChainTree
    ):
        user_message_id, assistant_message_id = [
            message_id
            for message_id, message in conversation.mapping.items()
            if message.message.author.role in ["user", "assistant"]
        ]
        self._combined_mapping[assistant_message_id].parent = user_message_id
        self._combined_mapping[user_message_id].children = [assistant_message_id]
        # Update adjacency list accordingly
        if user_message_id in self._adjacency_list:
            self._adjacency_list[user_message_id].append(assistant_message_id)
        else:
            self._adjacency_list[user_message_id] = [assistant_message_id]

    def _save_adjacency_list(self):
        with open(self.save_path_adjacency_list, "w") as f:
            json.dump(self._adjacency_list, f)

    def update_graph(self, conversation: ChainTree):
        for mapping_id, mapping in conversation.mapping.items():
            if mapping.message is None:
                continue

            self.graph.add_node(mapping_id, **mapping.message.dict())

            if mapping.parent is not None:
                self.graph.add_edge(mapping.parent, mapping_id)

            for ref_id in mapping.references:
                if ref_id in self.combined_mapping:
                    self.graph.add_edge(mapping_id, ref_id)


def count_starting_phrase(
    df: pd.DataFrame, phrase: str, author: str = "assistant"
) -> int:
    """
    Count the number of messages by a specific author that start with a given phrase.

    Args:
        df (pd.DataFrame): The DataFrame containing the message data.
        phrase (str): The phrase to search for at the start of messages.
        author (str): The author to search messages from. Default is 'assistant'.

    Returns:
        int: The number of messages by the author that start with the given phrase.
    """
    author_messages = df[df["author"] == author]["message"]
    count = author_messages.str.startswith(phrase).sum()
    return count


def count_ending_phrase(
    df: pd.DataFrame, phrase: str, author: str = "assistant"
) -> int:
    """
    Count the number of messages by a specific author that end with a given phrase.

    Args:
        df (pd.DataFrame): The DataFrame containing the message data.
        phrase (str): The phrase to search for at the end of messages.
        author (str): The author to search messages from. Default is 'assistant'.

    Returns:
        int: The number of messages by the author that end with the given phrase.
    """
    author_messages = df[df["author"] == author]["message"]
    count = author_messages.str.endswith(phrase).sum()
    return count


def count_messages(df: pd.DataFrame, author: str = "assistant") -> int:
    """
    Count the number of messages by a specific author.

    Args:
        df (pd.DataFrame): The DataFrame containing the message data.
        author (str): The author to search messages from. Default is 'assistant'.

    Returns:
        int: The number of messages by the author.
    """
    author_messages = df[df["author"] == author]["message"]
    count = len(author_messages)
    return count
