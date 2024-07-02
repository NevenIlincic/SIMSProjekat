from Model.DTO.MusicalElementDTO import MusicalElementDTO

class AlbumDTO(MusicalElementDTO):
    def __init__(self, id: int, naziv: str, slika: str, pregledi: int, broj_ocena: int, zbir_ocena: int, muzicka_dela: list):
        super().__init__(id, naziv, slika, pregledi, broj_ocena, zbir_ocena)
        self._muzicka_dela = muzicka_dela
    
    @property
    def muzicka_dela(self):
        return self._muzicka_dela

    @muzicka_dela.setter
    def muzicka_dela(self, value):
        self._muzicka_dela = value
