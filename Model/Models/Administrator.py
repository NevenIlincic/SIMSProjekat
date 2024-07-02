from Model.Models.Osoba import Osoba
from Model.Models.Enumerations import Pol
from Model.Models.KorisnickiNalog import KorisnickiNalog

class Administrator(Osoba):
    def __init__(self, id:int, ime: str, prezime: str, pol: Pol, zadaci: list, korisnicki_nalog: KorisnickiNalog):
        super().__init__(ime, prezime, pol, korisnicki_nalog)
        self.id = id
        self.zadaci = zadaci
       
    @property
    def id(self) -> bool:
        return self._id

    @id.setter
    def id(self, value: bool) -> None:
        self._id = value

    @property
    def zadaci(self) -> bool:
        return self._zadaci

    @zadaci.setter
    def zadaci(self, value: bool) -> None:
        self._zadaci = value
