from Model.Models.MuzickiElement import MuzickiElement
from Model.Models.Enumerations import Pol

class Ucesnik(MuzickiElement):
    def __init__(self, naziv: str, slika: str, tekst: str, pregledi: int, broj_ocena: int, zbir_ocena: int, ime: str, prezime: str, pol: Pol, datum_rodjenja: str, biografija: str, zanrovi: list[str], reklamira_se: bool):
        super().__init__(naziv, slika, tekst, pregledi, broj_ocena, zbir_ocena)
        self.ime = ime
        self.prezime = prezime
        self.pol = pol
        self.datum_rodjenja = datum_rodjenja
        self.biografija = biografija
        self.zanrovi = zanrovi
        self.reklamira_se = reklamira_se
