from Enumerations import Jezik
from abc import ABC, abstractmethod

class NeregistrovaniKorisnik(ABC):
    @abstractmethod
    def promeni_jezik(self, jezik: Jezik):
        pass

    @abstractmethod
    def pregledaj_pocetnu_stranicu(self):
        pass

    @abstractmethod
    def pregledaj_detalje_o_izvodjacima(self):
        pass

    @abstractmethod
    def pregledaj_detalje_o_delima(self):
        pass

    @abstractmethod    
    def pretraga(self, upit: str):
        pass
