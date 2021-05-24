import enum

from datetime import date


class Type(enum.Enum):
    BUY = "buy"
    SELL = "sell"


class Transaction:

    def __init__(self,type,unitsAlloted,price,dateOfTransaction):
        self.type : Type = type
        self.unitsAllotted: float = unitsAlloted
        self.price: float = price
        self.dateOfTransaction: date = dateOfTransaction
    pass
