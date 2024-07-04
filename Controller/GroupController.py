from Controller.ParticipantController import ParticipantController
from Model.DTO.GroupFormDTO import GroupFormDTO
from Model.Repository.GroupRepository import GroupRepository
from Model.Models.Grupa import Grupa
from Model.DTO.GroupDTO import GroupDTO
from Model.DTO.ParticipantDTO import ParticipantDTO
from Model.Models.Ucesnik import Ucesnik

class GroupController():
    def __init__(self) -> None:
        self.group_repository = GroupRepository()
        self.participant_controller = ParticipantController()
    
    def add_group(self, group_dto: GroupFormDTO):
        id = self.group_repository.generate_id()
        new_group = self.convert_DTO_to_model(group_dto)
        new_group.id = id
        self.group_repository.add_group(new_group)
        return new_group
    
    def load(self):
        return self.group_repository.load()
    
    def delete_group(self, id: int):
        return self.group_repository.delete_group(id)
    
    def convert_DTO_to_model(self, group_dto):
        if isinstance(group_dto, GroupFormDTO):
            participants = [self.participant_controller.get_by_id(participant.id) for participant in group_dto.participants]
            return Grupa(
                0,
                group_dto.name,
                group_dto.image,
                0,
                0,
                0,
                participants
            )
    
    def get_all_groups(self):
        return self.group_repository.get_all_groups()

    def get_by_id(self, id: int):
        return self.group_repository.get_by_id(id)
    
    def get_by_naziv(self, naziv: str):
        return self.group_repository.get_by_naziv(naziv)
