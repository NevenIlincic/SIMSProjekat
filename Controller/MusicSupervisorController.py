from Model.DTO.UserDTO import UserDTO
from Model.Models.MuzickiUrednik import MuzickiUrednik
from Model.Repository.MusicSupervisorRepository import MusicSupervisorRepository

class MusicSupervisorController():
    def __init__(self) -> None:
        self.musicSupervisorRepository = MusicSupervisorRepository()
    
    def add_supervisor(self, user: UserDTO):
        id = self.musicSupervisorRepository.generate_id()
        new_supervisor = self.convert_DTO_to_model(user)
        new_supervisor.id = id
        self.musicSupervisorRepository.add_supervisor(new_supervisor)
        return new_supervisor
        

    def update_supervisor(self, supervisor: MuzickiUrednik):
        return self.musicSupervisorRepository.update_supervisor(supervisor)

    def get_all_supervisors(self):
        return self.musicSupervisorRepository.get_all_supervisors()
    
    def find_supervisor_by_account(self, id: int):
        all_supervisors = self.get_all_supervisors()
        found_supervisor = None
        for supervisor in all_supervisors:
            if supervisor.korisnicki_nalog.id == id:
                found_supervisor = supervisor
                break
        return found_supervisor
    
    def convert_DTO_to_model(self, dto):
        if isinstance(dto, UserDTO):
            return MuzickiUrednik(0, dto.ime, dto.prezime, dto.pol, False, [], [], dto.korisnicki_nalog)