from typing import Dict, List, Optional, Tuple
from dl_matrix.structure import ChainTreeIndex, ChainTree
from dl_matrix.representation.compute import CoordinateRepresentation
from dl_matrix.representation.filters import ChainFilter
from dl_matrix.builder import ChainTreeBuilder
import logging
import pandas as pd


class ChainCombiner:
    def __init__(
        self,
        builder: Optional[ChainTreeBuilder] = None,
        chain_filter: Optional[ChainFilter] = None,
        title_range: Optional[Tuple[int, int]] = (0, 10),
        max_workers: Optional[int] = 4,
    ):
        self.builder = builder if builder else ChainTreeBuilder()
        self.chain_filter = chain_filter if chain_filter else ChainFilter()
        self.conversations = self.builder.conversations
        self.title_range = title_range
        self._adjacency_list: Dict[str, List[str]] = {}
        self.max_workers = max_workers
        self.logger = logging.getLogger(self.__class__.__name__)
        self._combined_conversation = None
        self.less_than_target, self.greater_than_target = self.split_conversations()

        self.conversation_trees = self.builder.create_conversation_trees()

    def split_conversations(self, target_num: int = 10):
        """
        Splits the list of conversations into two lists: less_than_target and greater_than_target.
        The conversations are divided based on their size, determined by the number of mappings they contain.
        """
        less_than_target = []
        greater_than_target = []

        for i, conversation in enumerate(self.conversations):
            if conversation is not None:
                if len(conversation.mapping) >= target_num:
                    greater_than_target.append(conversation)
                else:
                    # Only update title for conversations that are less than target_num
                    conversation.title = str(i)
                    less_than_target.append(conversation)
        return less_than_target, greater_than_target

    def combine_small_conversations(
        self, conversations_to_combine: Optional[List[ChainTree]] = None
    ):
        """
        Combines the smaller conversations into a larger one.
        Takes an optional list of conversations to combine, defaulting to self.less_than_target.
        """
        if conversations_to_combine is None:
            conversations_to_combine = self.less_than_target
        # Combine the provided conversations
        return self.combine_conversations(conversations_to_combine)

    def create_combined_conversation_tree(self):
        """
        Creates a ChainTreeIndex for each Conversation in the greater_than_target list,
        including the newly combined conversation.
        """
        # Add the combined conversation to the list of larger conversations
        combined_conversation = self.combine_small_conversations()
        if combined_conversation is not None:
            self.greater_than_target.append(combined_conversation)
            return [
                ChainTreeIndex(conversation=conv) for conv in self.greater_than_target
            ]
        else:
            return [
                ChainTreeIndex(conversation=conv) for conv in self.greater_than_target
            ]

    def combine_conversations_save(
        self, conversations_to_combine: Optional[List[ChainTree]] = None
    ):
        """
        Combines the provided conversations and saves the combined conversation to a CSV file.
        """
        if conversations_to_combine is None:
            conversations_to_combine = self.conversations
        combined_conversation = self.combine_conversations(conversations_to_combine)
        if combined_conversation is not None:
            combined_conversation.to_csv()
            return combined_conversation
        else:
            return None

    def create_and_combine_conversations(
        self, target_num: int = 6
    ) -> List[ChainTreeIndex]:
        # Split the conversations into two lists
        less_than_target, greater_than_target = self.builder.create_conversation_trees(
            target_num
        )

        # Combine the smaller conversations
        combined_conversation = self.combine_conversations(less_than_target)

        # Add the combined conversation to the list of larger conversations
        if combined_conversation is not None:
            combined_tree_index = ChainTreeIndex(conversation=combined_conversation)
            greater_than_target.append(combined_tree_index)

        return greater_than_target

    def combine_conversations(
        self,
        conversations_to_combine: Optional[List[ChainTree]] = None,
        title_range: Optional[Tuple[int, int]] = None,
    ) -> Optional[ChainTree]:
        """
        Combine multiple conversations into a single conversation.

        :param conversations_to_combine: list of conversations to be combined
        :param title_range: tuple specifying the range of titles to be included in the combined conversation
        :return: a combined conversation
        """
        if conversations_to_combine is None:
            self.logger.info(
                "No specific conversations provided, using all conversations."
            )
            conversations_to_combine = self.conversations

        if title_range is None:
            title_range = (0, len(conversations_to_combine))

        self.logger.info(
            f"Combining conversations with titles in the range {title_range}."
        )

        for conversation in conversations_to_combine:
            self.logger.debug(f"Processing conversation {conversation.title}")
            try:
                title = int(conversation.title)
                if title_range[0] <= title < title_range[1]:
                    self._combine_conversation(conversation)
            except ValueError:
                self.logger.error(
                    f"Invalid title for conversation: {conversation.title}. Skipping this conversation."
                )
                continue
            except Exception as e:
                self.logger.error(
                    f"Unexpected error while processing conversation {conversation.title}: {str(e)}. Skipping this conversation."
                )
                continue

        combined_conversation = self._finalize_combined_conversation()
        if combined_conversation is not None:
            self.logger.info(
                f"Successfully combined {len(conversations_to_combine)} conversations."
            )
        else:
            self.logger.warning(
                f"No conversations were combined. Please check the input and try again."
            )

        return combined_conversation

    def _finalize_combined_conversation(self) -> Optional[ChainTree]:
        """
        Finalize the combined conversation by updating the mapping and saving the result.

        :return: the combined conversation, or None if there was no conversation to combine
        """
        if self._combined_conversation is not None:
            self.logger.info("Finalizing the combined conversation.")
            self._combined_conversation.mapping = self.builder._combined_mapping
            self.builder.save_json(
                self.builder.save_path, [self._combined_conversation.dict()]
            )
            self.builder._save_adjacency_list()
        else:
            self.logger.warning(
                "There was no conversation to combine. The combined conversation is None."
            )

        return self._combined_conversation

    def _combine_conversation(self, conversation: ChainTree):
        """
        Combine the provided conversation into the combined conversation.

        :param conversation: Conversation to be combined
        """
        if self._combined_conversation is None:
            self._combined_conversation = conversation
        else:
            self.builder._combined_mapping.update(conversation.mapping)
            self.builder._process_system_messages(conversation)
            self.builder._update_adjacency_list(conversation)

    def _process_conversation_trees(
        self,
        use_graph: bool = False,
        use_graph_index=None,
        tree_range: Optional[Tuple[int, int]] = (0, None),
        skip_indexes: Optional[List[int]] = None,
    ):
        if use_graph_index is not None and not isinstance(use_graph_index, int):
            raise ValueError("use_graph_index should be an integer or None.")

        if not self.conversation_trees:
            raise ValueError("No conversation trees to process.")

        start, end = tree_range
        if end is None:
            end = len(self.conversation_trees)

        # Filter out the conversations that are in the skip_indexes list
        if skip_indexes is not None:
            filtered_trees = [
                ct
                for i, ct in enumerate(self.conversation_trees[start:end])
                if i not in skip_indexes
            ]
        else:
            filtered_trees = self.conversation_trees[start:end]

        total_trees = len(filtered_trees)

        for idx, conversation_tree in enumerate(filtered_trees):
            if not isinstance(conversation_tree, ChainTreeIndex):
                raise ValueError(
                    "Invalid conversation_tree type, should be instance of ConversationTree."
                )
            tetra = CoordinateRepresentation(conversation_tree)
            tree_depth = tetra.depth

            if self.chain_filter is not None:
                filtered_tree = self.chain_filter.is_valid(
                    idx, total_trees, conversation_tree, tree_depth
                )
                if not filtered_tree:
                    continue
                conversation_tree = filtered_tree  # use the filtered tree

            use_graph = idx == use_graph_index

            tetra_dict = tetra._procces_coordnates(use_graph)

            print(f"Processing tree {idx + 1} of {total_trees}...")

            tetra.handler.add_local_embeddings(tetra_dict)

        main_df = tetra.handler.create_and_persist_dataframes()

        return main_df

    def process_conversation_trees(
        self,
        use_graph: bool = False,
        use_graph_index=None,
        tree_range: Optional[Tuple[int, int]] = (0, None),
        skip_indexes: Optional[List[int]] = None,
    ):
        """
        Process the conversation trees.

        :param use_graph: whether to use the graph representation
        :param use_graph_index: index of the conversation tree to use for the graph representation
        :param tree_range: range of conversation trees to process
        :param skip_indexes: indexes of the conversation trees to skip
        """
        main_df = self._process_conversation_trees(
            use_graph=use_graph,
            use_graph_index=use_graph_index,
            tree_range=tree_range,
            skip_indexes=skip_indexes,
        )
        return main_df
