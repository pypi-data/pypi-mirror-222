from typing import *

from pydantic import BaseModel, Field


class Message(BaseModel):
    """
    Message model

    """

    message: str = Field(alias="message")
