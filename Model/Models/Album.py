from Model.Models.MuzickiElement import MuzickiElement

class Album(MuzickiElement):
    def __init__(self, id: int, naziv: str, slika: str, pregledi: int, broj_ocena: int, zbir_ocena: int, muzicka_dela: list):
        super().__init__(id, naziv, slika, pregledi, broj_ocena, zbir_ocena)
        self.muzicka_dela = muzicka_dela
