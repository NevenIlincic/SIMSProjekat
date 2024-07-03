from Model.Repository.TaskRepository import TaskRepository
from Model.Models.Zadatak import Zadatak
from Model.DTO.TaskDTO import ZadatakDTO
from Model.Repository.MusicalElementRepository import MusicalElementRepository

class TaskController(): 
    def __init__(self, musical_piece_controller) -> None:
        self.task_repository = TaskRepository(musical_piece_controller)
        self.musical_piece_controller = MusicalElementRepository()

    def add_task(self, task_dto: ZadatakDTO):
        muzicka_dela_ids = [md.id for md in task_dto.muzicka_dela]
        new_task = Zadatak(
            0,  # ID will be generated by the repository
            task_dto.tekst,
            task_dto.uradjen,
            [self.musical_piece_controller.get_by_id(md_id) for md_id in muzicka_dela_ids]
        )
        added_task = self.task_repository.add_task(new_task)
        return added_task
    
    def load(self):
        return self.task_repository.load()
    
    def delete_task(self, id: int):
        return self.task_repository.delete_task(id)
    
    def convert_DTO_to_model(self, task_dto : ZadatakDTO):
        if isinstance(task_dto, ZadatakDTO):
            muzicka_dela = [self.musical_piece_controller.get_by_id(md.id) for md in task_dto.muzicka_dela]
            return Zadatak(
                task_dto.id,
                task_dto.tekst,
                task_dto.uradjen,
                muzicka_dela
            )
    
    def get_all_tasks(self):
        return self.task_repository.get_all_tasks()

    def get_by_id(self, id: int):
        return self.task_repository.get_by_id(id)
    