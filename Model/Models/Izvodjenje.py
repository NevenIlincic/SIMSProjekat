from Model.Models.MuzickiElement import MuzickiElement, VrstaIzvodjenja

class Izvodjenje(MuzickiElement):
    def __init__(self, id: int, naziv: str, slika: str, pregledi: int, broj_ocena: int, zbir_ocena: int, mesto: str, vreme: str, link: str, vrsta_izvodjenja: VrstaIzvodjenja, muzicka_dela : list):
        super().__init__(id, naziv, slika, pregledi, broj_ocena, zbir_ocena)
        self.mesto = mesto
        self.vreme = vreme
        self.link = link
        self.vrsta_izvodjenja = vrsta_izvodjenja
        self.muzicka_dela = muzicka_dela
