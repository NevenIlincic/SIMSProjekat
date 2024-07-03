from Model.Models.Korisnik import Korisnik
from Model.Models.Enumerations import Pol
from Model.Models.KorisnickiNalog import KorisnickiNalog

class MuzickiUrednik(Korisnik):
    def __init__(self, id: int, ime: str, prezime: str, pol: Pol, blokiran: bool, zadaci: list, recenzije: list, korisnicki_nalog: KorisnickiNalog ):
        super().__init__(id, ime, prezime, pol, blokiran, korisnicki_nalog)
        self.id = id
        self.zadaci = zadaci
        self.recenzije = recenzije
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def zadaci(self):
        return self._zadaci

    @zadaci.setter
    def zadaci(self, value):
        self._zadaci = value

    @property
    def recenzije(self):
        return self._recenzije
    
    @recenzije.setter
    def recenzije(self, value):
        self._recenzije = value
