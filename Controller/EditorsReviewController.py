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
        new_review = RecenzijaUrednika(
            review_dto.opis, 
            review_dto.ocena, 
            review_dto.menja_se,
            review_dto.muzicki_element
            )
        added_review = self.editors_review_repository.add_review(new_review)
        return added_review
    
    def load(self):
        return self.editors_review_repository.load()
    
    def delete_review(self, id: int):
        return self.editors_review_repository.delete_review(id)
       
    def convert_DTO_to_model(self, editors_review_dto):
        if isinstance(editors_review_dto, EditorsReviewDTO):
            return RecenzijaUrednika(
                editors_review_dto.opis, 
                editors_review_dto.ocena, 
                editors_review_dto.menja_se, 
                editors_review_dto.muzicki_element      
            )
    
    def get_all_reviews(self):
        return self.editors_review_repository.get_all_reviews()
    
    def get_by_id(self, id: int):
        return self.editors_review_repository.get_by_id(id)