from Model.Models.Korisnik import Korisnik
from Model.Models.Enumerations import Pol
from Model.Models.KorisnickiNalog import KorisnickiNalog

class MuzickiUrednik(Korisnik):
    def __init__(self, id: int, ime: str, prezime: str, pol: Pol, blokiran: bool, zadaci: list, recenzije: list, korisnicki_nalog: KorisnickiNalog ):
        super().__init__(id, ime, prezime, pol, blokiran, korisnicki_nalog)
        self.id = id
        self.zadaci = zadaci
        self.recenzije = recenzije
    
    def dodaj_izvodjaca(self, izvodjac):
        pass

    def dodaj_muzicko_delo(self, delo):
        pass

    def dodaj_dogadjaj(self, izvodjenje):
        pass

    def dodaj_album(self, album):
        pass

    def dodaj_grupu(self, grupa):
        pass

    def dodaj_recenziju(self, recenzija):
        pass

    def pregledaj_zadatke(self):
        pass

    def izmena_stranice(self, je_dozvoljena: bool):
        pass

