from Controller.RegisteredUserController import RegisteredUserController
from Model.DTO.ListOfFavouritesDTO import ListaOmiljenihDTO
from Model.Repository.ListOfFavouritesRepository import ListOfFavouritesRepository
from Model.Observer.Subject import Subject
from Model.Repository.MusicalElementRepository import MusicalElementRepository
from Model.Models.ListaOmiljenih import ListaOmiljenih


class ListOfFavouritesController(): 
    def __init__(self) -> None:
        self.list_repository = ListOfFavouritesRepository()
        self.musical_piece_controller = MusicalElementRepository()

    def add_list(self, list_dto: ListaOmiljenihDTO):
        muzicka_dela_ids = [md.id for md in list_dto.muzicki_elementi]
        new_list = ListaOmiljenih(
            0,  # ID will be generated by the repository
            list_dto.naziv,
            list_dto.korisnik,
            [self.musical_piece_controller.get_by_id(md_id) for md_id in muzicka_dela_ids]
        )
        added_list = self.list_repository.add_list(new_list)
        return added_list
    
    def update_list(self, list_dto: ListaOmiljenihDTO):
        muzicka_dela_ids = [md.id for md in list_dto.muzicki_elementi]
        new_list = ListaOmiljenih(
            list_dto.id,  
            list_dto.naziv,
            list_dto.korisnik,
            [self.musical_piece_controller.get_by_id(md_id) for md_id in muzicka_dela_ids]
        )
        self.list_repository.update_list(new_list)
    
    def load(self):
        return self.list_repository.load()
    
    def delete_list(self, id: int):
        return self.list_repository.delete_list(id)
    
    def convert_DTO_to_model(self, list_dto : ListaOmiljenihDTO):
        if isinstance(list_dto, ListaOmiljenihDTO):
            muzicka_dela = [self.musical_piece_controller.get_by_id(md.id) for md in list_dto.muzicki_elementi]
            return ListaOmiljenih(
                list_dto.id,
                list_dto.naziv,
                list_dto.korisnik,
                muzicka_dela
            )
    
    def get_all_lists(self):
        return self.list_repository.get_all_lists()

    def get_by_id(self, id: int):
        return self.list_repository.get_by_id(id)
    
