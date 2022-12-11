from enum import Enum


class TimeInterval(Enum):
    three_min = "3 min"
    six_hours = "6 hr"
    twelve_hours = "12 hr"


class SetupStatus(Enum):
    active = "Active"
    disabled = "Disabled"
