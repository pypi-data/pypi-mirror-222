from typing import *

from pydantic import BaseModel, Field

from .Member import Member


class CommitteeVote(BaseModel):
    """
    CommitteeVote model

    """

    date: str = Field(alias="date")

    session: int = Field(alias="session")

    bill_number: str = Field(alias="bill_number")

    result: str = Field(alias="result")

    yeas: int = Field(alias="yeas")

    nays: int = Field(alias="nays")

    abstain: int = Field(alias="abstain")

    excused: int = Field(alias="excused")

    absent: int = Field(alias="absent")

    yeas_members: Union[List[Member], Any] = Field(alias="yeas_members")

    nays_members: Union[List[Member], Any] = Field(alias="nays_members")

    abstain_members: Union[List[Member], Any] = Field(alias="abstain_members")

    excused_members: Union[List[Member], Any] = Field(alias="excused_members")

    absent_members: Union[List[Member], Any] = Field(alias="absent_members")

    chamber: str = Field(alias="chamber")

    committee: Union[str, Any] = Field(alias="committee")
