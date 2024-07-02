from Model.Models.Korisnik import Korisnik
from Model.Models.NeregistrovaniKorisnik import NeregistrovaniKorisnik
from Model.Models.Enumerations import Pol
from Model.Repository.UserAccountRepository import UserAccountRepository
from Model.Observer.Subject import Subject

class RegisteredUsersRepository(NeregistrovaniKorisnik):
    def __init__(self) -> None:
        self.users = []
        self.path = "Data/RegisteredUsers.txt"
        self.__user_account_repository = UserAccountRepository()
        self.subject = Subject()
        self.load()

    def save(self):
        with open(self.path, "w") as f:
            for user in self.users:
                parameters = self.convert_to_list(user)
                row = ",".join(parameters) + "\n"
                f.write(row)

    def load(self):
        with open(self.path, "r") as f:
            while True:
                row = f.readline()
                if row == None or row == "":
                    return
                row = row.strip("\n")
                parameters = row.split(",")
                user = self.assign_from_list(parameters)
                if user == None:
                    return
                self.users.append(user)

    def generate_id(self):
        if len(self.users) == 0:
            return 1
        self.users.sort(key=lambda x: x.id)
        last_user = self.users[-1]
        return last_user.id + 1

    def add_user(self, user: Korisnik):
        self.users.append(user)
        self.save()
        self.subject.notify_observers()

    def assign_from_list(self, parameters):
        if parameters[0] == "":
            return None
        user_account = self.__user_account_repository.get_by_id(int(parameters[5]))
        blocked = False
        if parameters[4] == "True":
            blocked = True
        return Korisnik(int(parameters[0]), parameters[1], parameters[2], Pol(parameters[3]), blocked, user_account)
    
    def convert_to_list(self, entity: Korisnik):
        return [str(entity.id), entity.ime, entity.prezime, entity.pol.value, str(entity.blokiran), str(entity.korisnicki_nalog.id)]
    
    def delete_user(self, id: int):
        user_to_remove = None
        for user in self.users:
            if user.id == id:
                user_to_remove = user
                break
        if user_to_remove != None:
            self.users.remove(user_to_remove)
            self.save()
            self.subject.notify_observers()
        return user_to_remove

    def get_all_users(self):
        return self.users

    def dodaj_recenziju(self, recenzija ):
        pass

    def dodaj_ucesnik_delo(self, delo ):
        pass

    def dodaj_grupu(self, grupa):
        pass

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
    