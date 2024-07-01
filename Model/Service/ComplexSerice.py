from Controller.UserAccountController import UserAccountController
from Controller.RegisteredUserController import RegisteredUserController
from Model.DTO.UserInformationsDTO import UserInformationsDTO

class ComplexService():
    def __init__(self) -> None:
        self.user_account_controller = UserAccountController()
        self.registered_account_controller = RegisteredUserController()
    
    def user_login(self, username, password):
        all_accounts = self.user_account_controller.get_all_accounts()
        found_account = None
        for account in all_accounts:
            if account.korisnicko_ime == username:
                if account.lozinka == password:
                    found_account = account
                    break
        if found_account == None:
            return None
        found_user = self.registered_account_controller.find_user_by_account(found_account.id)
        if found_user == None:
            return None
        
        user_informations_dto = UserInformationsDTO(found_account.korisnicko_ime, found_account.lozinka, found_user.ime,
                                                    found_user.prezime, found_user.pol, found_user.korisnicki_nalog.uloga)
        return user_informations_dto
        
        

