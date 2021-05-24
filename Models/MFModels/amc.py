from typing import List

from Models.MFModels.folio import Folio


class Amc:

    def __init__(self, name):
        self.name: str = name
        self.folios: List[Folio] = list()

    pass
