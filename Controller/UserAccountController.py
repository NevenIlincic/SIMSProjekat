from Model.Repository.UserAccountRepository import UserAccountRepository
from Model.Models.KorisnickiNalog import KorisnickiNalog

class UserAccountController():
    def __init__(self) -> None:
        self.UserAccountRepository = UserAccountRepository()
    
    def add_account(self, account: KorisnickiNalog):
        self.UserAccountRepository.save()
    
    def load(self):
        return self.UserAccountRepository.load()
    
    def delete_account(self, id: int):
        return self.UserAccountRepository.delete_account(id)