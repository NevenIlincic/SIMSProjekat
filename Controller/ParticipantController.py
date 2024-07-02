from Model.Repository.ParticipantRepository import ParticipantRepository
from Model.Models.Ucesnik import Ucesnik
from Model.DTO.ParticipantDTO import ParticipantDTO
from Model.Models.Enumerations import Pol

class ParticipantController():
    def __init__(self) -> None:
        self.participant_repository = ParticipantRepository()
    
    def add_participant(self, participant_dto: ParticipantDTO):
        id = self.participant_repository.generate_id()
        new_participant = self.convert_DTO_to_model(participant_dto)
        new_participant.id = id
        self.participant_repository.add_participant(new_participant)
        return new_participant
    
    def load(self):
        return self.participant_repository.load()
    
    def delete_participant(self, id: int):
        return self.participant_repository.delete_participant(id)
    
    def convert_DTO_to_model(self, participant_dto):
        if isinstance(participant_dto, ParticipantDTO):
            return Ucesnik(
                0,  # ID will be set later
                participant_dto.naziv, 
                participant_dto.slika, 
                participant_dto.pregledi, 
                participant_dto.broj_ocena, 
                participant_dto.zbir_ocena, 
                participant_dto.ime, 
                participant_dto.prezime, 
                Pol[participant_dto.pol],  # assuming pol is passed as string and needs to be converted to Enum
                participant_dto.datum_rodjenja, 
                participant_dto.biografija, 
                participant_dto.zanrovi, 
                participant_dto.reklamira_se
            )
    
    def get_all_participants(self):
        return self.participant_repository.get_all_participants()

    def get_by_id(self, id: int):
        return self.participant_repository.get_by_id(id)
