from Model.Repository.UserAccountRepository import UserAccountRepository
from Model.Models.KorisnickiNalog import KorisnickiNalog
from Model.DTO.UserAccountDTO import UserAccountDTO

class UserAccountController():
    def __init__(self) -> None:
        self.UserAccountRepository = UserAccountRepository()
    
    def add_account(self, account: UserAccountDTO):
        id = self.UserAccountRepository.generate_id()
        new_account = self.convert_DTO_to_model(account)
        new_account.id = id
        self.UserAccountRepository.add_account(new_account)
    
    def load(self):
        return self.UserAccountRepository.load()
    
    def delete_account(self, id: int):
        return self.UserAccountRepository.delete_account(id)
    
    def convert_DTO_to_model(self,user_account_dto):
        if isinstance(user_account_dto, UserAccountDTO):
            return KorisnickiNalog(0, user_account_dto.korisnicko_ime, user_account_dto.lozinka, user_account_dto.uloga)