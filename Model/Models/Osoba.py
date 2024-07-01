from Model.Models.Enumerations import Pol
from Model.Models.KorisnickiNalog import KorisnickiNalog
class Osoba:
    def __init__(self, ime: str, prezime: str, pol: Pol, korisnicki_nalog: KorisnickiNalog):
        self.ime = ime
        self.prezime = prezime
        self.pol = pol
        self.korisnicki_nalog = korisnicki_nalog

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
    def korisnicki_nalog(self) -> KorisnickiNalog:
        return self._korisnicki_nalog

    @korisnicki_nalog.setter
    def korisnicki_nalog(self, value: KorisnickiNalog) -> None:
        self._korisnicki_nalog = value