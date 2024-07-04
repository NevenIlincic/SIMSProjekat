from Model.Models.Album import Album
from Model.Models.Grupa import Grupa
from Model.Models.MuzickiElement import MuzickiElement
from Model.Models.MuzickoDelo import MuzickoDelo
from Model.Models.Ucesnik import Ucesnik
from Model.Observer.Subject import Subject
from Model.Models.RecenzijaUrednika import RecenzijaUrednika
from Model.Repository.AlbumRepository import AlbumRepository
from Model.Repository.GroupRepository import GroupRepository
from Model.Repository.MusicalPieceRepository import MusicalPieceRepository
from Model.Repository.ParticipantRepository import ParticipantRepository

class EditorsReviewRepository():
    def __init__(self) -> None:
        self.elements = []
        self.path = "Data/EditorsReview.txt"
        self.__music_piece_repository = MusicalPieceRepository()
        self.__participant_repository = ParticipantRepository()
        self.__group_repository = GroupRepository()
        self.__album_repository = AlbumRepository()
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
                element = self.assign_from_list(parameters)
                if element == None:
                    return
                self.elements.append(element)
    

    def assign_from_list(self, parameters):
        if parameters[0] == "":
            return None
       
        b = False
        if parameters[3] == "False":
            b = False
        else:
            b = bool(parameters[3])
        muzicki_element = None
        if parameters[5] == "Muzicko delo":
            muzicki_element = self.__music_piece_repository.get_by_id(int(parameters[4]))
        elif parameters[5] == "Izvodjac":
            muzicki_element = self.__participant_repository.get_by_id(int(parameters[4]))
        elif parameters[5] == "Grupa":
            muzicki_element = self.__group_repository.get_by_id(int(parameters[4]))
        else:
            muzicki_element = self.__album_repository.get_by_id(int(parameters[4]))

        return RecenzijaUrednika(int(parameters[0]), parameters[1] ,int(parameters[2]), b, muzicki_element, parameters[5])
    

    def convert_to_list(self, entity: RecenzijaUrednika):
        return [str(entity.id),entity.opis,str(entity.ocena), str(entity.menja_se), str(entity.muzicki_element.id), entity.vrsta_elementa]
     

    def save(self):
        with open(self.path, "w") as f:
            for element in self.elements:
                parameters = self.convert_to_list(element)
                row = ",".join(parameters) + "\n"
                f.write(row)
                

    def generate_id(self):
        if len(self.elements) == 0:
            return 1
        self.elements.sort(key=lambda x: x.id)
        last_element = self.elements[-1]
        return last_element.id + 1
    
    def add_review(self, review: RecenzijaUrednika):
        self.elements.append(review)
        self.save()
        self.subject.notify_observers()

    def delete_review(self, id: int):
        review_to_remove = None
        for element in self.elements:
            if element.id == id:
                review_to_remove = element
                break
        if review_to_remove != None:
            self.elements.remove(review_to_remove)
            self.save()
            self.subject.notify_observers()

    def get_all_reviews(self):
        return self.elements

    def get_by_id(self, id : int):
        for element in self.elements:
            if element.id == id:
                return element
        return None   
    
    def get_reviews_by_element(self, element, element_type):
        found_reviews = []
        for review in self.elements:
            if review.muzicki_element.id == element.id and review.vrsta_elementa == element_type:
                found_reviews.append(review)
        return found_reviews

    def get_reviews_by_music_element(self, element: MuzickiElement):
        if isinstance(element, Ucesnik):
            return self.get_reviews_by_element(element, "Izvodjac")
        elif isinstance(element, MuzickoDelo):
            return self.get_reviews_by_element(element, "Muzicko delo")
        elif isinstance(element, Grupa):
            return self.get_reviews_by_element(element, "Grupa")
        else:
            return self.get_reviews_by_element(element, "Album")
