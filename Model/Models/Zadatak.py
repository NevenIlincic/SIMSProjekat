class Zadatak:
    def __init__(self, id : int ,tekst: str, uradjen: bool, muzicki_elementi: list):
        self.id = id
        self.tekst = tekst
        self.uradjen = uradjen
        self.muzicki_elementi = muzicki_elementi

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def tekst(self):
        return self.tekst

    @tekst.setter
    def tekst(self, value):
        self.tekst = value

    @property
    def uradjen(self):
        return self.uradjen

    @uradjen.setter
    def uradjen(self, value):
        self.uradjen = value

    @property
    def muzicki_elementi(self):
        return self.muzicki_elementi

    @muzicki_elementi.setter
    def muzicki_elementi(self, value):
        self.muzicki_elementi = value