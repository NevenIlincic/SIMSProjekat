from Model.Models.Enumerations import Uloga
from Model.Models.Ucesnik import Ucesnik
from Model.Models.Izvodjenje import Izvodjenje

class UcesnikIzvodjenje:
    def __init__(self, uloga: Uloga, ucesnik: Ucesnik, izvodjenje: Izvodjenje):
        self.uloga = uloga
        self.ucesnik = ucesnik
        self.izvodjenje = izvodjenje