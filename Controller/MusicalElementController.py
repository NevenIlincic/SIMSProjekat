from Model.Repository.MusicalElementRepository import MusicalElementRepository
from Model.Models.MuzickiElement import MuzickiElement
from Model.DTO.MusicalElementDTO import MusicalElementDTO

class MusicalElementController():
    def __init__(self) -> None:
        self.musical_element_repository = MusicalElementRepository()
    
    def add_element(self, element: MusicalElementDTO):
        id = self.musical_element_repository.generate_id()
        new_element = self.convert_DTO_to_model(element)
        new_element.id = id
        self.musical_element_repository.add_element(new_element)
        return new_element
    
    def load(self):
        return self.musical_element_repository.load()
    
    def delete_element(self, id: int):
        return self.musical_element_repository.delete_element(id)
    
    def convert_DTO_to_model(self, musical_element_dto):
        if isinstance(musical_element_dto, MusicalElementDTO):
            return MuzickiElement(
                0,  # ID will be set later
                musical_element_dto.naziv, 
                musical_element_dto.slika, 
                musical_element_dto.pregledi, 
                musical_element_dto.broj_ocena, 
                musical_element_dto.zbir_ocena
            )
    
    def get_all_elements(self):
        return self.musical_element_repository.get_all_elements()

    def get_by_id(self, id: int):
        return self.musical_element_repository.get_by_id(id)
