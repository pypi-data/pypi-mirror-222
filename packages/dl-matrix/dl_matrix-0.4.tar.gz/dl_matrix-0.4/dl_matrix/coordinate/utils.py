from typing import Any, Tuple
import numpy as np
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine
from sentence_transformers import SentenceTransformer
import torch.nn.functional as F
from scipy.spatial import distance

model = SentenceTransformer("all-mpnet-base-v2")


def get_bert_embedding(text):
    """
    Get BERT embeddings for the given text.

    Args:
        text: The input text.

    Returns:
        The BERT embeddings for the input text.
    """
    return model.encode([text])[0]


def cross_entropy(p, q):
    """
    Calculate the cross entropy between two distributions.

    Args:
        p: The first distribution.
        q: The second distribution.

    Returns:
        The cross entropy between the two distributions.
    """
    q = q + 1e-9  # Add a small constant to avoid taking the logarithm of zero
    return -np.sum(np.multiply(p, np.log2(q)))


def avg_cross_entropy(node1, node2):
    """
    Calculate the average cross entropy between the BERT embeddings of two nodes.

    Args:
        node1: The first node.
        node2: The second node.

    Returns:
        The average cross entropy between the BERT embeddings of the two nodes.
    """
    return (cross_entropy(node1[1], node2[1]) + cross_entropy(node2[1], node1[1])) / 2


def should_connect_bert_cross_entropy(
    node1: Tuple[Any, ...], node2: Tuple[Any, ...], threshold: float = 0.5
) -> bool:
    """
    Determine whether two nodes should be connected based on the average cross entropy between their BERT embeddings.

    Args:
        node1: The first node.
        node2: The second node.
        threshold: The cross-entropy threshold.

    Returns:
        True if the average cross entropy between the BERT embeddings of the two nodes is less than the threshold, False otherwise.
    """
    return avg_cross_entropy(node1, node2) < threshold


def should_connect_default(node1: Tuple[Any, ...], node2: Tuple[Any, ...]) -> bool:
    """
    Default function to determine whether two nodes should be connected.

    Args:
        node1: The first node.
        node2: The second node.

    Returns:
        True, since by default all nodes should be connected.
    """
    return True


def calculate_weight_sum(node1: Tuple[Any, ...], node2: Tuple[Any, ...]) -> int:
    """
    Default function to calculate edge weight as the sum of node values.

    Args:
        node1: The first node.
        node2: The second node.

    Returns:
        The sum of the node values.
    """
    return sum(node1[1:]) + sum(node2[1:])


def calculate_weight_sum_squares(node1: Tuple[Any, ...], node2: Tuple[Any, ...]) -> int:
    """Calculate the weight of an edge as the sum of the squares of the node values."""
    return sum(value**2 for value in node1[1:] + node2[1:])


def custom_should_connect(node1: Tuple[Any, ...], node2: Tuple[Any, ...]) -> bool:
    """
    Custom function to determine whether two nodes should be connected.
    Connects nodes if their first values are even.

    Args:
        node1: The first node.
        node2: The second node.

    Returns:
        True if the first values of both nodes are even, False otherwise.
    """
    return node1[1] % 2 == 0 and node2[1] % 2 == 0


def custom_calculate_weight(node1: Tuple[Any, ...], node2: Tuple[Any, ...]) -> int:
    """
    Custom function to calculate the weight of an edge.
    Calculates weight as the product of the first values of the nodes.

    Args:
        node1: The first node.
        node2: The second node.

    Returns:
        The product of the first values of the nodes.
    """
    return node1[1] * node2[1]


def should_connect_same_first_letter(
    node1: Tuple[Any, ...], node2: Tuple[Any, ...]
) -> bool:
    """
    Determine whether two nodes should be connected based on their identifiers.

    Connects nodes if their first values start with the same letter.

    Args:
        node1: The first node.
        node2: The second node.

    Returns:
        True if the first values of both nodes start with the same letter, False otherwise.

    """
    return node1[0][0] == node2[0][0]


