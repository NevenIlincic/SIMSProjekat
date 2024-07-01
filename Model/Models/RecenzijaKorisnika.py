from Model.Models.Korisnik import Korisnik

class RecenzijaKorisnika:
    def __init__(self, ocena: int, korisnik: Korisnik, muzicki_element: list):
        self.ocena = ocena
        self.korisnik = korisnik
        muzicki_element = muzicki_element