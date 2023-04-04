from enum import Enum


class Size(str, Enum):
    SMALL = "SMALL"
    MID = "MID"
    LARGE = "LARGE"


class Age(str, Enum):
    LESS_THAN_ONE = "LESS_THAN_ONE"
    BETWEEN_ONE_AND_SEVEN = "BETWEEN_ONE_AND_SEVEN"
    GREATHER_THAN_SEVEN = "GREATHER_THAN_SEVEN"


class Species(str, Enum):
    CAT = "CAT"
    DOG = "DOG"


class Sex(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class Temper(str, Enum):
    SHY = "SHY"
    DOCILE = "DOCILE"
    AGGRESSIVE = "AGGRESSIVE"


class AdoptionStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    NOT_AVAILABLE = "NOT_AVAILABLE"
    ADOPTED = "ADOPTED"


class HealthStatus(str, Enum):
    HEALTHY = "HEALTHY"
    SICK = "SICK"
    INJURIED = "INJURIED"
    DEAD = "DEAD"