def both_values_are_odd(node1: Tuple[Any, ...], node2: Tuple[Any, ...]) -> bool:
    """
    Connects nodes if their first values are odd.

    Args:
        node1: The first node.
        node2: The second node.

    Returns:
        True if the first values of both nodes are odd, False otherwise.
    """
    return node1[1] % 2 != 0 and node2[1] % 2 != 0


def values_sum_to_even(node1: Tuple[Any, ...], node2: Tuple[Any, ...]) -> bool:
    """
    Connects nodes if the sum of their first values is even.

    Args:
        node1: The first node.
        node2: The second node.

    Returns:
        True if the sum of the first values of the nodes is even, False otherwise.
    """
    return (node1[1] + node2[1]) % 2 == 0


def values_are_within_range(node1: Tuple[Any, ...], node2: Tuple[Any, ...]) -> bool:
    """
    Connects nodes if the absolute difference between their first values is less than 3.

    Args:
        node1: The first node.
        node2: The second node.

    Returns:
        True if the absolute difference between the first values of the nodes is less than 3, False otherwise.
    """
    return abs(node1[1] - node2[1]) < 3


def both_values_are_primes(node1: Tuple[Any, ...], node2: Tuple[Any, ...]) -> bool:
    """
    Connects nodes if their first values are both prime numbers.

    Args:
        node1: The first node.
        node2: The second node.

    Returns:
        True if the first values of both nodes are prime numbers, False otherwise.
    """

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False

        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False

        return True

    return is_prime(node1[1]) and is_prime(node2[1])


def custom_should_connect_close_values(
    node1: Tuple[Any, ...], node2: Tuple[Any, ...]
) -> bool:
    """
    Custom function to determine whether two nodes should be connected.
    Connects nodes if the absolute difference between their first values is less than or equal to 5.

    Args:
        node1: The first node.
        node2: The second node.

    Returns:
        True if the absolute difference between the first values of both nodes is less than or equal to 5, False otherwise.
    """
    return abs(node1[1] - node2[1]) <= 5


def should_connect_contains_substring(
    node1: Tuple[Any, ...], node2: Tuple[Any, ...], substring: str = "a"
) -> bool:
    """
    Connects nodes if their identifiers contain the given substring.

    Args:
        node1: The first node.
        node2: The second node.
        substring: The substring to check for.

    Returns:
        True if the nodes' identifiers contain the substring, False otherwise.
    """
    return substring in node1[0] and substring in node2[0]


def custom_should_connect_greater_than_ten(
    node1: Tuple[Any, ...], node2: Tuple[Any, ...]
) -> bool:
    """
    Custom function to determine whether two nodes should be connected.
    Connects nodes if their first values are both greater than 10.

    Args:
        node1: The first node.
        node2: The second node.

    Returns:
        True if the first values of both nodes are greater than 10, False otherwise.
    """
    return node1[1] > 10 and node2[1] > 10


def custom_should_connect_sum_even(
    node1: Tuple[Any, ...], node2: Tuple[Any, ...]
) -> bool:
    """
    Custom function to determine whether two nodes should be connected.
    Connects nodes if the sum of their first values is even.

    Args:
        node1: The first node.
        node2: The second node.

    Returns:
        True if the sum of the first values of both nodes is even, False otherwise.
    """
    return (node1[1] + node2[1]) % 2 == 0


def should_connect_sum_greater_than(
    node1: Tuple[Any, ...], node2: Tuple[Any, ...], threshold: int = 10
) -> bool:
    """
    Connects nodes if the sum of their values is greater than the given threshold.

    Args:
        node1: The first node.
        node2: The second node.
        threshold: The value threshold.

    Returns:
        True if the sum of the nodes' values is greater than the threshold, False otherwise.
    """
    return sum(node1[1:]) + sum(node2[1:]) > threshold


