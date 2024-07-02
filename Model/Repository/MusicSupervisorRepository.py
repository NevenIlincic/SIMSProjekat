from Model.Observer.Subject import Subject
from Model.Models.MuzickiUrednik import MuzickiUrednik
from Model.Models.NeregistrovaniKorisnik import NeregistrovaniKorisnik
from Model.Models.Enumerations import Pol
from Model.Repository.UserAccountRepository import UserAccountRepository

class MusicSupervisorRepository(NeregistrovaniKorisnik):
    def __init__(self) -> None:
        self.subject = Subject()
        self.supervisors = []
        self.__user_account_repository = UserAccountRepository()
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
        user_account = self.__user_account_repository.get_by_id(int(parameters[7]))
        blocked = False
        if parameters[4] == "True":
            blocked = True
        return MuzickiUrednik(int(parameters[0]), parameters[1], parameters[2], Pol(parameters[3]), 
                              blocked, [parameters[5]], [parameters[6]], user_account)

    def convert_to_list(self, entity: MuzickiUrednik):
        return [str(entity.id), entity.ime, entity.prezime, entity.pol.value. str(entity.blokiran), str(entity.korisnicki_nalog.id)]
    
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
