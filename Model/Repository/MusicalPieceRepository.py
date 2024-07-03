from Model.Models.MuzickoDelo import MuzickoDelo
from Model.Models.Grupa import Grupa
from Model.Observer.Subject import Subject
from Model.Repository.GroupRepository import GroupRepository
class MusicalPieceRepository():
    def __init__(self) -> None:
        self.pieces = []
        self.path = "Data/MusicalPieces.txt"
        self.subject = Subject()
        self.__group_repository = GroupRepository()
        self.load()

    def load(self):
        with open(self.path, "r") as f:
            while True:
                row = f.readline()
                if row == None or row == "":
                    return
                row = row.strip("\n")
                parameters = row.split(";")
                piece = self.assign_from_list(parameters)
                if piece == None:
                    return
                self.pieces.append(piece)
    
    def assign_from_list(self, parameters):
        if parameters[0] == "":
            return None
        grupa = self.__group_repository.get_by_id(int(parameters[7]))
        return MuzickoDelo(
            int(parameters[0]),  # id
            parameters[1],       # naziv
            parameters[2],       # slika
            parameters[3],       # tekst
            int(parameters[4]),  # pregledi
            int(parameters[5]),  # broj_ocena
            int(parameters[6]),  # zbir_ocena
            grupa                # grupa
        )
    
    def convert_to_list(self, entity: MuzickoDelo):
        return [
            str(entity.id), 
            entity.naziv, 
            entity.slika, 
            entity.tekst, 
            str(entity.pregledi), 
            str(entity.broj_ocena), 
            str(entity.zbir_ocena), 
            str(entity.grupa.id)  # Save the group's ID
        ]

    def save(self):
        with open(self.path, "w") as f:
            for piece in self.pieces:
                parameters = self.convert_to_list(piece)
                row = ";".join(parameters) + "\n"
                f.write(row)

    def generate_id(self):
        if len(self.pieces) == 0:
            return 1
        self.pieces.sort(key=lambda x: x.id)
        last_piece = self.pieces[-1]
        return last_piece.id + 1

    def add_piece(self, piece: MuzickoDelo):
        self.pieces.append(piece)
        self.save()
        self.subject.notify_observers()

    def delete_piece(self, id: int):
        piece_to_remove = None
        for piece in self.pieces:
            if piece.id == id:
                piece_to_remove = piece
                break
        if piece_to_remove != None:
            self.pieces.remove(piece_to_remove)
            self.save()
            self.subject.notify_observers()

    def get_all_pieces(self):
        return self.pieces

    def get_by_id(self, id):
        for piece in self.pieces:
            if piece.id == id:
                return piece
        return False
