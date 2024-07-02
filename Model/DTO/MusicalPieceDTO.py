from Model.Models.Grupa import Grupa
from Model.DTO.MusicalElementDTO import MusicalElementDTO

class MusicalPieceDTO(MusicalElementDTO):
    def __init__(self, id: int, naziv: str, slika: str, tekst: str, pregledi: int, broj_ocena: int, zbir_ocena: int, grupa: Grupa):
        super().__init__(id, naziv, slika, pregledi, broj_ocena, zbir_ocena)
        self._tekst = tekst
        self._grupa = grupa
    
    @property
    def tekst(self):
        return self._tekst

    @tekst.setter
    def tekst(self, value):
        self._tekst = value

    @property
    def grupa(self):
        return self._grupa

    @grupa.setter
    def grupa(self, value):
        self._grupa = value
