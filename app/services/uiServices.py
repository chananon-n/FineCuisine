import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from app.services.userServices import *
import transaction

from app.gui.login.loginPage import Ui_MainWindow as loginPage
from app.gui.register.registerPage import Ui_MainWindow as registerPage
from app.gui.mainPage.mainPage import Ui_MainWindow as mainPage
from app.gui.course.coursePage import Ui_MainWindow as coursePage

from datetime import datetime
    

class LoginPage(QMainWindow, loginPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.signinBtn.clicked.connect(self.openRegisterPage)
        self.loginBtn.clicked.connect(self.loginBTN)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        
    def openRegisterPage(self):
        self.registerPage = RegisterPage()
        self.registerPage.show()
        self.hide()
    
    def loginBTN(self):
        self.mainPage = MainPage()
        self.mainPage.show()
        self.hide()
        # result = UserServices.login(self.usernameInput.text(), self.passwordInput.text())
        # if result == "Admin":
        #     # self.adminPage = AdminPage()
        #     # self.adminPage.show()
        #     # self.hide()
        #     pass
        # elif result == "Client":
        #     # self.clientPage = ClientPage()
        #     # self.clientPage.show()
        #     # self.hide()
        #     pass
        # else:
        #     alert =QtWidgets.QMessageBox()
        #     alert.setText("Invalid username or password")
        #     alert.exec()

class RegisterPage(QMainWindow, registerPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #phone number input only accepts numbers
        self.phoneInput.setValidator(QtGui.QIntValidator())
        self.redirectBtn.clicked.connect(self.backToLogin)
        self.registerBtn.clicked.connect(self.register)
        
    def backToLogin(self):
        self.loginPage = LoginPage()
        self.loginPage.show()
        self.hide()
    
    def register(self):
        pass
      
class MainPage(QMainWindow, mainPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pageWidget.setCurrentIndex(0)
        
        #sidebar buttons
        self.homeBtn.clicked.connect(self.openHomePage)
        self.userinfoBtn.clicked.connect(self.openUserInfo)
        self.notiBtn.clicked.connect(self.openNotification)
        self.historyBtn.clicked.connect(self.openHistory)
        self.feedbackBtn.clicked.connect(self.openFeedback)
        
        #hoompage buttons
        self.courseBtn.clicked.connect(self.openCoursePage)
        
        self.logoutBtn.clicked.connect(self.logout)
        
    def openHomePage(self):
        self.pageWidget.setCurrentIndex(0)
        
        self.courseBtn.clicked.connect(self.openCoursePage)
        
    def openUserInfo(self):
        self.pageWidget.setCurrentIndex(1)
        membership = False
        if membership:
            self.registerBtn.hide()
        else:
            self.birthDateLabel.hide()
            self.userBirth.hide()
            self.dateExpireLabel.hide()
            self.userExpire.hide()
        
    def openNotification(self):
        self.pageWidget.setCurrentIndex(2)
        
    def openHistory(self):
        self.pageWidget.setCurrentIndex(3)
        self.historyTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.historyTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        #add data to the table
        self.historyTable.setRowCount(5)
        self.historyTable.setColumnCount(4)
        self.historyTable.setItem(0, 0, QtWidgets.QTableWidgetItem("1"))
        self.historyTable.setItem(0, 1, QtWidgets.QTableWidgetItem("Course 1"))
        self.historyTable.setItem(0, 2, QtWidgets.QTableWidgetItem(f"{datetime.now()}"))
        self.historyTable.setItem(0, 3, QtWidgets.QTableWidgetItem("Completed"))
        self.historyTable.setItem(1, 0, QtWidgets.QTableWidgetItem("2"))
        self.historyTable.setItem(1, 1, QtWidgets.QTableWidgetItem("Course 2"))
        self.historyTable.setItem(1, 2, QtWidgets.QTableWidgetItem(f"{datetime.now()}"))
        self.historyTable.setItem(1, 3, QtWidgets.QTableWidgetItem("Completed"))
        
        
    def openFeedback(self):
        self.pageWidget.setCurrentIndex(4)
        
    def logout(self):
        self.loginPage = LoginPage()
        self.loginPage.show()
        self.hide()
        
    def openCoursePage(self):
        self.coursePage = CoursePage()
        self.coursePage.show()
        self.hide()
        
class CoursePage(QMainWindow, coursePage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mainPage = MainPage()
        
        # Sidebar buttons
        self.homeBtn.clicked.connect(self.openHomePage)
        self.userinfoBtn.clicked.connect(self.openUserInfo)
        self.notiBtn.clicked.connect(self.openNotification)
        self.historyBtn.clicked.connect(self.openHistory)
        self.feedbackBtn.clicked.connect(self.openFeedback)
        
        self.logoutBtn.clicked.connect(self.mainPage.logout)
        
    def openHomePage(self):
        self.mainPage.show()
        self.mainPage.openHomePage()
        self.hide()
        
    def openUserInfo(self):
        self.mainPage.show()
        self.mainPage.openUserInfo()
        self.hide()
        
    def openNotification(self):
        self.mainPage.show()
        self.mainPage.openNotification()
        self.hide()
        
    def openHistory(self):
        self.mainPage.show()
        self.mainPage.openHistory()
        self.hide()
        
    def openFeedback(self):
        self.mainPage.show()
        self.mainPage.openFeedback()
        self.hide()
