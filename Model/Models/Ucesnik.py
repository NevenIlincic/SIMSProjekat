from Model.Models.MuzickiElement import MuzickiElement
from Model.Models.Enumerations import Pol
from datetime import date

class Ucesnik(MuzickiElement):
    def __init__(self, id: int, naziv: str, slika: str, pregledi: int, broj_ocena: int, zbir_ocena: int, ime: str, prezime: str, pol: Pol, datum_rodjenja: date, biografija: str, zanrovi: list[str], reklamira_se: bool):
        super().__init__(id, naziv, slika, pregledi, broj_ocena, zbir_ocena)
        self.ime = ime
        self.prezime = prezime
        self.pol = pol
        self.datum_rodjenja = datum_rodjenja
        self.biografija = biografija
        self.zanrovi = zanrovi
        self.reklamira_se = reklamira_se
        
    @property
    def ime(self):
        return self._ime

    @ime.setter
    def ime(self, value):
        self._ime = value

    @property
    def prezime(self):
        return self._prezime

    @prezime.setter
    def prezime(self, value):
        self._prezime = value

    @property
    def pol(self):
        return self._pol

    @pol.setter
    def pol(self, value):
        self._pol = value

    @property
    def datum_rodjenja(self):
        return self._datum_rodjenja

    @datum_rodjenja.setter
    def datum_rodjenja(self, value):
        self._datum_rodjenja = value

    @property
    def biografija(self):
        return self._biografija

    @biografija.setter
    def biografija(self, value):
        self._biografija = value

    @property
    def zanrovi(self):
        return self._zanrovi

    @zanrovi.setter
    def zanrovi(self, value):
        self._zanrovi = value

    @property
    def reklamira_se(self):
        return self._reklamira_se

    @reklamira_se.setter
    def reklamira_se(self, value):
        self._reklamira_se = value