import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
import transaction

from app.gui.login.loginPage import Ui_MainWindow as loginPage
# from app.UI.registerPage import Ui_Dialog as registerPage

class LoginPage(QMainWindow, loginPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.signinBtn.clicked.connect(self.openRegisterPage)
        self.loginBtn.clicked.connect(self.login)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        
    # def openRegisterPage(self):
    #     self.registerPage = RegisterPage()
    #     self.registerPage.show()
    #     self.hide()