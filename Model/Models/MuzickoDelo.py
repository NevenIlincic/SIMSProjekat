from Model.Models.MuzickiElement import MuzickiElement
from Model.Models.Grupa import Grupa

class MuzickoDelo(MuzickiElement):
    def __init__(self, naziv: str, slika: str, tekst: str, pregledi: int, broj_ocena: int, zbir_ocena: int, grupa: Grupa):
        super().__init__(naziv, slika, pregledi, broj_ocena, zbir_ocena)
        self.tekst = tekst
        self.grupa = grupa
        
    def reprodukuj_delo(self, je_registrovan: bool):
        pass
