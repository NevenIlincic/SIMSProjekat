import sys
from PyQt5.QtWidgets import QApplication
from View.StartingMenuView import MainWindow  # Uvoz klase MainWindow iz StartingMenuView modula
from Controller.UserAccountController import UserAccountController
from Controller.RegisteredUserController import RegisteredUserController
from Model.DTO.UserAccountDTO import UserAccountDTO
from Model.Models.Enumerations import VrstaKorisnika
from Model.DTO.UserDTO import UserDTO
from Model.Models.Enumerations import Pol
from Model.Service.ComplexSerice import ComplexService
from Controller.MusicalPieceController import MusicalPieceController
from Model.DTO.MusicalPieceDTO import MusicalPieceDTO
from Controller.GroupController import GroupController
from Model.DTO.GroupDTO import GroupDTO
from Controller.ParticipantController import ParticipantController
from Model.Models.Grupa import Grupa


if __name__ == "__main__":
    # kontroler = UserAccountController()
    # # #kontroler.delete_account(2)
    # dto = UserAccountDTO("Imer", "sifrica", "Registrovani korisnik")
    # account = kontroler.add_account(dto)
    # user_dto = UserDTO("Pero", "Ilincic", Pol.Muski, account)
    # kontroler_user = RegisteredUserController()
    # kontroler_user.add_user(user_dto)
    #kontroler_user.add_user(user_dto)
    # service = ComplexService()
    # service.delete_registered_user(2)
    #
    pKontroler = ParticipantController()
    grKontroler = GroupController(pKontroler)
    grupa = grKontroler.get_by_id(1)
    # grDto = GroupDTO("Crvena Jabuka", "null", 122, 12, 35, "nesto", [])
    # grKontroler.add_group(grDto)
    kontroler = MusicalPieceController(grKontroler)
    dto = MusicalPieceDTO("Malo cemo da se kupamo", "null", "nesto", 122, 9, 40, grupa)
    kontroler.add_piece(dto)
    app = QApplication(sys.argv)
    
    # Instanciranje glavnog prozora
    main_window = MainWindow()
    main_window.show()
    
    sys.exit(app.exec_())