import enum

from datetime import date


class Type(enum.Enum):
    BUY = "buy"
    SELL = "sell"


class Transaction:

    def __init__(self,dateOfTransaction,type,price,unitsAlloted):
        self.type: str = type
        self.unitsAllotted: float = unitsAlloted
        self.price: float = price
        self.dateOfTransaction: date = dateOfTransaction
    pass
