from Model.Models.Korisnik import Korisnik

class ListaOmiljenih:
    def __init__(self, naziv: str, korisnik: Korisnik, muzicki_elementi: list):
        self.naziv = naziv
        self.korisnik = korisnik
        self.muzicki_elementi = muzicki_elementi