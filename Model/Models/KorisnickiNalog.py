from Osoba import Osoba

class KorisnickiNalog:
    def __init__(self, korisnicko_ime: str, lozinka: str, osoba: Osoba):
        self.korisnicko_ime = korisnicko_ime
        self.lozinka = lozinka
        self.osoba = osoba