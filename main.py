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
    app = QApplication(sys.argv)
    
    # Instanciranje glavnog prozora
    main_window = MainWindow()
    main_window.show()
    
    sys.exit(app.exec_())