from Controller.RegisteredUserController import RegisteredUserController
from Model.Models.ListaOmiljenih import ListaOmiljenih
from Model.Observer.Subject import Subject
from Model.Repository.MusicalElementRepository import MusicalElementRepository


class ListOfFavouritesRepository():
    def __init__(self) -> None:
        self.lists = []
        self.path = "Data/Lists.txt"
        self.subject = Subject()
        self.musical_piece_repository = MusicalElementRepository()
        self.user_controller = RegisteredUserController()
        self.load()

    def load(self):
        with open(self.path, "r") as f:
            while True:
                row = f.readline()
                if not row:
                    return
                row = row.strip("\n")
                parameters = row.split(",")
                list = self.assign_from_list(parameters)
                if list:
                    self.lists.append(list)

    def assign_from_list(self, parameters):
        if parameters[0] == "":
            return None
        muzicka_dela = []
        if parameters[3] != "":
            muzicka_dela_ids = parameters[3].split("|")
            muzicka_dela = [self.musical_piece_repository.get_by_id(int(md_id)) for md_id in muzicka_dela_ids]
        
      
        return ListaOmiljenih(
            int(parameters[0]),   
            parameters[1],        
            self.user_controller.get_by_id(int(parameters[2])),       
            muzicka_dela         
        )
    
    def convert_to_list(self, entity: ListaOmiljenih):
        muzicka_dela_ids_str = "|".join([str(md.id) for md in entity.muzicki_elementi])
        return [
            str(entity.id),       
            entity.naziv, 
            str(entity.korisnik.id), 
            muzicka_dela_ids_str
        ]
    

    def save(self):
        with open(self.path, "w") as f:
            for list in self.lists:
                parameters = self.convert_to_list(list)
                row = ",".join(parameters) + "\n"
                f.write(row)

    def generate_id(self):
        if not self.lists:
            return 1
        self.lists.sort(key=lambda x: x.id)
        last_list = self.lists[-1]
        return last_list.id + 1

    def add_list(self, lista : ListaOmiljenih):
        self.lists.append(lista)
        self.save()
        self.subject.notify_observers()
        return lista
    
    def update_list(self, list : ListaOmiljenih):
        self.delete_list(list.id)
        self.add_list(list)
    
    def delete_list(self, id : int):
        list_to_remove = None
        for list in self.lists:
            if list.id == id:
                list_to_remove = list
                break
        if list_to_remove:
            self.lists.remove(list_to_remove)
            self.save()
            self.subject.notify_observers()

    def get_all_lists(self):
        return self.lists

    def get_by_id(self, id):
        for list in self.lists:
            if list.id == id:
                return list
        return None
