from Model.Observer.Subject import Subject
from Model.Models.Zadatak import Zadatak
from Model.Repository.MusicalElementRepository import MusicalElementRepository


class TaskRepository():
    def __init__(self) -> None:
        self.tasks = []
        self.path = "Data/Tasks.txt"
        self.subject = Subject()
        self.musical_piece_repository = MusicalElementRepository()
        self.load()

    def load(self):
        with open(self.path, "r") as f:
            while True:
                row = f.readline()
                if not row:
                    return
                row = row.strip("\n")
                parameters = row.split(";")
                task = self.assign_from_list(parameters)
                if task:
                    self.tasks.append(task)

    def assign_from_list(self, parameters):
        if parameters[0] == "":
            return None
        muzicka_dela_ids = parameters[5].split("|")
        muzicka_dela = [self.musical_piece_repository.get_by_id(int(md_id)) for md_id in muzicka_dela_ids]
        
        b = False
        if parameters[2] == "False":
            b = False
        else:
            b = bool(parameters[2])

        return Zadatak(
            int(parameters[0]),   
            parameters[1],        
            b,       
            muzicka_dela          
        )
    
    def convert_to_list(self, entity: Zadatak):
        muzicka_dela_ids_str = "|".join([str(md.id) for md in entity.muzicka_dela])
        return [
            str(entity.id),       
            entity.tekst, 
            str(entity.uradjen), 
            muzicka_dela_ids_str
        ]
    

    def save(self):
        with open(self.path, "w") as f:
            for task in self.tasks:
                parameters = self.convert_to_list(task)
                row = ";".join(parameters) + "\n"
                f.write(row)

    def generate_id(self):
        if not self.tasks:
            return 1
        self.tasks.sort(key=lambda x: x.id)
        last_zadataka = self.tasks[-1]
        return last_zadataka.id + 1

    def add_task(self, zadatak : Zadatak):
        self.tasks.append(zadatak)
        self.save()
        self.subject.notify_observers()

    def delete_task(self, id : int):
        task_to_remove = None
        for task in self.tasks:
            if task.id == id:
                task_to_remove = task
                break
        if task_to_remove:
            self.tasks.remove(task_to_remove)
            self.save()
            self.subject.notify_observers()

    def get_all_tasks(self):
        return self.tasks

    def get_by_id(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
        return None
