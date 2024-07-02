from Model.Repository.UserAccountRepository import UserAccountRepository
from Model.Models.KorisnickiNalog import KorisnickiNalog
from Model.DTO.UserAccountDTO import UserAccountDTO

class UserAccountController():
    def __init__(self) -> None:
        self.user_account_repository = UserAccountRepository()
    
    def add_account(self, account: UserAccountDTO):
        id = self.user_account_repository.generate_id()
        new_account = self.convert_DTO_to_model(account)
        new_account.id = id
        self.user_account_repository.add_account(new_account)
        return new_account
    
    def load(self):
        return self.user_account_repository.load()
    
    def delete_account(self, id: int):
        return self.user_account_repository.delete_account(id)
    
    def get_all_accounts(self):
        return self.user_account_repository.get_all_accounts()
    
    def get_account_by_id(self, id: int):
        return self.user_account_repository.get_by_id(id)
    
    def get_account_by_username(self, username: str):
        return self.user_account_repository.get_by_username(username)

    def convert_DTO_to_model(self,user_account_dto):
        if isinstance(user_account_dto, UserAccountDTO):
            return KorisnickiNalog(0, user_account_dto.korisnicko_ime, user_account_dto.lozinka, user_account_dto.uloga.value)             
        
    def valid_username(self, user_account_dto):
        username : str = user_account_dto.korisnicko_ime
        error_message_username = "Username is not valid"

        if len(username) > 35 and len(username) < 8:
            return error_message_username, False

        account = self.get_account_by_username(username)
        if account != None:
            return error_message_username, False
        
        return "", True

    def valid_password(self, user_account_dto):
        password : str = user_account_dto.lozinka
        error_message_password = "Password is not valid"

        if len(password) > 35 and len(password) < 8:
            return error_message_password, False

        valid = self.chack_password_valid_format(password)
        if not valid:
           return error_message_password, False
        
        return "", True
    

    def chack_password_valid_format(self, password):     
        sadrzi_malo = False
        sadrzi_veliko = False
        sadrzi_broj = False
        sadrzi_znak = False

        for char in password:
            if char.islower():
                sadrzi_malo = True
            elif char.isupper():
                sadrzi_veliko = True
            elif char.isdigit():
                sadrzi_broj = True
            elif not char.isalnum():
                sadrzi_znak = True

            if sadrzi_malo and sadrzi_veliko and sadrzi_broj and sadrzi_znak:
                break

        return sadrzi_malo and sadrzi_veliko and sadrzi_broj and sadrzi_znak
