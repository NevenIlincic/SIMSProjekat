from Model.Models.Enumerations import Pol
from Model.Models.KorisnickiNalog import KorisnickiNalog
class Osoba:
    def __init__(self, ime: str, prezime: str, pol: Pol, korisnicki_nalog: KorisnickiNalog):
        self.ime = ime
        self.prezime = prezime
        self.pol = pol
        self.korisnicki_nalog = korisnicki_nalog