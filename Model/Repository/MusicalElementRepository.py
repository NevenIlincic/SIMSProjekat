from Model.Models.MuzickiElement import MuzickiElement
from Model.Observer.Subject import Subject

class MusicalElementRepository():
    def __init__(self) -> None:
        self.elements = []
        self.path = "Data/MusicalElements.txt"
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
        return MuzickiElement(int(parameters[0]), parameters[1], parameters[2], int(parameters[3]), int(parameters[4]), int(parameters[5]))
    
    def convert_to_list(self, entity: MuzickiElement):
        return [str(entity.id), entity.naziv, entity.slika, str(entity.pregledi), str(entity.broj_ocena), str(entity.zbir_ocena)]
    
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

    def add_element(self, element: MuzickiElement):
        self.elements.append(element)
        self.save()
        self.subject.notify_observers()

    def delete_element(self, id: int):
        element_to_remove = None
        for element in self.elements:
            if element.id == id:
                element_to_remove = element
                break
        if element_to_remove != None:
            self.elements.remove(element_to_remove)
            self.save()
            self.subject.notify_observers()

    def get_all_elements(self):
        return self.elements

    def get_by_id(self, id):
        for element in self.elements:
            if element.id == id:
                return element
        return False