def should_connect_same_length(node1: Tuple[Any, ...], node2: Tuple[Any, ...]) -> bool:
    """
    Connects nodes if their identifiers have the same length.

    Args:
        node1: The first node.
        node2: The second node.

    Returns:
        True if the length of both nodes' identifiers is the same, False otherwise.
    """
    return len(node1[0]) == len(node2[0])


def semantic_similarity(sentence1, sentence2):
    # Encode sentences to get their embeddings
    embedding1 = model.encode(sentence1, convert_to_tensor=True)
    embedding2 = model.encode(sentence2, convert_to_tensor=True)

    # Compute cosine similarity between embeddings
    cosine_similarity = 1 - cosine(embedding1, embedding2)

    return cosine_similarity


# Custom condition for connection
def should_connect_custom_sim(node1, node2):
    return node1[0][0] == node2[0][0] and semantic_similarity(node1[0], node2[0]) > 0.7


def should_connect_semantic_and_distance(
    node1: Tuple[Any, ...], node2: Tuple[Any, ...]
) -> bool:
    node1_str = str(node1[0])
    node2_str = str(node2[0])

    if semantic_similarity(node1_str, node2_str) > 0.8:
        if abs(node1[1] - node2[1]) < 10:
            return True
    return False


def calculate_weight_bert_distance(
    node1: Tuple[Any, ...], node2: Tuple[Any, ...]
) -> int:
    # Encode the sentences to get their embeddings
    embedding1 = model.encode(node1[0], convert_to_tensor=True)
    embedding2 = model.encode(node2[0], convert_to_tensor=True)

    # Compute Euclidean distance between the embeddings
    dist = distance.euclidean(embedding1, embedding2)

    return dist


def semantic_similarity_cross_entropy_adjusted(sentence1: str, sentence2: str):
    # Encode sentences to get their embeddings
    embedding1 = model.encode(sentence1, convert_to_tensor=True)
    embedding2 = model.encode(sentence2, convert_to_tensor=True)

    # Convert embeddings into probability distributions
    prob_dist1 = F.softmax(embedding1, dim=0)
    prob_dist2 = F.softmax(embedding2, dim=0)

    # Compute cross-entropy
    cross_entropy_loss = F.kl_div(
        F.log_softmax(prob_dist1, dim=0), prob_dist2, reduction="sum"
    )

    # Compute cosine similarity between embeddings
    cosine_sim = 1 - cosine(embedding1.detach().numpy(), embedding2.detach().numpy())

    # Adjust cosine similarity with inverse of cross entropy
    adjusted_cosine_sim = cosine_sim / (1 + cross_entropy_loss.item())

    return adjusted_cosine_sim


def semantic_similarity_cross_entropy(sentence1: str, sentence2: str):
    # Encode sentences to get their embeddings
    embedding1 = model.encode(sentence1, convert_to_tensor=True)
    embedding2 = model.encode(sentence2, convert_to_tensor=True)

    # Convert embeddings into probability distributions
    prob_dist1 = F.softmax(embedding1, dim=0)
    prob_dist2 = F.softmax(embedding2, dim=0)

    # Compute cross-entropy
    cross_entropy_loss = F.kl_div(
        F.log_softmax(prob_dist1, dim=0), prob_dist2, reduction="sum"
    )

    return cross_entropy_loss.item()


def should_connect_semantic(node1: Tuple[Any, ...], node2: Tuple[Any, ...]) -> bool:
    sentence1 = node1[0]
    sentence2 = node2[0]
    cross_entropy_threshold = 0.5
    cosine_similarity_threshold = 0.8

    if (
        semantic_similarity_cross_entropy(sentence1, sentence2)
        < cross_entropy_threshold
        and semantic_similarity(sentence1, sentence2) > cosine_similarity_threshold
    ):
        return True
    else:
        return False
