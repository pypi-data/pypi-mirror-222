from typing import *

from pydantic import BaseModel, Field

from .Member import Member


class Committee(BaseModel):
    """
    Committee model

    """

    name: str = Field(alias="name")

    chair: Optional[Union[Member, Any]] = Field(alias="chair", default=None)

    vice_chair: Optional[Union[Member, Any]] = Field(alias="vice_chair", default=None)

    email: Optional[Union[str, Any]] = Field(alias="email", default=None)

    website: str = Field(alias="website")
