from Model.Models.Grupa import Grupa
from Model.Models.Izvodjenje import Izvodjenje
from Model.Models.MuzickoDelo import MuzickoDelo
from Model.Models.Ucesnik import Ucesnik
from Model.Repository.EditorsReviewRepository import EditorsReviewRepository
from Model.Models.MuzickiElement import MuzickiElement
from Model.DTO.MusicalElementDTO import MusicalElementDTO
from Model.Models.RecenzijaUrednika import RecenzijaUrednika
from Model.DTO.EditorsReviewDTO import EditorsReviewDTO

class EditorsReviewController():
    def __init__(self, musical_element_repository) -> None:
        self.editors_review_repository = EditorsReviewRepository(musical_element_repository)
        self.musical_element_repository = musical_element_repository

    def add_review(self, review_dto: EditorsReviewDTO):
        id = self.editors_review_repository.generate_id()
        new_review = self.convert_DTO_to_model(review_dto)
        new_review.id = id
        self.editors_review_repository.add_review(new_review)
        return new_review
    
    def load(self):
        return self.editors_review_repository.load()
    
    def delete_review(self, id: int):
        return self.editors_review_repository.delete_review(id)
       
    def convert_DTO_to_model(self, editors_review_dto):
        if isinstance(editors_review_dto, EditorsReviewDTO):
            musical_element_type = None
            if isinstance(editors_review_dto.muzicki_element, MuzickoDelo):
                musical_element_type = "Muzicko delo"
            elif isinstance(editors_review_dto.muzicki_element, Ucesnik):
                musical_element_type = "Izvodjac"
            elif isinstance(editors_review_dto.muzicki_element, Grupa):
                musical_element_type = "Grupa"
            elif isinstance(editors_review_dto.muzicki_element, Izvodjenje):
                musical_element_type = "Izvodjenje"
            else:
                musical_element_type = "Album"
            return RecenzijaUrednika(
                0, #generise se
                editors_review_dto.opis, 
                editors_review_dto.ocena, 
                False, 
                editors_review_dto.muzicki_element,
                musical_element_type   
            )

    def get_all_reviews(self):
        return self.editors_review_repository.get_all_reviews()
    
    def get_by_id(self, id: int):
        return self.editors_review_repository.get_by_id(id)