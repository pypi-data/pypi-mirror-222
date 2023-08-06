"""
Lobsang provides a simple interaction interface with a dialog-based LLM.
Please see the README for more information.

https://thelongearth.fandom.com/wiki/Lobsang
"""

import importlib.metadata

__version__ = importlib.metadata.version(__package__ or __name__)
__all__ = ["Chat", "UserMessage", "AssistantMessage", "SystemMessage"]

from lobsang.chat import Chat
from lobsang.messages import UserMessage, AssistantMessage, SystemMessage
