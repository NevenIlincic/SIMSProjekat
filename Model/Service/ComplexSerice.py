from Controller.AlbumController import AlbumController
from Controller.EditorsReviewController import EditorsReviewController
from Controller.GroupController import GroupController
from Controller.MusicalPieceController import MusicalPieceController
from Controller.UserAccountController import UserAccountController
from Controller.RegisteredUserController import RegisteredUserController
from Model.DTO.EditorsReviewDTO import EditorsReviewDTO
from Model.DTO.AlbumFormDTO import AlbumFormDTO

from Model.DTO.GroupFormDTO import GroupFormDTO
from Model.DTO.UserInformationsDTO import UserInformationsDTO
from Controller.MusicSupervisorController import MusicSupervisorController
from Model.DTO import UserDTO, UserAccountDTO
from Controller.AdministratorController import AdministratorController
from Controller.ParticipantController import ParticipantController
from Controller.MusicalElementController import MusicalElementController
from Controller.ListoOfFavouritesController import ListOfFavouritesController
from Model.Models.MuzickiElement import MuzickiElement

class ComplexService():
    def __init__(self) -> None:
        self.user_account_controller = UserAccountController()
        self.registered_account_controller = RegisteredUserController()
        self.supervisor_controller = MusicSupervisorController()
        self.participant_controller = ParticipantController()
        self.administrator_controller = AdministratorController()
        self.group_controller = GroupController()
        self.musical_element_controller = MusicalElementController()
        self.list_controller = ListOfFavouritesController()
        
    def account_login(self, username, password, role: str):
        all_accounts = self.user_account_controller.get_all_accounts()
        found_account = None
        for account in all_accounts:
            if account.korisnicko_ime == username:
                if account.lozinka == password:
                    found_account = account
                    break
        if found_account == None:
            return None
        
        found_user = None
        if role == "Registered user":
            found_user = self.registered_account_controller.find_user_by_account(found_account.id)
        elif role == "Music supervisor":
            found_user = self.supervisor_controller.find_supervisor_by_account(found_account.id)
        else:
            found_user = self.administrator_controller.find_administrator_by_account(found_account.id)
            
        if found_user == None:
                return None  
        user_informations_dto = UserInformationsDTO(found_account.korisnicko_ime, found_account.lozinka, found_user.ime,
                                                    found_user.prezime, found_user.pol, found_user.korisnicki_nalog.uloga)
        return user_informations_dto
        
    def delete_registered_user(self, id: int):
        user_to_remove = self.registered_account_controller.delete_account(id)
        if user_to_remove == None: 
            return None
        account_to_remove = self.user_account_controller.get_account_by_id(user_to_remove.id)
        self.user_account_controller.delete_account(account_to_remove.id)
        return user_to_remove

    def validate_data_for_registration(self, user_dto : UserDTO, user_account_dto : UserAccountDTO):
        error_message = ""
        valid = True

        message, valid_password = self.user_account_controller.valid_password(user_account_dto)
        if not valid_password:
            error_message = message + " "

        message, valid_name = self.registered_account_controller.valid_name(user_dto)
        if not valid_name:
            error_message += message + " "

        message, valid_username = self.user_account_controller.valid_username(user_account_dto)
        if not valid_username:
            error_message += message + " "


        if (valid_username == False or valid_name == False or valid_password == False):
            valid = False

        return error_message, valid
    
    def validate_data_for_group_adding(self, group_form_dto: GroupFormDTO):
        if self.group_controller.get_by_naziv(group_form_dto.name) != None:
            return ("Group with that name already exists!", False)
        if group_form_dto.name == "":
            return ("Group has to have name!", False)
        return ("",True)

    def validate_data_for_album_adding(self, album_form_dto: AlbumFormDTO):
        if self.album_controller.get_by_naziv(album_form_dto.album_name):
            return ("Album with that name already exists!", False)
        if album_form_dto.album_name == "":
            return ("Album has to have name!", False)
        if len(album_form_dto.musical_pieces) == 0:
            return ("Album has to have at least one piece!", False)
        return ("", True)

    def validate_data_for_review_adding(self, review_dto: EditorsReviewDTO):
        if review_dto.opis == "":
            return ("You need to add description!", False)
        return("", True)
    
    def check_for_user_review(self, user_informations_dto: UserInformationsDTO, element: MuzickiElement):
        accounts = self.user_account_controller.get_all_accounts()
        user_account = None
        for acc in accounts:
            if acc.korisnicko_ime == user_informations_dto.korisnicko_ime:
                if acc.lozinka == user_informations_dto.lozinka:
                    user_account = acc
                    break
        supervisor = self.supervisor_controller.find_supervisor_by_account(user_account.id)
        if element in supervisor.recenzije:
            return("", True)
        else:
            return("You already added review!", False)


    def register_new_user(self, user_dto, user_account_dto):  
        account = self.user_account_controller.add_account(user_account_dto)
        user_dto.korisnicki_nalog = account
        self.registered_account_controller.add_user(user_dto)

    def register_new_supervisor(self, user_dto, user_account_dto):
        account = self.user_account_controller.add_account(user_account_dto)
        user_dto.korisnicki_nalog = account
        self.supervisor_controller.add_supervisor(user_dto)

    def add_new_participant(self, participant_dto): 
        self.participant_controller.add_participant(participant_dto) 
    
    def add_new_group(self, group_dto):
        self.group_controller.add_group(group_dto)
    
    def add_new_album(self, album_dto):
        self.album_controller.add_album(album_dto)

    def add_review(self, editors_review_dto, user_informations_dto):
        accounts = self.user_account_controller.get_all_accounts()
        user_account = None
        for acc in accounts:
            if acc.korisnicko_ime == user_informations_dto.korisnicko_ime:
                if acc.lozinka == user_informations_dto.lozinka:
                    user_account = acc
                    break
        supervisor = self.supervisor_controller.find_supervisor_by_account(user_account.id)
        review = self.editors_review_controller.add_review(editors_review_dto)
        supervisor.recenzije.append(review)
        self.supervisor_controller.update_supervisor(supervisor)