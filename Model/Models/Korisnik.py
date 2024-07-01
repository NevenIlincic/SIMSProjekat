from NeregistrovaniKorisnik import NeregistrovaniKorisnik
from Enumerations import Pol
from Osoba import Osoba

class Korisnik(NeregistrovaniKorisnik, Osoba):
    def __init__(self, ime: str, prezime: str, pol: Pol, blokiran: bool):
        super().__init__(ime, prezime, pol)
        self.blokiran = blokiran

    def prijavi_se(self, korisnicko_ime: str, lozinka: str):
        pass

    def dodaj_recenziju(self, recenzija: RecenzijaKorisnika):
        pass

    def dodaj_ucesnik_delo(self, delo: MuzickoDelo):
        pass

    def dodaj_grupu(self, grupa: Grupa):
        pass