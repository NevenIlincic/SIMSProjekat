class KorisnickiNalog:
    def __init__(self, id: int, korisnicko_ime: str, lozinka: str, uloga: str):
        self.id = id
        self.korisnicko_ime = korisnicko_ime
        self.lozinka = lozinka
        self.uloga = uloga
    
    #Geters
    @property
    def id(self):
        return self._id

    @property
    def korisnicko_ime(self):
        return self._korisnicko_ime

    @property
    def lozinka(self):
        return self._lozinka

    @property
    def uloga(self):
        return self._uloga

    # Seteri
    @id.setter
    def id(self, value):
        self._id = value

    @korisnicko_ime.setter
    def korisnicko_ime(self, value):
        self._korisnicko_ime = value

    @lozinka.setter
    def lozinka(self, value):
        self._lozinka = value

    @uloga.setter
    def uloga(self, value):
        self._uloga = value