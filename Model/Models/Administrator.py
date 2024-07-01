from Osoba import Osoba
from SIMSProjekat.Model.Models.Enumerations import Pol

class Administrator(Osoba):
    def __init__(self, ime: str, prezime: str, pol: Pol, zadaci: list):
        super().__init__(ime, prezime, pol)
        self.zadaci = zadaci

    def dodaj_urednika(self, urednik):
        pass

    def izmeni_urednika(self, urednik):
        pass

    def pregledaj_urednike(self):
        pass

    def obrisi_urednika(self, urednik):
        pass

    def registruj_izvodjaca_za_reklamu(self, izvodjac):
        pass

    def blokiraj_korisnika(self, korisnik):
        pass

    def brisanje_korisnika(self, korisnik):
        pass

    def pregledaj_detalje_o_pregledima_stranica(self):
        pass

    def zadaj_zadatak(self, zadatak):
        pass

    def pregledaj_zadatke_muzickih_urednika(self):
        pass