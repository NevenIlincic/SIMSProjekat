from Model.Models.Izvodjenje import Izvodjenje
from Model.Models.MuzickoDelo import MuzickoDelo
from Model.Models.Enumerations import VrstaIzvodjenja
from Model.Observer.Subject import Subject

class ConcertRepository():
    def __init__(self, musical_piece_repository) -> None:
        self.concerts = []
        self.path = "Data/Concerts.txt"
        self.subject = Subject()
        self.musical_piece_repository = musical_piece_repository
        self.load()

    def load(self):
        with open(self.path, "r") as f:
            while True:
                row = f.readline()
                if not row:
                    return
                row = row.strip("\n")
                parameters = row.split(";")
                concert = self.assign_from_list(parameters)
                if concert:
                    self.concerts.append(concert)
    
    def assign_from_list(self, parameters):
        if parameters[0] == "":
            return None
        muzicka_dela_ids = parameters[9].split("|")
        muzicka_dela = [self.musical_piece_repository.get_by_id(int(md_id)) for md_id in muzicka_dela_ids]
        return Izvodjenje(
            int(parameters[0]),    # id
            parameters[1],         # naziv
            parameters[2],         # slika
            int(parameters[3]),    # pregledi
            int(parameters[4]),    # broj_ocena
            int(parameters[5]),    # zbir_ocena
            parameters[6],         # mesto
            parameters[7],         # vreme
            parameters[8],         # link
            VrstaIzvodjenja[parameters[9]],  # vrsta_izvodjenja (assuming Enum)
            muzicka_dela          # muzicka_dela
        )
    
    def convert_to_list(self, entity: Izvodjenje):
        muzicka_dela_ids_str = "|".join([str(md.id) for md in entity.muzicka_dela])
        return [
            str(entity.id),                # id
            entity.naziv, 
            entity.slika, 
            str(entity.pregledi), 
            str(entity.broj_ocena), 
            str(entity.zbir_ocena), 
            entity.mesto, 
            entity.vreme, 
            entity.link, 
            entity.vrsta_izvodjenja.name,  # assuming Enum
            muzicka_dela_ids_str
        ]

    def save(self):
        with open(self.path, "w") as f:
            for concert in self.concerts:
                parameters = self.convert_to_list(concert)
                row = ";".join(parameters) + "\n"
                f.write(row)

    def generate_id(self):
        if not self.concerts:
            return 1
        self.concerts.sort(key=lambda x: x.id)
        last_concert = self.concerts[-1]
        return last_concert.id + 1

    def add_concert(self, concert: Izvodjenje):
        self.concerts.append(concert)
        self.save()
        self.subject.notify_observers()

    def delete_concert(self, naziv: str):
        concert_to_remove = None
        for concert in self.concerts:
            if concert.naziv == naziv:
                concert_to_remove = concert
                break
        if concert_to_remove:
            self.concerts.remove(concert_to_remove)
            self.save()
            self.subject.notify_observers()

    def get_all_concerts(self):
        return self.concerts

    def get_by_naziv(self, naziv):
        for concert in self.concerts:
            if concert.naziv == naziv:
                return concert
        return None
