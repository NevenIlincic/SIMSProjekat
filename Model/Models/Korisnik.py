from Model.Models.NeregistrovaniKorisnik import NeregistrovaniKorisnik
from Model.Models.Enumerations import Pol
from Model.Models.Osoba import Osoba
from Model.Models.KorisnickiNalog import KorisnickiNalog

class Korisnik(Osoba):
    def __init__(self, id: int, ime: str, prezime: str, pol: Pol, blokiran: bool, korisnicki_nalog: KorisnickiNalog):
        super().__init__(ime, prezime, pol, korisnicki_nalog)
        self.id = id
        self.blokiran = blokiran

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def blokiran(self) -> bool:
        return self._blokiran

    @blokiran.setter
    def blokiran(self, value: bool) -> None:
        self._blokiran = value
   