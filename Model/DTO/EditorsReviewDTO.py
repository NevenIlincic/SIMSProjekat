from Model.Models.MuzickiElement import MuzickiElement

class EditorsReviewDTO:
    def __init__(self, id : int, opis: str, ocena: int, menja_se: bool, muzicki_element: MuzickiElement):
        self._id = id
        self._opis = opis
        self._ocena = ocena
        self._menja_se = menja_se
        self._muzicki_element = muzicki_element

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
