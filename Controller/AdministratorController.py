from Model.Repository.AdministratorRepository import AdministratorRepository

class AdministratorController():
    def __init__(self) -> None:
        self.administrator_repository = AdministratorRepository()
    
    def get_administrator_by_id(self, id):
        return self.administrator_repository.get_administrator_by_id(id)
    
    def get_all_administrators(self):
        return self.administrator_repository.get_all_administrators()
    
    def find_administrator_by_account(self, id: int):
        all_administrators = self.get_all_administrators()
        found_administrator = None
        for administrator in all_administrators:
            if administrator.korisnicki_nalog.id == id:
                found_administrator = administrator
                break
        return found_administrator
