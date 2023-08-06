from typing import *

from pydantic import BaseModel, Field


class Bill(BaseModel):
    """
    Bill model

    """

    bill_number: str = Field(alias="bill_number")

    chapter_number: Optional[Union[str, Any]] = Field(alias="chapter_number", default=None)

    crossfile_bill_number: Optional[Union[str, Any]] = Field(alias="crossfile_bill_number", default=None)

    sponsor_primary: str = Field(alias="sponsor_primary")

    sponsors: Optional[List[Dict[str, Any]]] = Field(alias="sponsors", default=None)

    synopsis: str = Field(alias="synopsis")

    title: str = Field(alias="title")

    house: str = Field(alias="house")

    status: Optional[Union[str, Any]] = Field(alias="status", default=None)

    committee_primary_origin: Optional[Union[str, Any]] = Field(alias="committee_primary_origin", default=None)

    committee_secondary_origin: Optional[Union[str, Any]] = Field(alias="committee_secondary_origin", default=None)

    committee_primary_opposite: Optional[Union[str, Any]] = Field(alias="committee_primary_opposite", default=None)

    committee_secondary_opposite: Optional[Union[str, Any]] = Field(alias="committee_secondary_opposite", default=None)

    first_reading_date_house_of_origin: Optional[Union[str, Any]] = Field(
        alias="first_reading_date_house_of_origin", default=None
    )

    hearing_date_time_primary_house_of_origin: Optional[Union[str, Any]] = Field(
        alias="hearing_date_time_primary_house_of_origin", default=None
    )

    hearing_date_time_secondary_house_of_origin: Optional[Union[str, Any]] = Field(
        alias="hearing_date_time_secondary_house_of_origin", default=None
    )

    report_date_house_of_origin: Optional[Union[str, Any]] = Field(alias="report_date_house_of_origin", default=None)

    report_action_house_of_origin: Optional[Union[str, Any]] = Field(
        alias="report_action_house_of_origin", default=None
    )

    second_reading_date_house_of_origin: Optional[Union[str, Any]] = Field(
        alias="second_reading_date_house_of_origin", default=None
    )

    second_reading_action_house_of_origin: Optional[Union[str, Any]] = Field(
        alias="second_reading_action_house_of_origin", default=None
    )

    third_reading_date_house_of_origin: Optional[Union[str, Any]] = Field(
        alias="third_reading_date_house_of_origin", default=None
    )

    third_reading_action_house_of_origin: Optional[Union[str, Any]] = Field(
        alias="third_reading_action_house_of_origin", default=None
    )

    first_reading_date_opposite_house: Optional[Union[str, Any]] = Field(
        alias="first_reading_date_opposite_house", default=None
    )

    hearing_date_time_primary_opposite_house: Optional[Union[str, Any]] = Field(
        alias="hearing_date_time_primary_opposite_house", default=None
    )

    hearing_date_time_secondary_opposite_house: Optional[Union[str, Any]] = Field(
        alias="hearing_date_time_secondary_opposite_house", default=None
    )

    report_date_opposite_house: Optional[Union[str, Any]] = Field(alias="report_date_opposite_house", default=None)

    report_action_opposite_house: Optional[Union[str, Any]] = Field(alias="report_action_opposite_house", default=None)

    second_reading_date_opposite_house: Optional[Union[str, Any]] = Field(
        alias="second_reading_date_opposite_house", default=None
    )

    second_reading_action_opposite_house: Optional[Union[str, Any]] = Field(
        alias="second_reading_action_opposite_house", default=None
    )

    third_reading_date_opposite_house: Optional[Union[str, Any]] = Field(
        alias="third_reading_date_opposite_house", default=None
    )

    third_reading_action_opposite_house: Optional[Union[str, Any]] = Field(
        alias="third_reading_action_opposite_house", default=None
    )

    interaction_between_chambers: Optional[Union[str, Any]] = Field(alias="interaction_between_chambers", default=None)

    passed_by_mga: Optional[Union[bool, Any]] = Field(alias="passed_by_mga", default=None)

    emergency_bill: Optional[Union[bool, Any]] = Field(alias="emergency_bill", default=None)

    constitutional_amendment: Optional[Union[bool, Any]] = Field(alias="constitutional_amendment", default=None)

    broad_subjects: Optional[Union[List[Dict[str, Any]], Any]] = Field(alias="broad_subjects", default=None)

    narrow_subjects: Optional[Union[List[Dict[str, Any]], Any]] = Field(alias="narrow_subjects", default=None)

    bill_type: Optional[Union[str, Any]] = Field(alias="bill_type", default=None)

    bill_version: Optional[Union[str, Any]] = Field(alias="bill_version", default=None)

    statutes: Optional[Union[List[Dict[str, Any]], Any]] = Field(alias="statutes", default=None)

    year_and_session: Optional[Union[str, Any]] = Field(alias="year_and_session", default=None)

    status_current_as_of: Union[str, Any] = Field(alias="status_current_as_of")

    state: Optional[Union[str, Any]] = Field(alias="state", default=None)
