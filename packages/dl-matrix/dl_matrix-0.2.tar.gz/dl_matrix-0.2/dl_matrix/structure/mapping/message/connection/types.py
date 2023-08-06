from enum import Enum


class ConnectionType(str, Enum):
    REPLY_TO = "REPLY_TO"
    MENTION = "MENTION"
    QUOTE = "QUOTE"
    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"
    SIMILAR_TO = "SIMILAR_TO"
    RESPONSE_TO = "RESPONSE_TO"
    QUESTION_TO = "QUESTION_TO"
    COUNTER = "COUNTER"


class ConnectionStrength(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
