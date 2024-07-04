from Controller.GroupController import GroupController
from Model.Repository.MusicalPieceRepository import MusicalPieceRepository
from Model.Models.MuzickoDelo import MuzickoDelo
from Model.DTO.MusicalPieceDTO import MusicalPieceDTO
from Model.Models.Grupa import Grupa

class MusicalPieceController():
    def __init__(self) -> None:
        self.piece_repository = MusicalPieceRepository()
        self.group_controller = GroupController()
    
    def add_piece(self, piece_dto: MusicalPieceDTO):
        id = self.piece_repository.generate_id()
        new_piece = self.convert_DTO_to_model(piece_dto)
        new_piece.id = id
        self.piece_repository.add_piece(new_piece)
        return new_piece
    
    def load(self):
        return self.piece_repository.load()
    
    def delete_piece(self, id: int):
        return self.piece_repository.delete_piece(id)
    
    def convert_DTO_to_model(self, piece_dto):
        if isinstance(piece_dto, MusicalPieceDTO):
            grupa = self.group_controller.get_by_id(piece_dto.grupa.id) if piece_dto.grupa else None
            return MuzickoDelo(
                0,
                piece_dto.naziv,
                piece_dto.slika,
                piece_dto.tekst,
                piece_dto.pregledi,
                piece_dto.broj_ocena,
                piece_dto.zbir_ocena,
                grupa
            )
    
    def get_all_pieces(self):
        return self.piece_repository.get_all_pieces()

    def get_by_id(self, id: int):
        return self.piece_repository.get_by_id(id)
    
    def get_by_name(self, name):
        return self.piece_repository.get_by_name(name)
