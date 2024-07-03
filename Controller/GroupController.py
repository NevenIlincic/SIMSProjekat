from Model.Repository.GroupRepository import GroupRepository
from Model.Models.Grupa import Grupa
from Model.DTO.GroupDTO import GroupDTO
from Model.DTO.ParticipantDTO import ParticipantDTO
from Model.Models.Ucesnik import Ucesnik

class GroupController():
    def __init__(self, participant_controller) -> None:
        self.group_repository = GroupRepository(participant_controller)
        self.participant_controller = participant_controller
    
    def add_group(self, group_dto: GroupDTO):
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
        if isinstance(group_dto, GroupDTO):
            ucesnici = [self.participant_controller.get_by_id(u_id) for u_id in group_dto.ucesnici]
            return Grupa(
                0,
                group_dto.naziv,
                group_dto.slika,
                group_dto.pregledi,
                group_dto.broj_ocena,
                group_dto.zbir_ocena,
                ucesnici
            )
    
    def get_all_groups(self):
        return self.group_repository.get_all_groups()

    def get_by_id(self, id: int):
        return self.group_repository.get_by_id(id)
    
    def get_by_naziv(self, naziv: str):
        return self.group_repository.get_by_naziv(naziv)
