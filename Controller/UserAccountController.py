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

    def convert_DTO_to_model(self,user_account_dto):
        if isinstance(user_account_dto, UserAccountDTO):
            return KorisnickiNalog(0, user_account_dto.korisnicko_ime, user_account_dto.lozinka, user_account_dto.uloga)