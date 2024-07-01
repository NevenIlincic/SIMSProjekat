from Model.Observer.Subject import Subject
from Model.Models.MuzickiUrednik import MuzickiUrednik
from Model.Models.NeregistrovaniKorisnik import NeregistrovaniKorisnik
from Model.Models.Enumerations import Pol

class MusicSupervisorRepository(NeregistrovaniKorisnik):
    def __init__(self) -> None:
        self.subject = Subject()
        self.supervisors = []
        self.path = "Data/MusicSupervisors.txt"
        self.load()

    def load(self):
        with open(self.path, "r") as f:
            while True:
                row = f.readline()
                if row == None or row == "":
                    return self.supervisors
                row = row.strip("\n")
                parameters = row.split(",")
                supervisor = self.assign_from_list(parameters)
                self.supervisors.append(supervisor)


    def assign_from_list(self, parameters):
        supervisor = MuzickiUrednik(int(parameters[0]), parameters[1], parameters[2], Pol(parameters[3]), 
                              bool(parameters[4]), [parameters[5]], [parameters[6]])
        return supervisor


    def get_all_supervisors(self):
        return self.supervisors

    def promeni_jezik(self, jezik):
        pass

    def pregledaj_pocetnu_stranicu(self):
        pass

    def pregledaj_detalje_o_izvodjacima(self):
        pass

    
    def pregledaj_detalje_o_delima(self):
        pass

    def pretraga(self, upit: str):
        pass
