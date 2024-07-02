from Model.Models.MuzickiElement import MuzickiElement

class RecenzijaUrednika:
    def __init__(self, opis: str, ocena: int, menja_se: bool, muzicki_element: MuzickiElement):
        self.opis = opis
        self.ocena = ocena
        self.menja_se = menja_se
        self.muzicki_element = muzicki_element

    @property
    def opis(self):
        return self._opis

    @opis.setter
    def opis(self, value):
        self._opis = value

    @property
    def ocena(self):
        return self._ocena

    @ocena.setter
    def ocena(self, value):
        self._ocena = value

    @property
    def menja_se(self):
        return self._menja_se

    @menja_se.setter
    def menja_se(self, value):
        self._menja_se = value

    @property
    def muzicki_element(self):
        return self._muzicki_element

    @muzicki_element.setter
    def muzicki_element(self, value):
        self._muzicki_element = value