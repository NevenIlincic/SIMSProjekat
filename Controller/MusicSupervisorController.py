from Model.Repository.MusicSupervisorRepository import MusicSupervisorRepository

class MusicSupervisorController():
    def __init__(self) -> None:
        self.musicSupervisorRepository = MusicSupervisorRepository()
    
    def login(self, name, last_name):
        supervisors = self.get_all_supervisors()
        for supervisor in supervisors:
            if supervisor.ime == name:
                if supervisor.prezime == last_name:
                    return supervisor
                return False
        return False
    
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