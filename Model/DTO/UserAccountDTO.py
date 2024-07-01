from Model.Models.Enumerations import VrstaKorisnika
from Model.DTO.DTO_BaseClass import DTO

class UserAccountDTO(DTO):
    def __init__(self, korisnicko_ime: str, lozinka: str, uloga: VrstaKorisnika) -> None:
        self.korisnicko_ime = korisnicko_ime
        self.lozinka = lozinka
        self.uloga = uloga
    
    @property
    def korisnicko_ime(self):
        return self._korisnicko_ime

    @korisnicko_ime.setter
    def korisnicko_ime(self, value):
        self._korisnicko_ime = value

    @property
    def lozinka(self):
        return self._lozinka

    @lozinka.setter
    def lozinka(self, value):
        self._lozinka = value

    @property
    def uloga(self):
        return self._uloga

    @uloga.setter
    def uloga(self, value):
        self._uloga = value