from Controller.MusicalPieceController import MusicalPieceController
from Model.DTO.AlbumFormDTO import AlbumFormDTO
from Model.Repository.AlbumRepository import AlbumRepository
from Model.Models.Album import Album
from Model.DTO.AlbumDTO import AlbumDTO
from Model.Models.MuzickoDelo import MuzickoDelo

class AlbumController():
    def __init__(self) -> None:
        self.album_repository = AlbumRepository()
        self.musical_piece_controller = MusicalPieceController()
    
    def add_album(self, album_dto: AlbumFormDTO):
        id = self.album_repository.generate_id()
        new_album = self.convert_DTO_to_model(album_dto)
        new_album.id = id
        self.album_repository.add_album(new_album)
        return new_album
    
    def load(self):
        return self.album_repository.load()
    
    def delete_album(self, naziv: str):
        return self.album_repository.delete_album(naziv)
    
    def convert_DTO_to_model(self, album_dto):
        if isinstance(album_dto, AlbumFormDTO):
            musical_pieces = [self.musical_piece_controller.get_by_id(md.id) for md in album_dto.musical_pieces]
            return Album(
                0,
                album_dto.album_name,
                album_dto.image,
                0,
                0,
                0,
                musical_pieces
            )
    
    def get_all_albums(self):
        return self.album_repository.get_all_albums()

    def get_by_naziv(self, naziv: str):
        return self.album_repository.get_by_naziv(naziv)
