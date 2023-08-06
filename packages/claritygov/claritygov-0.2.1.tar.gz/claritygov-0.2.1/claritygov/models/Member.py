from typing import *

from pydantic import BaseModel, Field

from .Party import Party


class Member(BaseModel):
    """
    Member model

    """

    first_name: str = Field(alias="first_name")

    last_name: str = Field(alias="last_name")

    full_name: str = Field(alias="full_name")

    party: Party = Field(alias="party")
