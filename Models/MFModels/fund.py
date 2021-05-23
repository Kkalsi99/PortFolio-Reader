from Models.MFModels.transaction import Transaction


class Fund:
    name: str
    code: str
    transactions: list[Transaction]
    pass
