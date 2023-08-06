from __future__ import annotations
from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel
from enum import Enum
from dataclasses import dataclass, field
from jax import numpy as jnp
import numpy as np


class ContentType(str, Enum):
    """
    Represents the type of  message content.
    Attributes:
        TEXT (str): A text message content..
        IMAGE (str): An image message content..
        AUDIO (str): An audio message content..
        VIDEO (str): A video message content..
        FILE (str): A file message content..
        LOCATION (str): A location message content..
        CONTACT (str): A contact message content..
        LINK (str): A link message content..
        EVENT (str): An event message content..
        OTHER (str): A message content. of another type.
    """

    TEXT = "text"
    IMAGE = "image"
    AUDIO = "audio"
    VIDEO = "video"
    FILE = "file"
    LOCATION = "location"
    CONTACT = "contact"
    MESSAGE = "message"
    LINK = "link"
    EVENT = "event"
    DIRECTORY = "directory"
    OTHER = "other"
