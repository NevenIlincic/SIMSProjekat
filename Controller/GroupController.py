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
        ucesnici_ids = [u.id for u in group_dto.ucesnici]
        new_group = Grupa(
            0,  # ID will be generated by the repository
            group_dto.naziv,
            group_dto.slika,
            group_dto.pregledi,
            group_dto.broj_ocena,
            group_dto.zbir_ocena,
            group_dto.tekst,
            ucesnici_ids
        )
        added_group = self.group_repository.add_group(new_group)
        return added_group
    
    def load(self):
        return self.group_repository.load()
    
    def delete_group(self, id: int):
        return self.group_repository.delete_group(id)
    
    def convert_DTO_to_model(self, group_dto):
        if isinstance(group_dto, GroupDTO):
            ucesnici = [self.participant_controller.get_by_id(u_id) for u_id in group_dto.ucesnici]
            return Grupa(
                group_dto.id,
                group_dto.naziv,
                group_dto.slika,
                group_dto.pregledi,
                group_dto.broj_ocena,
                group_dto.zbir_ocena,
                group_dto.tekst,
                ucesnici
            )
    
    def get_all_groups(self):
        return self.group_repository.get_all_groups()

    def get_by_id(self, id: int):
        return self.group_repository.get_by_id(id)
