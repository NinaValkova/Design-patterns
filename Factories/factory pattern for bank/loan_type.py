from enum import Enum, auto


class LoanType(Enum):
    HOME = auto()
    BUSINESS = auto()
    EDUCATION = auto()