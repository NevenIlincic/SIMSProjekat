from Model.Models.Enumerations import VrstaIzvodjenja
from Model.DTO.MusicalElementDTO import MusicalElementDTO

class ConcertDTO(MusicalElementDTO):
    def __init__(self, id: int, naziv: str, slika: str, pregledi: int, broj_ocena: int, zbir_ocena: int, mesto: str, vreme: str, link: str, vrsta_izvodjenja: VrstaIzvodjenja, muzicka_dela: list):
        super().__init__(id, naziv, slika, pregledi, broj_ocena, zbir_ocena)
        self._mesto = mesto
        self._vreme = vreme
        self._link = link
        self._vrsta_izvodjenja = vrsta_izvodjenja
        self._muzicka_dela = muzicka_dela
    
    @property
    def mesto(self):
        return self._mesto

    @mesto.setter
    def mesto(self, value):
        self._mesto = value

    @property
    def vreme(self):
        return self._vreme

    @vreme.setter
    def vreme(self, value):
        self._vreme = value

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value

    @property
    def vrsta_izvodjenja(self):
        return self._vrsta_izvodjenja

    @vrsta_izvodjenja.setter
    def vrsta_izvodjenja(self, value):
        self._vrsta_izvodjenja = value

    @property
    def muzicka_dela(self):
        return self._muzicka_dela

    @muzicka_dela.setter
    def muzicka_dela(self, value):
        self._muzicka_dela = value
