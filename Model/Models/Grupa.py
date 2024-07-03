from Model.Models.MuzickiElement import MuzickiElement

class Grupa(MuzickiElement):
    def __init__(self, id: int, naziv: str, slika: str, pregledi: int, broj_ocena: int, zbir_ocena: int, ucesnici: list):
        super().__init__(id, naziv, slika, pregledi, broj_ocena, zbir_ocena)
        self.ucesnici = ucesnici

        