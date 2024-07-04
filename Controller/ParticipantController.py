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
                participant_dto.pol,
                participant_dto.datum_rodjenja, 
                participant_dto.biografija, 
                participant_dto.zanrovi, 
                participant_dto.reklamira_se
            )
    
    def get_all_participants(self):
        return self.participant_repository.get_all_participants()

    def get_by_id(self, id: int):
        return self.participant_repository.get_by_id(id)
    
    def get_by_pseodonym(self, pseudonym):
        return self.participant_repository.get_by_pseudonym(pseudonym)
    
    def get_participants_first_last_name_pseudonym(self, first_name, last_name, pseudonym):
        participants = self.get_all_participants()
        found_participants_first_name = []
        found_participants_last_name = []
        found_participant = None
        found_participant_pseudonym = self.get_by_pseodonym(pseudonym)
        
        for participant in participants:
            if participant.ime == first_name:
                found_participants_first_name.append(participant)
            if participant.prezime == last_name:
                found_participants_last_name.append(participant)
            if participant.ime == first_name and participant.prezime == last_name:
                found_participant = participant
        
        
        return (found_participant, found_participant_pseudonym, found_participants_first_name, found_participants_last_name)