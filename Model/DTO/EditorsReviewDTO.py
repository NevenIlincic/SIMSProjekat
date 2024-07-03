from Model.Models.MuzickiElement import MuzickiElement

class EditorsReviewDTO:
    def __init__(self, opis: str, ocena: int, muzicki_element: MuzickiElement):
        self._opis = opis
        self._ocena = ocena
        self._muzicki_element = muzicki_element
        

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
    def muzicki_element(self):
        return self._muzicki_element

    @muzicki_element.setter
    def muzicki_element(self, value):
        self._muzicki_element = value
