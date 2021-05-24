from typing import List

from Models.MFModels.transaction import Transaction


class Fund:

    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.transactions = list()

    pass
