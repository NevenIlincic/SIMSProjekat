from Model.Models.Enumerations import Pol
class UserInformationsDTO():
    def __init__(self, korisnicko_ime: str, lozinka: str, ime: str, prezime: str, pol: Pol, uloga: str ) -> None:
        self.korisnicko_ime = korisnicko_ime
        self.lozinka = lozinka
        self.ime = ime
        self.prezime = prezime
        self.pol = pol
        self.uloga = uloga
    
    @property
    def korisnicko_ime(self) -> str:
        return self._korisnicko_ime

    @korisnicko_ime.setter
    def korisnicko_ime(self, value: str) -> None:
        self._korisnicko_ime = value

    @property
    def lozinka(self) -> str:
        return self._lozinka

    @lozinka.setter
    def lozinka(self, value: str) -> None:
        self._lozinka = value

    @property
    def ime(self) -> str:
        return self._ime

    @ime.setter
    def ime(self, value: str) -> None:
        self._ime = value

    @property
    def prezime(self) -> str:
        return self._prezime

    @prezime.setter
    def prezime(self, value: str) -> None:
        self._prezime = value

    @property
    def pol(self) -> Pol:
        return self._pol

    @pol.setter
    def pol(self, value: Pol) -> None:
        self._pol = value

    @property
    def uloga(self) -> str:
        return self._uloga

    @uloga.setter
    def uloga(self, value: str) -> None:
        self._uloga = value