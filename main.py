import sys
from PyQt5.QtWidgets import QApplication
from View.StartingMenuView import MainWindow  # Uvoz klase MainWindow iz StartingMenuView modula
from Controller.UserAccountController import UserAccountController

if __name__ == "__main__":
    kontroler = UserAccountController()
    kontroler.delete_account(1)
    # app = QApplication(sys.argv)
    
    # # Instanciranje glavnog prozora
    # main_window = MainWindow()
    # main_window.show()
    
    # sys.exit(app.exec_())