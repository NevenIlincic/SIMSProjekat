from Model.Observer.Subject import Subject
from Model.Models.MuzickiUrednik import MuzickiUrednik
from Model.Models.NeregistrovaniKorisnik import NeregistrovaniKorisnik
from Model.Models.Enumerations import Pol
from Model.Repository.UserAccountRepository import UserAccountRepository
from Model.Repository.EditorsReviewRepository import EditorsReviewRepository
from Model.Repository.TaskRepository import TaskRepository

class MusicSupervisorRepository(NeregistrovaniKorisnik):
    def __init__(self) -> None:
        self.subject = Subject()
        self.supervisors = []
        self.__user_account_repository = UserAccountRepository()
        self.__editors_review_repository = EditorsReviewRepository()
        self.__task_repository = TaskRepository()
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
        if parameters[5] != "":
            for id_str in parameters[5].split("-"):
                task = self.__task_repository.get_by_id(int(id_str))
                tasks.append(task)

        reviews = []
        if parameters[6] != "":
            for id_str in parameters[6].split("-"):
                review = self.__editors_review_repository.get_by_id(int(id_str))
                reviews.append(review)
        
        return MuzickiUrednik(int(parameters[0]), parameters[1], parameters[2], Pol(parameters[3]), 
                              blocked, tasks, reviews, user_account)

    def convert_to_list(self, entity: MuzickiUrednik):
        reviews_id = []
        tasks_id = []
        for review in entity.recenzije:
            reviews_id.append(str(review.id))
        for task in entity.zadaci:
            tasks_id.append(str(task.id))

        tasks = "-".join(tasks_id)
        reviews = "-".join(reviews_id)
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

    def get_supervisor_by_id(self, id):
        for supervisor in self.supervisors:
            if supervisor.id == id:
                return supervisor
        return None
    
    def update_supervisor(self, supervisor: MuzickiUrednik):
        supervisor_to_update = self.get_supervisor_by_id(supervisor.id)
        index = self.supervisors.index(supervisor_to_update)
        supervisor_to_update.recenzije = supervisor.recenzije
        self.supervisors[index] = supervisor_to_update
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
