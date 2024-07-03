from Model.Models.MuzickiElement import MuzickiElement
from Model.Observer.Subject import Subject
from Model.Models import RecenzijaUrednika
from Model.Repository.MusicalElementRepository import MusicalElementRepository
class EditorsReviewRepository():
    def __init__(self) -> None:
        self.elements = []
        self.path = "Data/EditorsReview.txt"
        self.__musical_element_repository = MusicalElementRepository()
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
        muzicki_element_id = parameters[4]
        muzicki_element = self.__musical_element_repository.get_by_id(int(muzicki_element_id))
       
        b = False
        if parameters[3] == "False":
            b = False
        else:
            b = bool(parameters[3])

        return RecenzijaUrednika(int(parameters[0]), parameters[1] ,int(parameters[2]), b, muzicki_element)
    

    def convert_to_list(self, entity: RecenzijaUrednika):
        return [str(entity.id),entity.opis,str(entity.ocena), str(entity.menja_se), str(entity.muzickiElement.id)]
     

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
        return False   
