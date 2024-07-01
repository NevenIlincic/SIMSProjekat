from Korisnik import Korisnik
from Enumerations import Pol

class MuzickiUrednik(Korisnik):
    def __init__(self, korisnicko_ime: str, lozinka: str, ime: str, prezime: str, pol: Pol, blokiran: bool, zadaci: list, recenzije: list):
        super().__init__(korisnicko_ime, lozinka, ime, prezime, pol, blokiran)
        self.zadaci = zadaci
        self.recenzije = recenzije

    def dodaj_izvodjaca(self, izvodjac: Ucesnik):
        pass

    def dodaj_muzicko_delo(self, delo: MuzickoDelo):
        pass

    def dodaj_dogadjaj(self, izvodjenje: Izvodjenje):
        pass

    def dodaj_album(self, album: Album):
        pass

    def dodaj_grupu(self, grupa: Grupa):
        pass

    def dodaj_recenziju(self, recenzija: RecenzijaUrednika):
        pass

    def pregledaj_zadatke(self):
        pass

    def izmena_stranice(self, je_dozvoljena: bool):
        pass