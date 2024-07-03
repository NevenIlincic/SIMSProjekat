class MusicalElementDTO:
    def __init__(self, id: int, naziv: str, slika: str, pregledi: int, broj_ocena: int, zbir_ocena: int):
        self._id = id
        self._naziv = naziv
        self._slika = slika
        self._pregledi = pregledi
        self._broj_ocena = broj_ocena
        self._zbir_ocena = zbir_ocena
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def naziv(self):
        return self._naziv

    @naziv.setter
    def naziv(self, value):
        self._naziv = value

    @property
    def slika(self):
        return self._slika

    @slika.setter
    def slika(self, value):
        self._slika = value

    @property
    def pregledi(self):
        return self._pregledi

    @pregledi.setter
    def pregledi(self, value):
        self._pregledi = value

    @property
    def broj_ocena(self):
        return self._broj_ocena

    @broj_ocena.setter
    def broj_ocena(self, value):
        self._broj_ocena = value

    @property
    def zbir_ocena(self):
        return self._zbir_ocena

    @zbir_ocena.setter
    def zbir_ocena(self, value):
        self._zbir_ocena = value
