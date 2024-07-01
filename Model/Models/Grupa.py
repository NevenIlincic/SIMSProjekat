from Model.Models.MuzickiElement import MuzickiElement

class Grupa(MuzickiElement):
    def __init__(self, naziv: str, slika: str, tekst: str, pregledi: int, broj_ocena: int, zbir_ocena: int, ucesnici: list):
        super().__init__(naziv, slika, tekst, pregledi, broj_ocena, zbir_ocena)
        self.ucesnici = ucesnici

        