import sys
from PyQt5.QtWidgets import QApplication
from View.StartingMenuView import MainWindow  # Uvoz klase MainWindow iz StartingMenuView modula
from View.RegisteredUserView import RegisteredUserWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Instanciranje glavnog prozora
    main_window = MainWindow()
    main_window.show()
    
    sys.exit(app.exec_())