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