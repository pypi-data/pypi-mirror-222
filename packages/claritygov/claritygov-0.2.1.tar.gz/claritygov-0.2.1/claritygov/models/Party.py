from enum import Enum


class Party(str, Enum):
    democrat = "Democrat"
    republican = "Republican"
    independent = "Independent"
    other = "Other"
