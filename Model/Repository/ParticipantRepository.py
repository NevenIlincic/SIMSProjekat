from Model.Models.Ucesnik import Ucesnik
from Model.Models.Enumerations import Pol, Zanr
from Model.Observer.Subject import Subject
from datetime import datetime, date

class ParticipantRepository():
    def __init__(self) -> None:
        self.participants = []
        self.path = "Data/Participants.txt"
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
                participant = self.assign_from_list(parameters)
                if participant == None:
                    return
                self.participants.append(participant)
    
    def assign_from_list(self, parameters):
        if parameters[0] == "":
            return None
        enum_list = [Zanr[string_value] for string_value in parameters[11].split("|")]
        return Ucesnik(
            int(parameters[0]),  # id
            parameters[1],       # naziv
            parameters[2],       # slika
            int(parameters[3]),  # pregledi
            int(parameters[4]),  # broj_ocena
            int(parameters[5]),  # zbir_ocena
            parameters[6],       # ime
            parameters[7],       # prezime
            Pol[parameters[8]],  # pol (assuming Pol is an enum)
            datetime.strptime(parameters[9], '%Y-%m-%d').date(),       # datum_rodjenja
            parameters[10],      # biografija
            enum_list,  # zanrovi (assuming genres are separated by '|')
            parameters[12] == "True"  # reklamira_se
        )
    
    def convert_to_list(self, entity: Ucesnik):
        string_list = [member.value for member in entity.zanrovi]
        return [
            str(entity.id), 
            entity.naziv, 
            entity.slika, 
            str(entity.pregledi), 
            str(entity.broj_ocena), 
            str(entity.zbir_ocena), 
            entity.ime, 
            entity.prezime, 
            entity.pol.name,  # assuming Pol is an enum
            entity.datum_rodjenja.strftime('%Y-%m-%d'), 
            entity.biografija, 
            "|".join(string_list),  # join genres with '|'
            str(entity.reklamira_se)
        ]
    
    def save(self):
        with open(self.path, "w") as f:
            for participant in self.participants:
                parameters = self.convert_to_list(participant)
                row = ",".join(parameters) + "\n"
                f.write(row)

    def generate_id(self):
        if len(self.participants) == 0:
            return 1
        self.participants.sort(key=lambda x: x.id)
        last_participant = self.participants[-1]
        return last_participant.id + 1

    def add_participant(self, participant: Ucesnik):
        self.participants.append(participant)
        self.save()
        self.subject.notify_observers()

    def delete_participant(self, id: int):
        participant_to_remove = None
        for participant in self.participants:
            if participant.id == id:
                participant_to_remove = participant
                break
        if participant_to_remove != None:
            self.participants.remove(participant_to_remove)
            self.save()
            self.subject.notify_observers()

    def get_all_participants(self):
        return self.participants

    def get_by_id(self, id):
        for participant in self.participants:
            if participant.id == id:
                return participant
        return False
