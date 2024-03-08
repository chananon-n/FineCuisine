import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QFileDialog, QVBoxLayout, QFormLayout, QSizePolicy
from app.controller.userServices import *
import transaction

from app.gui.login.loginPage import Ui_MainWindow as loginPage
from app.gui.register.registerPage import Ui_MainWindow as registerPage
from app.gui.mainPage.mainPage import Ui_MainWindow as mainPage
from app.gui.course.coursePage import Ui_MainWindow as coursePage
from app.gui.reservation.reservationPage import Ui_MainWindow as reservationPage
from app.gui.registerMembership.registerMembershipPage import Ui_MainWindow as registerMembershipPage
from app.gui.news.newsPage import Ui_MainWindow as newsPage
from app.gui.news.newsBlog import Ui_Blog as newsBlog

from app.gui.adminMainPage.adminMainPage import Ui_MainWindow as adminMainPage

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
        global userRole
        global userID
        global userServices 
        userServices = UserServices()
        userRole = userServices.login(self.usernameInput.text(), self.passwordInput.text())
        if userRole == "admin":
            userID = userServices.getAdminID(self.usernameInput.text())
            userRole = "admin"
            print(userID)
            self.adminMainPage = AdminMainPage()
            self.adminMainPage.show()
            self.hide()
            pass
        elif userRole == "client":
            userID = userServices.getClientID(self.usernameInput.text())
            userRole = "client"
            print(userID)
            self.mainPage = MainPage()
            self.mainPage.show()
            self.hide()
        else:
            alert =QtWidgets.QMessageBox()
            alert.setText("Invalid username or password")
            alert.exec()

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
        global userServices
        userServices = UserServices()
        if self.usernameInput.text() and self.passwordInput.text() and self.emailInput.text() and self.phoneInput.text():
            userServices.register(self.usernameInput.text(), self.passwordInput.text(), self.emailInput.text(), self.phoneInput.text())
            alert =QtWidgets.QMessageBox()
            alert.setText("Registration successful!")
            alert.exec()
            self.loginPage = LoginPage()
            self.loginPage.show()
            self.hide()
        else:
            alert =QtWidgets.QMessageBox()
            alert.setText("Please fill in all information")
            alert.exec()
      
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
        
        #homepage buttons
        self.courseBtn.clicked.connect(self.openCoursePage)
        self.reservationBtn.clicked.connect(self.openReservationPage)
        self.newsBtn.clicked.connect(self.openNewsPage)
        
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
        self.registerBtn.clicked.connect(self.openRegisterMemberPage)
        
    def openRegisterMemberPage(self):
        self.registerMembershipPage = RegisterMembershipPage()
        self.registerMembershipPage.show()
        self.hide()
        
    def openNotification(self):
        self.pageWidget.setCurrentIndex(2)
        self.generateNotification()
    
    def generateNotification(self):
        for i in range(10):
            self.notificationDetail = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
            self.notificationDetail.setObjectName(f"notificationDetail_{i}")
            sizePolicy = QtWidgets.QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.notificationDetail.sizePolicy().hasHeightForWidth())
            self.notificationDetail.setSizePolicy(sizePolicy)
            self.notificationDetail.setMinimumSize(QSize(1100, 50))
            self.notificationDetail.setMaximumSize(QSize(1100, 50))
            self.notificationDetail.setLayoutDirection(Qt.LeftToRight)
            self.notificationDetail.setStyleSheet(u"color: rgb(0, 0, 0);\n"
    "font: 700 18pt \"KoHo\";\n"
    "border: 1 solid black;\n"
    "border-radius: 8px")
            self.notificationDetail.setFrameShape(QFrame.NoFrame)
            self.notificationDetail.setFrameShadow(QFrame.Sunken)
            self.notificationDetail.setTextFormat(Qt.AutoText)
            self.notificationDetail.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
            self.notificationDetail.setWordWrap(True)
            self.notificationDetail.setMargin(10)
            self.notificationDetail.setIndent(0)
            self.notificationDetail.setText("Notification")
            self.verticalLayout_4.addWidget(self.notificationDetail)
            
            
        
    def openHistory(self):
        self.pageWidget.setCurrentIndex(3)
        self.historyTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.historyTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.confirmBtn = QtWidgets.QPushButton("Confirm")
        # decorate the button
        self.confirmBtn.setStyleSheet("background-color: #4CAF50; color: white;")
        self.cancelBtn = QtWidgets.QPushButton("Cancel")
        self.cancelBtn.setStyleSheet("background-color: #f44336; color: white;")
        #add data to the table
        self.historyTable.setRowCount(5)
        self.historyTable.setColumnCount(6)
        self.historyTable.setItem(0, 0, QtWidgets.QTableWidgetItem("1"))
        self.historyTable.setItem(0, 1, QtWidgets.QTableWidgetItem("Course 1"))
        self.historyTable.setItem(0, 2, QtWidgets.QTableWidgetItem(f"{datetime.now()}"))
        self.historyTable.setItem(0, 3, QtWidgets.QTableWidgetItem("Pending"))
        self.historyTable.setCellWidget(0, 4, self.confirmBtn)
        self.confirmBtn.clicked.connect(self.confirmation)
        self.historyTable.setCellWidget(0, 5, self.cancelBtn)
        self.cancelBtn.clicked.connect(self.cancellation)
        self.historyTable.setItem(1, 0, QtWidgets.QTableWidgetItem("2"))
        self.historyTable.setItem(1, 1, QtWidgets.QTableWidgetItem("Course 2"))
        self.historyTable.setItem(1, 2, QtWidgets.QTableWidgetItem(f"{datetime.now()}"))
        self.historyTable.setItem(1, 3, QtWidgets.QTableWidgetItem("Completed"))
        
    def cancellation(self):
        self.historyTable.setItem(0, 3, QtWidgets.QTableWidgetItem("Cancelled"))
        self.cancelBtn.hide()
        self.confirmBtn.hide()
        
    def confirmation(self):
        self.historyTable.setItem(0, 3, QtWidgets.QTableWidgetItem("Confirmed"))
        self.confirmBtn.hide()
        self.cancelBtn.hide()   

    def openFeedback(self):
        self.pageWidget.setCurrentIndex(4)
        self.addFeedback()
        
    def addFeedback(self):
        for i in range(5):
            self.feedbackDetail = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.feedbackDetail.setObjectName(f"feedbackDetail_{i}")
            sizePolicy = QtWidgets.QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.feedbackDetail.sizePolicy().hasHeightForWidth())
            self.feedbackDetail.setSizePolicy(sizePolicy)
            self.feedbackDetail.setMinimumSize(QSize(460, 200))
            self.feedbackDetail.setMaximumSize(QSize(460, 200))
            self.feedbackDetail.setLayoutDirection(Qt.LeftToRight)
            self.feedbackDetail.setStyleSheet(u"color: rgb(0, 0, 0);\n"
    "font: 16pt \"Arial\";\n"
    "border: 1 solid black;\n"
    "border-radius: 8px")
            self.feedbackDetail.setFrameShape(QFrame.NoFrame)
            self.feedbackDetail.setFrameShadow(QFrame.Sunken)
            self.feedbackDetail.setTextFormat(Qt.AutoText)
            self.feedbackDetail.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
            self.feedbackDetail.setWordWrap(True)
            self.feedbackDetail.setMargin(10)
            self.feedbackDetail.setIndent(0)
            
            self.feedbackDetail.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
            
            self.verticalLayout_3.addWidget(self.feedbackDetail)
        
    
    def logout(self):
        self.loginPage = LoginPage()
        self.loginPage.show()
        self.hide()
        
    def openCoursePage(self):
        self.coursePage = CoursePage()
        self.coursePage.show()
        self.hide()
        
    def openReservationPage(self):
        self.reservationPage = ReservationPage()
        self.reservationPage.show()
        self.hide()
        
    def openNewsPage(self):
        self.newsPage = NewsPage()
        self.newsPage.show()
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

