from Model.Models.MuzickiElement import MuzickiElement

class RecenzijaUrednika:
    def __init__(self, id: int, opis: str, ocena: int, menja_se: bool, muzicki_element: MuzickiElement, vrsta_elementa: str):
        self.id = id
        self.opis = opis
        self.ocena = ocena
        self.menja_se = menja_se
        self.muzicki_element = muzicki_element
        self.vrsta_elementa = vrsta_elementa

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

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

    @property
    def vrsta_elementa(self):
        return self._vrsta_elementa

    @vrsta_elementa.setter
    def vrsta_elementa(self, value):
        self._vrsta_elementa = value