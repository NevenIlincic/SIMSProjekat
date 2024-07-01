from Model.Models.Enumerations import Pol
from Model.Models.KorisnickiNalog import KorisnickiNalog
class UserDTO():
    def __init__(self, ime: str, prezime: str, pol: Pol, korisnicki_nalog: KorisnickiNalog ) -> None:
        self.ime = ime
        self.prezime = prezime
        self.pol = pol
        self.korisnicki_nalog = korisnicki_nalog
    
    @property
    def ime(self) -> str:
        return self._ime

    @ime.setter
    def ime(self, novo_ime: str) -> None:
        self._ime = novo_ime

    @property
    def prezime(self) -> str:
        return self._prezime

    @prezime.setter
    def prezime(self, novo_prezime: str) -> None:
        self._prezime = novo_prezime

    @property
    def pol(self) -> str:
        return self._pol

    @pol.setter
    def pol(self, novi_pol: str) -> None:
        self._pol = novi_pol

    @property
    def korisnicki_nalog(self) -> KorisnickiNalog:
        return self._korisnicki_nalog

    @korisnicki_nalog.setter
    def korisnicki_nalog(self, novi_korisnicki_nalog: KorisnickiNalog) -> None:
        self._korisnicki_nalog = novi_korisnicki_nalog