class ReservationPage(QMainWindow, reservationPage):
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
        
        #reservation page buttons
        self.calendar = self.findChild(QtWidgets.QCalendarWidget, "calendarWidget")
        self.selectedDate = self.findChild(QtWidgets.QLabel, "timeSelectedLabel")
        self.calendar.selectionChanged.connect(self.getDate)
        
        self.reservationName = self.findChild(QtWidgets.QLineEdit, "reservationoName")
        
        self.course = self.findChild(QtWidgets.QComboBox, "courseBox")
        self.course.addItems(["Lunch", "Dinner"])
        self.time = self.findChild(QtWidgets.QComboBox, "timeBox")
        self.time.addItems(["08:00-10:00", "10:00-12:00", "13:00-15:00", "15:00-17:00", "17:00-19:00", "19:00-21:00"])
        self.size = self.findChild(QtWidgets.QComboBox, "partySizeBox")
        self.size.addItems(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
        self.additionNote = self.findChild(QtWidgets.QTextEdit, "noteTextEdit")
        
        self.confirmBtn.clicked.connect(self.confirmReservation)
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
        
    def getDate(self):
        self.date = self.calendar.selectedDate()
        self.selectedDate.setText(self.date.toString("dd/MM/yyyy"))
        
    def confirmReservation(self):
        alert =QtWidgets.QMessageBox()
        alert.setText("Confirm reservation?")
        alert.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        alert.setDefaultButton(QtWidgets.QMessageBox.Yes)
        ret = alert.exec()
        if ret == QtWidgets.QMessageBox.Yes:
            print(f"Reservation confirmed! This Client: {userID} \n{self.date.toString('dd/MM/yyyy')}, {self.reservationName.text()}, {self.course.currentText()}, {self.time.currentText()}, {self.size.currentText()}, {self.additionNote.toPlainText() if self.additionNote.toPlainText() else 'No additional note'}")
            alert =QtWidgets.QMessageBox()
            alert.setText("Reservation confirmed!")
            alert.exec()
            self.mainPage.show()
            self.mainPage.openHomePage()
            self.hide()
        else:
            pass
    
class RegisterMembershipPage(QMainWindow, registerMembershipPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mainPage = MainPage()
        
        self.birthCalendar = self.findChild(QtWidgets.QCalendarWidget, "birthCalendar")
        self.userSelect = self.findChild(QtWidgets.QLabel, "userBirthDate")
        self.birthCalendar.selectionChanged.connect(self.getBirthDate)
        
        self.homeBtn.clicked.connect(self.openHomePage)
        self.userinfoBtn.clicked.connect(self.openUserInfo)
        self.notiBtn.clicked.connect(self.openNotification)
        self.historyBtn.clicked.connect(self.openHistory)
        self.feedbackBtn.clicked.connect(self.openFeedback)
        self.logoutBtn.clicked.connect(self.mainPage.logout)
        
        self.confirmBtn.clicked.connect(self.register)
    
    def getBirthDate(self):
        self.birthDate = self.birthCalendar.selectedDate()
        self.userSelect.setText(self.birthDate.toString("dd/MM/yyyy"))
        
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
        
    def register(self):
        self.checkUserInput()
    
    
    def checkUserInput(self):
        if self.userName.text() and self.userSurname.text() and self.userBirthDate.text() != "xx/xx/xxxx":
            alert =QtWidgets.QMessageBox()
            alert.setText("Membership registered!")
            alert.exec()
            self.mainPage.show()
            self.mainPage.openUserInfo()
            self.hide()
        else:
            alert =QtWidgets.QMessageBox()
            alert.setText("Please fill in all information")
            alert.exec()
        
        
class NewsPage(QMainWindow, newsPage):
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
        
        # News page
        self.addNews()
        
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
        
    def addNews(self):
        pass
    
    
    
#-----------------Admin Page-----------------
class AdminMainPage(QMainWindow, adminMainPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.title = self.findChild(QtWidgets.QLabel, "label")
        adminUser = userServices.getAdminInfo(userID)
        self.title.setText(f"Welcome Back, {adminUser.getUsername()}")
        
        # self.reservationListBtn.clicked.connect(self.openReservationList)
        # self.menuAdjustmentBtn.clicked.connect(self.openCourseList)
        # self.feedbacksBtn.clicked.connect(self.openFeedbackList)
        # self.createNewsBtn.clicked.connect(self.openNewsList)
        
        self.logoutBtn.clicked.connect(self.logout)
        
    def logout(self):
        self.loginPage = LoginPage()
        self.loginPage.show()
        self.hide()