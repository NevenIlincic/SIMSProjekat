from Model.Models.Korisnik import Korisnik

class ListaOmiljenih:
    def __init__(self, id : int ,naziv: str, korisnik: Korisnik, muzicki_elementi: list):
        self.id = id
        self.naziv = naziv
        self.korisnik = korisnik
        self.muzicki_elementi = muzicki_elementi

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def naziv(self) -> str:
        return self._naziv

    @naziv.setter
    def naziv(self, value: str):
        self._naziv = value

    @property
    def korisnik(self) -> Korisnik:
        return self._korisnik

    @korisnik.setter
    def korisnik(self, value: Korisnik):
        self._korisnik = value

    @property
    def muzicki_elementi(self) -> list:
        return self._muzicki_elementi

    @muzicki_elementi.setter
    def muzicki_elementi(self, value: list):
        self._muzicki_elementi = value