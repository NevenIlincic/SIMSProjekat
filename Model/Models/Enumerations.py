from enum import Enum

# Enums
class VrstaKorisnika(Enum):
    Urednik = "Muzicki urednik"
    Administrator = "Adminitrator"
    Registrovani_korisnik = "Registrovani korisnik"
    
class Zanr(Enum):
    Pop = "Pop"
    Narodna = "Narodna"
    Klasika = "Klasika"
    Dzez = "Dzez"

class Uloga(Enum):
    Kompozitor = "Kompozitor"
    Dirigent = "Dirigent"
    Izvodjac = "Izvodjac"
    Producer = "Producer"
    Menadzer = "Menadzer"

class Pol(Enum):
    Muski = "muski"
    Zenski = "zenski"

class VrstaIzvodjenja(Enum):
    CD = "CD"
    Ploca = "Ploca"
    Kaseta = "Kaseta"
    Video = "Video"

class Jezik(Enum):
    Srpski = "Srpski"
    Engleski = "Engleski"
    Nemacki = "Nemacki"