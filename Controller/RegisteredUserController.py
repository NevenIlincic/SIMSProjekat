from Model.Repository.RegisteredUserRepository import RegisteredUsersRepository
from Model.DTO.UserDTO import UserDTO
from Model.Models.Korisnik import Korisnik

class RegisteredUserController():
    def __init__(self) -> None:
        self.registered_user_repository = RegisteredUsersRepository()
    
    def add_user(self, user: UserDTO):
        id = self.registered_user_repository.generate_id()
        new_user = self.convert_DTO_to_model(user)
        new_user.id = id
        self.registered_user_repository.add_user(new_user)
    
    def load(self):
        return self.registered_user_repository.load()
    
    def delete_account(self, id: int):
        return self.registered_user_repository.delete_user(id)
    
    def get_all_users(self):
        return self.registered_user_repository.get_all_users()
    
    def find_user_by_account(self, id: int):
        all_users = self.get_all_users()
        found_user = None
        for user in all_users:
            if user.korisnicki_nalog.id == id:
                found_user = user
                break
        return found_user
    
    def convert_DTO_to_model(self,user_dto):
        if isinstance(user_dto, UserDTO):
            return Korisnik(0, user_dto.ime, user_dto.prezime, user_dto.pol, False, user_dto.korisnicki_nalog)
        
    
    def valid_name(self, user_dto):
        name : str = user_dto.ime
        surname : str = user_dto.prezime
        error_message_name = "Name is not valid"
        error_message_surname = "Surname is not valid"

        if not name.isalpha(): 
            return error_message_name, False
        if not surname.isalpha():
            return error_message_surname, False
        
        if len(name) > 25:
            return error_message_name, False
        if len(surname) > 25:
            return error_message_surname, False
        
        return "", True