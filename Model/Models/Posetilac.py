from Model.Models.Enumerations import Pol, Jezik
from Model.Models.NeregistrovaniKorisnik import NeregistrovaniKorisnik

class Posetilac(NeregistrovaniKorisnik):
    def registruj_se(self, ime: str, prezime: str, pol: Pol, lozinka: str, korisnicko_ime: str):
        pass

    def promeni_jezik(self, jezik: Jezik):
        pass

    def pregledaj_pocetnu_stranicu(self):
        pass

    def pregledaj_detalje_o_izvodjacima(self):
        pass

    def pregledaj_detalje_o_delima(self):
        pass

    def pretraga(self, upit: str):
        pass