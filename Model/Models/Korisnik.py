from Model.Models.NeregistrovaniKorisnik import NeregistrovaniKorisnik
from Model.Models.Enumerations import Pol
from Model.Models.Osoba import Osoba

class Korisnik(Osoba):
    def __init__(self, ime: str, prezime: str, pol: Pol, blokiran: bool):
        super().__init__(ime, prezime, pol)
        self.blokiran = blokiran

    def prijavi_se(self, korisnicko_ime: str, lozinka: str):
        pass

    def dodaj_recenziju(self, recenzija ):
        pass

    def dodaj_ucesnik_delo(self, delo ):
        pass

    def dodaj_grupu(self, grupa):
        pass