import sys
from PyQt5.QtWidgets import QApplication
from View.StartingMenuView import MainWindow  # Uvoz klase MainWindow iz StartingMenuView modula
from Controller.UserAccountController import UserAccountController
from Model.DTO.UserAccountDTO import UserAccountDTO
from Model.Models.Enumerations import VrstaKorisnika

if __name__ == "__main__":
    kontroler = UserAccountController()
    #kontroler.delete_account(2)
    dto = UserAccountDTO("DJomla", "sifrica", "Registrovani korisnik")
    kontroler.add_account(dto)
    # app = QApplication(sys.argv)
    
    # # Instanciranje glavnog prozora
    # main_window = MainWindow()
    # main_window.show()
    
    # sys.exit(app.exec_())