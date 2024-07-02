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
                    return 
                row = row.strip("\n")
                parameters = row.split(",")
                supervisor = self.assign_from_list(parameters)
                if supervisor == None:
                    return
                self.supervisors.append(supervisor)


    def assign_from_list(self, parameters):
        if parameters[0] == "":
            return None
        user_account = self.__user_account_repository.get_by_id(int(parameters[7]))
        blocked = False
        if parameters[4] == "True":
            blocked = True

        tasks = [] #Dodati ovo kao parametar
        #for id_str in parameters[5].split("-"):
            #task = self.__task_repository.get_by_id(int(id_str))
            #tasks.append(task)
        reviews = []
        #for id_str in parameters[6].split("-"):
            #review = self.__review_repository.get_by_id(int(id_str))
            #reviews.append(review)
        
        return MuzickiUrednik(int(parameters[0]), parameters[1], parameters[2], Pol(parameters[3]), 
                              blocked, [parameters[5]], [parameters[6]], user_account)

    def convert_to_list(self, entity: MuzickiUrednik):
        tasks = []
        for task in entity.zadaci:
            if task == "null":
                tasks = "null"
                break
            tasks.append(str(task.id))
        #tasks_str = "-".join(tasks)

        reviews = []
        for review in entity.recenzije:
            if review == "null":
                reviews = "null"
                break
            reviews.append(str(review.id))

        #reviews_str = "-".join(reviews)

        return [str(entity.id), entity.ime, entity.prezime, entity.pol.value, str(entity.blokiran), tasks, reviews, str(entity.korisnicki_nalog.id)]
    

    def save(self):
        with open(self.path, "w") as f:
            for supervisor in self.supervisors:
                parameters = self.convert_to_list(supervisor)
                row = ",".join(parameters) + "\n"
                f.write(row)

    def generate_id(self):
        if len(self.supervisors) == 0:
            return 1
        self.supervisors.sort(key=lambda x: x.id)
        last_supervisor = self.supervisors[-1]
        return last_supervisor.id + 1
    
    def add_supervisor(self, supervisor: MuzickiUrednik):
        self.supervisors.append(supervisor)
        self.save()
        self.subject.notify_observers()

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
