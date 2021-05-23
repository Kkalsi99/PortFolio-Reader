import enum

from datetime import date


class Type(enum):
    BUY = "buy"
    SELL = "sell"


class Transaction:
    type: Type
    unitsAllotted: float
    price: float
    dateOfTransaction: date
    pass
