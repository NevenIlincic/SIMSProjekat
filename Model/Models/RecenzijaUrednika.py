from Model.Models.MuzickiElement import MuzickiElement

class RecenzijaUrednika:
    def __init__(self, opis: str, ocena: int, menja_se: bool, muzicki_element: MuzickiElement):
        self.opis = opis
        self.ocena = ocena
        self.menja_se = menja_se
        self.muzicki_element = muzicki_element