from app.services.uiServices import LoginPage
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication  
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginPage()
    window.show()
    sys.exit(app.exec_())