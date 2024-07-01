from Enumerations import Pol

class Osoba:
    def __init__(self, ime: str, prezime: str, pol: Pol):
        self.ime = ime
        self.prezime = prezime
        self.pol = pol