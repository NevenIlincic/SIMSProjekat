from Model.Models.Album import Album
from Model.Models.MuzickoDelo import MuzickoDelo
from Model.Observer.Subject import Subject

class AlbumRepository():
    def __init__(self, musical_piece_repository) -> None:
        self.albums = []
        self.path = "Data/Albums.txt"
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
                album = self.assign_from_list(parameters)
                if album:
                    self.albums.append(album)
    
    def assign_from_list(self, parameters):
        if parameters[0] == "":
            return None
        muzicka_dela_ids = parameters[5].split("|")
        muzicka_dela = [self.musical_piece_repository.get_by_id(int(md_id)) for md_id in muzicka_dela_ids]
        return Album(
            int(parameters[0]),   # id
            parameters[1],        # naziv
            parameters[2],        # slika
            int(parameters[3]),   # pregledi
            int(parameters[4]),   # broj_ocena
            int(parameters[5]),   # zbir_ocena
            muzicka_dela          # muzicka_dela
        )
    
    def convert_to_list(self, entity: Album):
        muzicka_dela_ids_str = "|".join([str(md.id) for md in entity.muzicka_dela])
        return [
            str(entity.id),       # id
            entity.naziv, 
            entity.slika, 
            str(entity.pregledi), 
            str(entity.broj_ocena), 
            str(entity.zbir_ocena), 
            muzicka_dela_ids_str
        ]

    def save(self):
        with open(self.path, "w") as f:
            for album in self.albums:
                parameters = self.convert_to_list(album)
                row = ";".join(parameters) + "\n"
                f.write(row)

    def generate_id(self):
        if not self.albums:
            return 1
        self.albums.sort(key=lambda x: x.id)
        last_album = self.albums[-1]
        return last_album.id + 1

    def add_album(self, album: Album):
        self.albums.append(album)
        self.save()
        self.subject.notify_observers()

    def delete_album(self, naziv: str):
        album_to_remove = None
        for album in self.albums:
            if album.naziv == naziv:
                album_to_remove = album
                break
        if album_to_remove:
            self.albums.remove(album_to_remove)
            self.save()
            self.subject.notify_observers()

    def get_all_albums(self):
        return self.albums

    def get_by_naziv(self, naziv):
        for album in self.albums:
            if album.naziv == naziv:
                return album
        return None
