from Model.Models.Enumerations import Uloga
from Model.Models.Ucesnik import Ucesnik
from Model.Models.MuzickoDelo import MuzickoDelo

class UcesnikIzvodjenje:
    def __init__(self, uloga: Uloga, ucesnik: Ucesnik, muzicko_delo: MuzickoDelo):
        self.uloga = uloga
        self.ucesnik = ucesnik
        self.muzicko_delo = muzicko_delo