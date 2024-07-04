from Model.Models.Grupa import Grupa
from Model.Models.Ucesnik import Ucesnik
from Model.Observer.Subject import Subject
from Model.Repository.ParticipantRepository import ParticipantRepository
class GroupRepository():
    def __init__(self) -> None:
        self.groups = []
        self.path = "Data/Groups.txt"
        self.subject = Subject()
        self.__participant_repository = ParticipantRepository()
        self.load()

    def load(self):
        with open(self.path, "r") as f:
            while True:
                row = f.readline()
                if not row:
                    return
                row = row.strip("\n")
                parameters = row.split(";")
                group = self.assign_from_list(parameters)
                if group:
                    self.groups.append(group)
    
    def assign_from_list(self, parameters):
        if parameters[0] == "":
            return None
        ucesnici = []
        if parameters[6] != "":
            ucesnici_ids = parameters[6].split("|")
            ucesnici = [self.__participant_repository.get_by_id(int(u_id)) for u_id in ucesnici_ids]
        return Grupa(
            int(parameters[0]),    # id
            parameters[1],         # naziv
            parameters[2],         # slika
            int(parameters[3]),    # pregledi
            int(parameters[4]),    # broj_ocena
            int(parameters[5]),    # zbir_ocena
            ucesnici               # ucesnici
        )
    
    def convert_to_list(self, entity: Grupa):
        ucesnici_ids_str = "|".join([str(u.id) for u in entity.ucesnici])
        return [
            str(entity.id), 
            entity.naziv, 
            entity.slika, 
            str(entity.pregledi), 
            str(entity.broj_ocena), 
            str(entity.zbir_ocena), 
            ucesnici_ids_str
        ]

    def save(self):
        with open(self.path, "w") as f:
            for group in self.groups:
                parameters = self.convert_to_list(group)
                row = ";".join(parameters) + "\n"
                f.write(row)

    def generate_id(self):
        if not self.groups:
            return 1
        self.groups.sort(key=lambda x: x.id)
        last_group = self.groups[-1]
        return last_group.id + 1

    def add_group(self, group: Grupa):
        self.groups.append(group)
        self.save()
        self.subject.notify_observers()

    def delete_group(self, naziv: str):
        group_to_remove = None
        for group in self.groups:
            if group.naziv == naziv:
                group_to_remove = group
                break
        if group_to_remove:
            self.groups.remove(group_to_remove)
            self.save()
            self.subject.notify_observers()

    def get_all_groups(self):
        return self.groups

    def get_by_naziv(self, naziv):
        for group in self.groups:
            if group.naziv == naziv:
                return group
        return None

    #dodato
    def get_by_id(self, id):
        for group in self.groups:
            if group.id == id:
                return group
        return False