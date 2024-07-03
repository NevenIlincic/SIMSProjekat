from Model.Observer.Subject import Subject
from Model.Models.Administrator import Administrator
from Model.Models.Enumerations import Pol
from Model.Repository.UserAccountRepository import UserAccountRepository

class AdministratorRepository():
    def __init__(self) -> None:
        self.administrators = []
        self.path = "Data/Administrators.txt"
        self.__user_account_repository = UserAccountRepository()
        self.subject = Subject()
        self.load()

    def load(self):
        with open(self.path, "r") as f:
            while True:
                row = f.readline()
                if row == None or row == "":
                    return
                row = row.strip("\n")
                parameters = row.split(",")
                administrator = self.assign_from_list(parameters)
                if administrator == None:
                    return
                self.administrators.append(administrator)
    
    def assign_from_list(self, parameters):
        if parameters[0] == "":
            return None
        user_account = self.__user_account_repository.get_by_id(int(parameters[5]))
        return Administrator(int(parameters[0]), parameters[1], parameters[2], Pol(parameters[3]),[parameters[4]], user_account)
    
    def get_administrator_by_id(self, id):
        for administrator in self.administrators:
            if administrator.id == id:
                return administrator
        return None
    
    def get_all_administrators(self):
        return self.administrators
    
    def dodaj_urednika(self, urednik):
        pass

    def izmeni_urednika(self, urednik):
        pass

    def pregledaj_urednike(self):
        pass

    def obrisi_urednika(self, urednik):
        pass

    def registruj_izvodjaca_za_reklamu(self, izvodjac):
        pass

    def blokiraj_korisnika(self, korisnik):
        pass

    def brisanje_korisnika(self, korisnik):
        pass

    def pregledaj_detalje_o_pregledima_stranica(self):
        pass

    def zadaj_zadatak(self, zadatak):
        pass

    def pregledaj_zadatke_muzickih_urednika(self):
        pass