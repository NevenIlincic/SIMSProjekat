from Model.Models.Korisnik import Korisnik

class RecenzijaKorisnika:
    def __init__(self, id: int, ocena: int, korisnik: Korisnik, muzicki_element: list):
        self.id = id
        self.ocena = ocena
        self.korisnik = korisnik
        muzicki_element = muzicki_element

    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def ocena(self):
        return self._ocena

    @ocena.setter
    def ocena(self, value):
        self._ocena = value

    @property
    def korisnik(self):
        return self._korisnik

    @korisnik.setter
    def korisnik(self, value):
        self._korisnik = value

    @property
    def muzicki_element(self):
        return self._muzicki_element

    @muzicki_element.setter
    def muzicki_element(self, value):
        self._muzicki_element = value