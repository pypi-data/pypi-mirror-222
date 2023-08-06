from __future__ import annotations
from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel
from enum import Enum
from dataclasses import dataclass, field
from jax import numpy as jnp
import numpy as np


class RoleType(str, Enum):
    USER = "user"
    CHAT = "chat"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    ADMIN = "admin"
    GUEST = "guest"
    ANONYMOUS = "anonymous"
    MODERATOR = "moderator"
    OWNER = "owner"
    DEVELOPER = "developer"
    CREATOR = "creator"
