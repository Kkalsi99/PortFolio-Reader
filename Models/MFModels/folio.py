from Models.MFModels.fund import Fund
from typing import List


class Folio:


    def __init__(self, folioNumber):
        self.folioNumber: str = folioNumber
        self.funds: List[Fund] = list()

    pass
