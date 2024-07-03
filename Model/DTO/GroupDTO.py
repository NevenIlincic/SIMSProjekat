from Model.DTO.MusicalElementDTO import MusicalElementDTO

class GroupDTO(MusicalElementDTO):
    def __init__(self, naziv: str, slika: str, pregledi: int, broj_ocena: int, zbir_ocena: int, tekst: str, ucesnici: list):
        super().__init__(naziv, slika, pregledi, broj_ocena, zbir_ocena)
        self._tekst = tekst
        self._ucesnici = ucesnici
    
    @property
    def tekst(self):
        return self._tekst

    @tekst.setter
    def tekst(self, value):
        self._tekst = value

    @property
    def ucesnici(self):
        return self._ucesnici

    @ucesnici.setter
    def ucesnici(self, value):
        self._ucesnici = value
