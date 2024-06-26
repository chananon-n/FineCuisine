import random
import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QFileDialog, QVBoxLayout, QFormLayout, QSizePolicy, QDialog, QListWidgetItem, QLabel, QPushButton, QHBoxLayout, QComboBox, QWidget, QSpinBox, QLineEdit
from PySide6.QtGui import QImage, QPixmap
from app.controller.userServices import *
import transaction

from app.gui.login.loginPage import Ui_MainWindow as loginPage
from app.gui.register.registerPage import Ui_MainWindow as registerPage
from app.gui.mainPage.mainPage import Ui_MainWindow as mainPage
from app.gui.course.coursePage import Ui_MainWindow as coursePage
from app.gui.reservation.reservationPage import Ui_MainWindow as reservationPage
from app.gui.registerMembership.registerMembershipPage import Ui_MainWindow as registerMembershipPage
from app.gui.news.newsPage import Ui_MainWindow as newsPage
from app.gui.news.newsDetail import Ui_MainWindow as newsDetail

from app.gui.adminMainPage.adminMainPage import Ui_MainWindow as adminMainPage
from app.gui.courseAdminPage.courseAdminPage import Ui_MainWindow as courseAdminPage
from app.gui.newsAdmin.newsAdminPage import Ui_MainWindow as newsAdminPage
from app.gui.reservationAdminPage.reservationAdminPage import Ui_MainWindow as reservationAdminPage
from app.gui.adminFeedback.adminFeedbackPage import Ui_MainWindow as adminFeedbackPage
from app.gui.paymentPage.paymentPage import Ui_Dialog as paymentPage

from datetime import datetime
import webbrowser

class LoginPage(QMainWindow, loginPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.signinBtn.clicked.connect(self.openRegisterPage)
        self.loginBtn.clicked.connect(self.loginBTN)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        
    def openRegisterPage(self):
        self.registerPage = RegisterPage()
        self.registerPage.setWindowTitle("FineCusine - Register Page")
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
            self.adminMainPage.setWindowTitle("FineCusine - Admin Page")
            self.adminMainPage.show()
            self.hide()
            pass
        elif userRole == "client":
            userID = userServices.getClientID(self.usernameInput.text())
            userRole = "client"
            print(userID)
            self.mainPage = MainPage()
            self.mainPage.setWindowTitle("FineCusine - Main Page")
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
        self.loginPage.setWindowTitle("FineCusine - Login Page")
        self.loginPage.show()
        self.hide()
    
    def register(self):
        global userServices
        userServices = UserServices()
        if self.usernameInput.text() and self.passwordInput.text() and self.emailInput.text() and self.phoneInput.text():
            status = userServices.register(self.usernameInput.text(), self.passwordInput.text(), self.emailInput.text(), self.phoneInput.text())
            if status:
                alert = QtWidgets.QMessageBox()
                alert.setText("Registration successful!")
                alert.exec()
                self.loginPage = LoginPage()
                self.loginPage.setWindowTitle("FineCusine - Login Page")
                self.loginPage.show()
                self.hide()
            else:
                alert =QtWidgets.QMessageBox()
                alert.setText("Username or email already exists")
                alert.exec()
        else:
            alert =QtWidgets.QMessageBox()
            alert.setText("Please fill in all information")
            alert.exec()
      
class MainPage(QMainWindow, mainPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pageWidget.setCurrentIndex(0)
        
        userServices.birthdayNoti(userID)
        
        #sidebar buttons
        self.findaverageFeedbackRating()
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
        
    def findaverageFeedbackRating(self):
        if userServices.getAllFeedbacks() == []:
            self.label_2.setText("No rating yet")
        else:
            feedbacks = userServices.getAllFeedbacks()
            totalRating = 0
            for feedback in feedbacks:
                totalRating += feedback['rating']
                print(feedback['rating'])
                result = totalRating/len(feedbacks)
                self.label_2.setText(f"Rating: {result:.1f}/5")
        
    def openHomePage(self):
        self.pageWidget.setCurrentIndex(0)
        self.findaverageFeedbackRating()
        
    def openUserInfo(self):
        self.pageWidget.setCurrentIndex(1)

        self.userID.setText(userID)
        
        self.userName.setText(userServices.getClientInfo(userID).getUsername())
        self.userEmail.setText(userServices.getClientInfo(userID).getEmail())
        self.userTel.setText(userServices.getClientInfo(userID).getTel())
        
        if userServices.getClientInfo(userID).getMembership() == None:
            self.userFirst.hide()
            self.userSurLabel.hide()
            self.birthDateLabel.hide()
            self.dateExpireLabel.hide()
            self.userFirst.hide()
            self.userSur.hide()
            self.userBirth.hide()
            self.userExpire.hide()
            self.registerMembershipBtn.clicked.connect(self.openRegisterMemberPage)
        else:
            self.userFirst.setText(userServices.getClientInfo(userID).getFname())
            self.userSur.setText(userServices.getClientInfo(userID).getLname())
            self.userBirth.setText(userServices.getClientInfo(userID).getDob())
            self.userExpire.setText(userServices.getClientInfo(userID).getExpireDate())
            self.registerMembershipBtn.hide()
        
    def openRegisterMemberPage(self):
        self.registerMembershipPage = RegisterMembershipPage()
        self.registerMembershipPage.show()
        self.hide()
        
    def openNotification(self):
        self.pageWidget.setCurrentIndex(2)
        self.generateNotification()
    
    def generateNotification(self):
        self.notiWidget.clear()
        userNoti = userServices.getNotifications(userID)
        print(userNoti)
        for noti in userNoti:
            self.notiWidget.insertItem(0, noti)
            self.notiWidget.item(0).setFont(QtGui.QFont("KoHo", 14))
            self.notiWidget.item(0).setForeground(QtGui.QColor(0, 0, 0))
            #can be selected
            self.notiWidget.item(0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        
    def openHistory(self):
        self.pageWidget.setCurrentIndex(3)
        self.historyTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        data = userServices.userHistory(userID)
        #decreasing order of id
        data = sorted(data, key=lambda x: x['bookingID'], reverse=True)
        self.historyTable.setRowCount(len(data))
        #no edit
        self.historyTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.sizeList = [] 
        
        def update_row_status(sender, row, status):
                if  sender is self.cancelBtn:
                    bookingID = int(self.historyTable.item(row, 0).text())
                    meal = self.historyTable.item(row, 1).text()
                    date = self.historyTable.item(row, 2).text()
                    time = self.historyTable.item(row, 3).text()
                    size = self.sizeList[row]
                    userServices.cancelBooking(meal, date, time, size)
                    userServices.confirmBookingStatus(bookingID, status)
                    self.historyTable.setItem(row, 4, QtWidgets.QTableWidgetItem(status))
                    self.historyTable.cellWidget(row, 5).hide()
                    
        for i in range(len(data)):
            self.historyTable.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data[i]['bookingID'])))
            self.historyTable.setItem(i, 1, QtWidgets.QTableWidgetItem(str(data[i]['course'])))
            self.historyTable.setItem(i, 2, QtWidgets.QTableWidgetItem(str(data[i]['date'])))
            self.historyTable.setItem(i, 3, QtWidgets.QTableWidgetItem(str(data[i]['time'])))
            self.historyTable.setItem(i, 4, QtWidgets.QTableWidgetItem(str(data[i]['status'])))
            self.sizeList.append(int(data[i]['partySize']))
            if data[i]['status'] == "pending":
                # Create cancel button
                self.cancelBtn = QtWidgets.QPushButton("Cancel")
                self.cancelBtn.setStyleSheet("background-color: #f44336; color: white;")
                self.cancelBtn.clicked.connect(lambda row=i, status="cancelled": update_row_status(self.cancelBtn, row, status))  # Pass row, status, and sender (self.cancelBtn)
                self.historyTable.setCellWidget(i, 5, self.cancelBtn)
         
    def openFeedback(self):
        self.pageWidget.setCurrentIndex(4)
        self.feedbackSubmitBtn.clicked.connect(self.submitFeedback)
        self.addFeedback()
        
    def addFeedback(self):
        #unchecked all radio buttons
        self.feedbackListWidget.clear()
        allFeedbacks = userServices.getAllFeedbacks()
        for feedbackItem in allFeedbacks:
            feedback_text = f"Rating: {feedbackItem['rating']}/5"
            if feedbackItem['title'] != "": 
                feedback_text += f"\n{feedbackItem['title']}"
            if feedbackItem['detail'] != "":
                feedback_text += f"\n{feedbackItem['detail']}"
            
            self.feedbackListWidget.insertItem(0, feedback_text)
            #set font size
            self.feedbackListWidget.item(0).setFont(QtGui.QFont("KoHo", 14))
            #set font color
            self.feedbackListWidget.item(0).setForeground(QtGui.QColor(0, 0, 0))
            
    def submitFeedback(self):
        rating = None
        for i in range(6): 
            button = self.findChild(QtWidgets.QRadioButton, f"star{i}Radio")
            if button.isChecked():
                rating = i
                break 
            
        if rating == None:
            alert = QtWidgets.QMessageBox()
            alert.setText("Please rate the service")
            alert.exec()
            return
        
        title = self.feedbackTitle.text()
        detail = self.feedbackTextBox.toPlainText()
        userServices.createNewFeedback(title,detail, rating, userID) 
        self.resetFeedback()
        self.addFeedback()
        
    
    def resetFeedback(self):
        for i in range(6):
            button = self.findChild(QtWidgets.QRadioButton, f"star{i}Radio")
            button.setAutoExclusive(False)
            button.setChecked(False)
            button.setAutoExclusive(True)

        self.feedbackTitle.clear()
        self.feedbackTextBox.clear() 
        self.feedbackTitle.clearFocus()
        self.feedbackTextBox.clearFocus()
        
    
    def logout(self):
        self.loginPage = LoginPage()
        self.loginPage.show()
        self.hide()
        
    def openCoursePage(self):
        self.coursePage = CoursePage()
        self.coursePage.setWindowTitle("FineCusine - Course Page")
        self.coursePage.show()
        self.hide()
        
    def openReservationPage(self):
        self.reservationPage = ReservationPage()
        self.reservationPage.setWindowTitle("FineCusine - Reservation Page")
        self.reservationPage.show()
        self.hide()
        
    def openNewsPage(self):
        self.newsPage = NewsPage()
        self.newsPage.setWindowTitle("FineCusine - News Page")
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
        
        # Course page
        self.lunchMenuBtn.clicked.connect(self.openLunchMenuLink)
        self.dinnerMenuBtn.clicked.connect(self.openDinnerMenuLink)
        
        self.logoutBtn.clicked.connect(self.logout)
        
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
        
    def logout(self):
        self.loginPage = LoginPage()
        self.loginPage.show()
        self.hide()
        
    def openLunchMenuLink(self):
        url = userServices.getCourseMenu("Lunch")
        if not url:
            alert =QtWidgets.QMessageBox()
            alert.setText("Lunch menu is not available yet")
            alert.exec()
        webbrowser.open(url)
        
    def openDinnerMenuLink(self):
        url = userServices.getCourseMenu("Dinner")
        webbrowser.open(url)


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
        
        self.logoutBtn.clicked.connect(self.logout)
        
        self.selectedTime = False
        self.selectSize = False
        
        # Sidebar buttons
        self.homeBtn.clicked.connect(self.openHomePage)
        self.userinfoBtn.clicked.connect(self.openUserInfo)
        #reservation page buttons
        self.calendar = self.findChild(QtWidgets.QCalendarWidget, "calendarWidget")
        self.timeSelectedLabel.setText(QtCore.QDate.currentDate().toString("dd/MM/yyyy"))
        self.selectedDate = self.findChild(QtWidgets.QLabel, "timeSelectedLabel")
        self.calendar.setMinimumDate(QtCore.QDate.currentDate())
        self.date = QtCore.QDate.currentDate()
        self.calendar.selectionChanged.connect(self.getDate)
        
        self.reservationName = self.findChild(QtWidgets.QLineEdit, "reservationoName")
        
        self.course = self.findChild(QtWidgets.QComboBox, "courseBox")
        self.course.addItems(["Lunch", "Dinner"])
        self.course.currentIndexChanged.connect(self.updateReservation)

        self.time = self.findChild(QtWidgets.QComboBox, "timeBox")
        self.time.currentIndexChanged.connect(self.updatePartySize)

        self.size = self.findChild(QtWidgets.QComboBox, "partySizeBox")
        self.additionNote = self.findChild(QtWidgets.QTextEdit, "noteTextEdit")
                    
        self.confirmBtn.clicked.connect(self.confirmReservation)  
          
    def updateReservation(self):
        if self.courseBox.currentText() == "Lunch":
            self.time.clear()
            self.time.addItems(self.updateTimeComboBox("Lunch", self.selectedDate.text()))
        elif self.courseBox.currentText() == "Dinner":
            self.time.clear()
            self.time.addItems(self.updateTimeComboBox("Dinner", self.selectedDate.text()))
        else:
            return
        
    def updateTimeComboBox(self, mealType, selectedDate):
        timeList = userServices.getallMealsBooking(mealType)
        print(timeList)
        availableTime = []
        for time in timeList:
            if time['T_Date'] == selectedDate:
                availableTime.append(time['T_Time'])
        return availableTime
    
    def updatePartySize(self):
        # Ensure this method is connected to the signal for when the time selection changes
        selectedDate = self.selectedDate.text()  # Again, ensure this updates correctly
        selectedTime = self.time.currentText()
        selectedCourse = self.course.currentText()
        self.updateSizeComboBox(selectedCourse, selectedDate, selectedTime)

    
    def updateSizeComboBox(self, mealType, selectedDate, selectedTime):
        print(selectedDate)
        print(selectedTime)
        partySize = userServices.getallMealsBooking(mealType)
        print(partySize)
        availableSize = []
        for size in partySize:
            if size['T_Date'] == selectedDate and size['T_Time'] == selectedTime:
                for i in range(size['T_Size']):
                    availableSize.append(str(i+1))
        self.size.clear()
        self.size.addItems(availableSize)
        
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
    
    def paymentPage(self, course, date, time, partySize, persons, userNotes):
        self.paymentPage = PaymentPage(course, date, time, partySize, persons, userNotes)
        self.paymentPage.show()
        self.hide()
        
    def logout(self):
        self.loginPage = LoginPage()
        self.loginPage.show()
        self.hide()
        
    def getDate(self):
        print( self.calendar.selectedDate())
        self.date = self.calendar.selectedDate()
        self.selectedDate.setText(self.date.toString("dd/MM/yyyy"))
        self.updateReservation()
        

    def userMembership(self):
        print("working")
        if userServices.checkUserMembership(userID) != False:
            if userServices.checkUserBirthday(userID) == True:
                # pop up discount - 10% and random code for discount
                discountCode = random.randint(0000, 9999)
                alert = QtWidgets.QMessageBox()
                alert.setText(f"Happy Birthday! You have a 10% discount on your reservation. Your discount code is DIS{discountCode}")
                alert.exec()
            else:
                #pop up discount - 5% and random code for discount
                discountCode = random.randint(0000, 9999)
                alert = QtWidgets.QMessageBox()
                alert.setText(f"You have a 5% discount on your reservation. Your discount code is DIS{discountCode}")
                alert.exec()
            
                

    def confirmReservation(self):
        print("not working")
        alert = QtWidgets.QMessageBox()
        alert.setText("Confirm reservation?")
        alert.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        alert.setDefaultButton(QtWidgets.QMessageBox.Yes)
        ret = alert.exec()
        if ret == QtWidgets.QMessageBox.Yes:
            self.userMembership()
            course = self.course.currentText()
            time = self.time.currentText()
            date = self.date.toString("dd/MM/yyyy")
            partySize = int(self.size.currentText())
            persons = self.reservationName.text()
            userNotes = self.additionNote.toPlainText()
            self.paymentPage(course, date, time, partySize, persons, userNotes)
            
class PaymentPage(QMainWindow, paymentPage):
    def __init__(self,course, date, time, partySize, persons, userNotes):
        super().__init__()
        self.setupUi(self)
        self.mainPage = MainPage()
        self.course = course
        self.date = date
        self.time = time
        self.partySize = partySize
        self.persons = persons
        self.userNotes = userNotes
        
        self.cancelBtn.clicked.connect(self.openReservationPage)
        self.cancelBtn_2.clicked.connect(self.paidPage)
    
    def openReservationPage(self):
        self.mainPage = MainPage()
        self.mainPage.show()
        self.hide()
    
    def paidPage(self):
        if userServices.reservation(userID, self.course, self.date, self.time, self.partySize, self.persons, self.userNotes):
            alert = QtWidgets.QMessageBox()
            alert.setText("Reservation successful!")
            alert.exec()
        else:
            alert = QtWidgets.QMessageBox()
            alert.setText("Reservation failed. Please try again.")
            alert.exec()
        
        self.mainPage = MainPage()
        self.mainPage.show()
        self.hide()

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
            userServices.registerMembership(userID, self.userName.text(), self.userSurname.text(), self.userBirthDate.text())
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
        
        self.mapIDandTitle = []
        
        # Sidebar buttons
        self.homeBtn.clicked.connect(self.openHomePage)
        self.userinfoBtn.clicked.connect(self.openUserInfo)
        self.notiBtn.clicked.connect(self.openNotification)
        self.historyBtn.clicked.connect(self.openHistory)
        self.feedbackBtn.clicked.connect(self.openFeedback)
        
        self.logoutBtn.clicked.connect(self.logout)
        
        # News page
        self.listWidget.itemClicked.connect(self.openNews)
        self.updateNews()
        
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
        
    def logout(self):
        self.loginPage = LoginPage()
        self.loginPage.show()
        self.hide()
        
    def openNews(self, item):
        newsID = item.data(QtCore.Qt.UserRole)
        news = userServices.getNewInfo(newsID).toJson()
        self.newsDetail = NewsDetail(news)
        self.newsDetail.show()  
    
    def updateNews(self):
        self.listWidget.clear()
        newsList = userServices.getAllNews()
        for newsItem in newsList:
            news = QListWidgetItem(newsItem['title'])
            news.setData(QtCore.Qt.UserRole, newsItem['id'])
            self.listWidget.insertItem(0, news)
    
class NewsDetail(QMainWindow, newsDetail):
    def __init__(self, news):
        super().__init__()
        self.setupUi(self)
        
        self.mainPage = MainPage()
        
        self.newsTitle.setText(news["title"])
        pixmap = self.convert_to_qpixmap(news["image"])
        if pixmap.width() > pixmap.height():
            aspect_ratio = pixmap.height() / pixmap.width()
            label_width = 841
            label_height = int(label_width * aspect_ratio)
            self.neswImage.setFixedSize(label_width, label_height)
        else:
            aspect_ratio = pixmap.width() / pixmap.height()
            label_height = 1100
            label_width = int(label_height * aspect_ratio)
            self.neswImage.setFixedSize(label_width, label_height)
        self.neswImage.setPixmap(QtGui.QPixmap(pixmap))
        self.newsDetail.setText(news["details"])
        self.newsDate.setText(news["datePost"])
        
    def convert_to_qpixmap(self, image_data):
        # Convert image data to QImage
        image = QImage.fromData(image_data)
        # Convert QImage to QPixmap
        pixmap = QPixmap.fromImage(image)
        return pixmap

#-----------------Admin Page-----------------
class AdminMainPage(QMainWindow, adminMainPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.title = self.findChild(QtWidgets.QLabel, "label")
        adminUser = userServices.getAdminInfo(userID)
        self.title.setText(f"Welcome Back, {adminUser.getUsername()}")
        
        self.reservationListBtn.clicked.connect(self.openReservationList)
        self.menuAdjustmentBtn.clicked.connect(self.openMenuAdjustPage)
        self.feedbacksBtn.clicked.connect(self.openFeedbackList)
        self.createNewsBtn.clicked.connect(self.openCreateNews)
        
        self.logoutBtn.clicked.connect(self.logout)
        
    def openFeedbackList(self):
        self.adminFeedbackPage = AdminFeedbackPage()
        self.adminFeedbackPage.show()
        self.hide()
    
    def openMenuAdjustPage(self):
        self.menuAdjustPage = MenuAdjustPage()
        self.menuAdjustPage.show()
        self.hide()
        
    def openCreateNews(self):
        self.newsAdminPage = NewsAdminPage()
        self.newsAdminPage.show()
        self.hide()
        
    def openReservationList(self):
        self.reservationAdminPage = ReservationAdminPage()
        self.reservationAdminPage.show()
        self.hide()
    
    def logout(self):
        self.loginPage = LoginPage()
        self.loginPage.show()
        self.hide()
        
class MenuAdjustPage(QMainWindow, courseAdminPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.courseComboBox.addItems(["Lunch", "Dinner"])
        self.submitBtn.clicked.connect(self.submit)
        
        self.logoutBtn.clicked.connect(self.backtoAdminMain)
        

    def submit(self):
        if self.courseComboBox.currentText() and self.linkInput.text():
            alert =QtWidgets.QMessageBox()
            alert.setText("Confirm adjustment?")
            alert.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            alert.setDefaultButton(QtWidgets.QMessageBox.Yes)
            ret = alert.exec()
            if ret == QtWidgets.QMessageBox.Yes:
                print(f"Menu adjusted! {self.courseComboBox.currentText()}, {self.linkInput.text()}")
                userServices.addCourseMenu(self.courseComboBox.currentText(), self.linkInput.text())
                alert =QtWidgets.QMessageBox()
                alert.setText("Menu adjusted!")
                alert.exec()
                self.adminMainPage = AdminMainPage()
                self.adminMainPage.show()
                self.hide()
            else:
                pass
        else:
            alert =QtWidgets.QMessageBox()
            alert.setText("Please fill in all information")
            alert.exec()

    def backtoAdminMain(self):
        self.adminMainPage = AdminMainPage()
        self.adminMainPage.show()
        self.hide()

class NewsAdminPage(QMainWindow, newsAdminPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.browseBtn.clicked.connect(self.browse)
        self.selected = False
        
        self.submitBtn.clicked.connect(self.submit)
        
        self.backBtn.clicked.connect(self.backtoAdminMain)
        
    def browse(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.png)")
        self.fileLabel.setText(fname[0])
        self.selected = True
        
    def submit(self):
        if self.selected and self.titleInput.text() and self.desTextBox.toPlainText():
            alert =QtWidgets.QMessageBox()
            alert.setText("Confirm news?")
            alert.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            alert.setDefaultButton(QtWidgets.QMessageBox.Yes)
            ret = alert.exec()
            if ret == QtWidgets.QMessageBox.Yes:
                with open(self.fileLabel.text(), 'rb') as f:
                    image_data = f.read()
                postDate = datetime.now()
                formatedDate = postDate.strftime("%d/%m/%Y - %H:%M")
                print(f"News created! {self.titleInput.text()}, {self.fileLabel.text()}, {self.desTextBox.toPlainText()}, {formatedDate}")
                userServices.createNews(self.titleInput.text(), image_data, self.desTextBox.toPlainText(), formatedDate)
                alert =QtWidgets.QMessageBox()
                alert.setText("News created!")
                alert.exec()
                self.adminMainPage = AdminMainPage()
                self.adminMainPage.show()
                self.hide()
            else:
                pass
        else:
            alert =QtWidgets.QMessageBox()
            alert.setText("Please fill in all information")
            alert.exec()
        
    def backtoAdminMain(self):
        self.adminMainPage = AdminMainPage()
        self.adminMainPage.show()
        self.hide()
        
class ReservationAdminPage(QMainWindow, reservationAdminPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.reservationTable.setWordWrap(True)
        self.reservationTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        #del all rows
        self.reservationTable.setRowCount(0)
        #no edit
        self.reservationTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        
        self.backBtn.clicked.connect(self.backtoAdminMain)
        self.closeReservationBtn.clicked.connect(self.closedReservation)
        self.createReservationBtn.clicked.connect(self.createReservation)
        self.EditReservation.clicked.connect(self.editReservation)
        self.selectBtn.clicked.connect(self.reservationList)
        
    def editReservation(self):
        self.editWidget = QWidget()
        self.editWidgetLayout = QVBoxLayout(self.editWidget)

        # Create a combobox for selecting close reason
        self.mealCombo = QComboBox()
        self.mealCombo.addItem("Select Meal")
        self.mealCombo.addItem("Lunch")
        self.mealCombo.addItem("Dinner")
        self.mealComboLayout = QHBoxLayout()
        self.mealComboLayout.addWidget(QLabel("Meal Type: "))
        self.mealComboLayout.addWidget(self.mealCombo)
        self.editWidgetLayout.addLayout(self.mealComboLayout)
        
        self.mealCombo.currentTextChanged.connect(self.updateDateCombo)
        

        self.dateCombo = QComboBox()
        userSelectedMeal = self.mealCombo.currentText()
        if userSelectedMeal == "Select Meal":
            self.dateCombo.addItem("Select Date")
        self.dateComboLayout = QHBoxLayout()
        self.dateComboLayout.addWidget(QLabel("Date: "))
        self.dateComboLayout.addWidget(self.dateCombo)
        self.editWidgetLayout.addLayout(self.dateComboLayout)
        
        self.dateCombo.currentTextChanged.connect(self.updateTimeCombo)
    

        self.timeCombo = QComboBox()
        userSelectedDate = self.dateCombo.currentText()
        if userSelectedDate == "Select Date":
            self.timeCombo.addItem("Select Time")
        self.timeComboLayout = QHBoxLayout()
        self.timeComboLayout.addWidget(QLabel("Time: "))
        self.timeComboLayout.addWidget(self.timeCombo)
        self.editWidgetLayout.addLayout(self.timeComboLayout)
        
        self.partySize = QSpinBox()
        self.partySize.setMinimum(1)
        self.partySize.setMaximum(10)
        self.partySizeLayout = QHBoxLayout()
        self.partySizeLayout.addWidget(QLabel("Party Size: "))
        self.partySizeLayout.addWidget(self.partySize)
        self.editWidgetLayout.addLayout(self.partySizeLayout)
        

        # Create a button to confirm closing the reservation
        self.confirmEditBtn = QPushButton("Confirm Edit")
        # self.confirmCloseBtn.clicked.connect(self.confirmCloseReservation)
        self.editWidgetLayout.addWidget(self.confirmEditBtn)
        
        self.confirmEditBtn.clicked.connect(self.confirmEditReservation)
        
        self.editWidget.show()
        
    def confirmEditReservation(self):
        meal = self.mealCombo.currentText()
        date = self.dateCombo.currentText()
        time = self.timeCombo.currentText()
        size =int(self.partySize.text())
        if meal == "Select Meal" or date == "" or time == "":
            alert = QtWidgets.QMessageBox()
            alert.setText("Please select meal, date, and time")
            alert.exec()
        else:
            check  = userServices.editMealReservation(meal,date,time,size)
            if check:
                alert = QtWidgets.QMessageBox()
                alert.setText("Reservation edited!")
                alert.exec()
                self.editWidget.hide()
                self.reservationList()
            else:
                alert = QtWidgets.QMessageBox()
                alert.setText("Reservation Invalid!")
                alert.exec()
    
    def reservationList(self):
        data = self.dateEdit.text().strip()
        bookings = userServices.getAllBookingsByDate(data)
        #sort by time
        bookings = sorted(bookings, key=lambda x: x['time'])
        self.reservationTable.setRowCount(len(
            bookings))

        def update_row_status(sender, row, status):
                if sender is self.confirmBtn or sender is self.cancelBtn:
                    bookingID = self.reservationTable.item(row, 0).text()
                    bookingID = int(bookingID)
                    if status == "cancelled":
                        meal = self.reservationTable.item(row, 2).text()
                        date = self.dateEdit.text().strip()
                        time = self.reservationTable.item(row, 3).text()
                        size = int(self.reservationTable.item(row, 4).text())
                        userServices.cancelBooking(meal, date, time, size)
                    else:
                        userServices.confirmBookingStatus(bookingID, status)
                    self.reservationTable.setItem(row, 7, QtWidgets.QTableWidgetItem(status))
                    self.reservationTable.cellWidget(row, 8).hide()
                    self.reservationTable.cellWidget(row, 9).hide()

        # Loop through bookings and populate table
        for i in range(len(bookings)):
            self.reservationTable.setItem(i, 3, QtWidgets.QTableWidgetItem(str(bookings[i]['time'])))
            self.reservationTable.setItem(i, 0, QtWidgets.QTableWidgetItem(str(bookings[i]['bookingID'])))
            self.reservationTable.setItem(i, 1, QtWidgets.QTableWidgetItem(str(bookings[i]['persons'])))
            self.reservationTable.setItem(i, 2, QtWidgets.QTableWidgetItem(str(bookings[i]['course'])))
            self.reservationTable.setItem(i, 4, QtWidgets.QTableWidgetItem(str(bookings[i]['partySize'])))
        
            userID = bookings[i]['clientID']
            checkMembership = userServices.checkUserMembership(userID)
            if checkMembership:
                self.reservationTable.setItem(i, 5, QtWidgets.QTableWidgetItem("Yes"))
            else:
                self.reservationTable.setItem(i, 5, QtWidgets.QTableWidgetItem("No"))
            self.reservationTable.setItem(i, 6, QtWidgets.QTableWidgetItem(str(bookings[i]['userNotes'])))
            self.reservationTable.setItem(i, 7, QtWidgets.QTableWidgetItem(str(bookings[i]['status'])))
            

            if bookings[i]['status'] == "pending":            
                self.confirmBtn = QtWidgets.QPushButton("Confirm")
                self.confirmBtn.setStyleSheet("background-color: #4CAF50; color: white;")
                self.confirmBtn.clicked.connect(lambda row=i, status="confirmed": update_row_status(self.confirmBtn, row, status))  # Pass row, status, and sender (self.confirmBtn)
                self.reservationTable.setCellWidget(i, 8, self.confirmBtn)

                # Create cancel button
                self.cancelBtn = QtWidgets.QPushButton("Cancel")
                self.cancelBtn.setStyleSheet("background-color: #f44336; color: white;")
                self.cancelBtn.clicked.connect(lambda row=i, status="cancelled": update_row_status(self.cancelBtn, row, status))  # Pass row, status, and sender (self.cancelBtn)
                self.reservationTable.setCellWidget(i, 9, self.cancelBtn)
     
    def createReservation(self):
        self.createReservationWidget = QWidget()
        self.createReservationWidgetLayout = QVBoxLayout(self.createReservationWidget)
        
        self.meal = QComboBox()
        self.meal.addItem("Select Meal")
        self.meal.addItem("Lunch")
        self.meal.addItem("Dinner")
        self.mealLayout = QHBoxLayout()
        self.mealLayout.addWidget(QLabel("Meal Type: "))
        self.mealLayout.addWidget(self.meal)
        self.createReservationWidgetLayout.addLayout(self.mealLayout)
        
        self.timeCombo = QLineEdit()
        self.timeLayout = QHBoxLayout()
        self.timeLayout.addWidget(QLabel("Time: "))
        self.timeLayout.addWidget(self.timeCombo)
        self.createReservationWidgetLayout.addLayout(self.timeLayout)
        
        self.size = QSpinBox()
        self.size.setMinimum(1)
        self.size.setMaximum(10)
        self.sizeLayout = QHBoxLayout()
        self.sizeLayout.addWidget(QLabel("Party Size: "))
        self.sizeLayout.addWidget(self.size)
        self.createReservationWidgetLayout.addLayout(self.sizeLayout)
        
        #create input number
        self.day = QSpinBox()
        self.day.setMinimum(1)
        self.day.setMaximum(31)
        self.dayLayout = QHBoxLayout()
        self.dayLayout.addWidget(QLabel("Day: "))
        self.dayLayout.addWidget(self.day)
        self.createReservationWidgetLayout.addLayout(self.dayLayout)
        
        #confirm button
        self.confirmCreateBtn = QPushButton("Confirm Create")
        self.createReservationWidgetLayout.addWidget(self.confirmCreateBtn)
        self.confirmCreateBtn.clicked.connect(self.confirmCreateReservation)
        
        self.createReservationWidget.show()
        
              
    def confirmCreateReservation(self):
        meal = self.meal.currentText()
        time = self.timeCombo.text()
        partySize = int(self.size.text())
        day = int(self.day.text())
        if meal == "Select Meal" or time == "" or day == "":
            alert = QtWidgets.QMessageBox()
            alert.setText("Please select meal, time, and day")
            alert.exec()
        else:
            check  = userServices.createMealReservation(meal, time,partySize, day)
            if check:
                alert = QtWidgets.QMessageBox()
                alert.setText("Reservation created!")
                alert.exec()
                self.createReservationWidget.hide()
                self.reservationList()
            else:
                alert = QtWidgets.QMessageBox()
                alert.setText("Reservation already exists!")
                alert.exec()
    
    def closedReservation(self):
        # Create a layout for the user input widget
        self.closeReasonWidget = QWidget()
        self.closeReasonWidgetLayout = QVBoxLayout(self.closeReasonWidget)

        # Create a combobox for selecting close reason
        self.mealCombo = QComboBox()
        self.mealCombo.addItem("Select Meal")
        self.mealCombo.addItem("Lunch")
        self.mealCombo.addItem("Dinner")
        self.mealComboLayout = QHBoxLayout()
        self.mealComboLayout.addWidget(QLabel("Meal Type: "))
        self.mealComboLayout.addWidget(self.mealCombo)
        self.closeReasonWidgetLayout.addLayout(self.mealComboLayout)
        
        self.mealCombo.currentTextChanged.connect(self.updateDateCombo)
        

        self.dateCombo = QComboBox()
        userSelectedMeal = self.mealCombo.currentText()
        if userSelectedMeal == "Select Meal":
            self.dateCombo.addItem("Select Date")
        self.dateComboLayout = QHBoxLayout()
        self.dateComboLayout.addWidget(QLabel("Date: "))
        self.dateComboLayout.addWidget(self.dateCombo)
        self.closeReasonWidgetLayout.addLayout(self.dateComboLayout)
        
        self.dateCombo.currentTextChanged.connect(self.updateTimeCombo)
    

        self.timeCombo = QComboBox()
        userSelectedDate = self.dateCombo.currentText()
        if userSelectedDate == "Select Date":
            self.timeCombo.addItem("Select Time")
        self.timeComboLayout = QHBoxLayout()
        self.timeComboLayout.addWidget(QLabel("Time: "))
        self.timeComboLayout.addWidget(self.timeCombo)
        self.closeReasonWidgetLayout.addLayout(self.timeComboLayout)
        

        # Create a button to confirm closing the reservation
        self.confirmCloseBtn = QPushButton("Confirm Close")
        # self.confirmCloseBtn.clicked.connect(self.confirmCloseReservation)
        self.closeReasonWidgetLayout.addWidget(self.confirmCloseBtn)
        
        self.confirmCloseBtn.clicked.connect(self.confirmCloseReservation)

        # Display the user input widget (consider using a dialog instead)
        self.closeReasonWidget.show()
    
    def confirmCloseReservation(self):
        meal = self.mealCombo.currentText()
        date = self.dateCombo.currentText()
        time = self.timeCombo.currentText()
        if meal == "Select Meal" or date == "Select Date" or time == "Select Time" or date == "" or time == "":
            alert = QtWidgets.QMessageBox()
            alert.setText("Please select meal, date, and time")
            alert.exec()
            return
        else:
            userServices.closedReservation(meal, date, time)
            userServices.changeAllStatusBooking(meal, date, time, "cancelled")
            alert = QtWidgets.QMessageBox()
            alert.setText("Reservation closed!")
            alert.exec()
            self.closeReasonWidget.hide()
            self.reservationList()
    
    def updateDateCombo(self):
        temp = ""
        userSelectedMeal = self.mealCombo.currentText()
        self.dateCombo.clear() 

        if userSelectedMeal == "Select Meal":
            self.dateCombo.addItem("Select Date")
        else:
            # Assuming you have logic to fetch available dates based on meal
            data = userServices.getallMealsBooking(userSelectedMeal)
            for date in data:
                    if date['T_Date'] != temp:
                        self.dateCombo.addItem(date['T_Date'])
                        temp = date['T_Date']
    
    def updateTimeCombo(self):
        userSelectedDate = self.dateCombo.currentText()
        userSelectedMeal = self.mealCombo.currentText()
        self.timeCombo.clear()

        date = QtCore.QDate.currentDate().toString("dd/MM/yyyy")
        if userSelectedDate == "Select Date":
            self.timeCombo.addItem("Select Time")
        else:
            # Assuming you have logic to fetch available times based on meal and date
            data = userServices.getallMealsBooking(userSelectedMeal)
            for time in data:
                if time['T_Date'] == userSelectedDate and time['T_Date'] >= date:
                    self.timeCombo.addItem(time['T_Time'])
                
        
    def backtoAdminMain(self):
        self.adminMainPage = AdminMainPage()
        self.adminMainPage.show()
        self.hide()
    

class AdminFeedbackPage(QMainWindow, adminFeedbackPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clearFocus()
        self.addFeedback()
        self.backBtn.clicked.connect(self.backtoAdminMain)
        self.AllBtn.clicked.connect(self.addFeedback)
        self.OneBtn.clicked.connect(self.ratingOne)
        self.TwoBtn.clicked.connect(self.ratingTwo)
        self.ThreeBtn.clicked.connect(self.ratingThree)
        self.FourBtn.clicked.connect(self.ratingFour)
        self.FiveBtn.clicked.connect(self.ratingFive)
        
    def backtoAdminMain(self):
        self.adminMainPage = AdminMainPage()
        self.adminMainPage.show()
        self.hide()
    
    def cleanFocus(self): 
        self.AllBtn.clearFocus()
        self.OneBtn.clearFocus()
        self.TwoBtn.clearFocus()
        self.ThreeBtn.clearFocus()
        self.FourBtn.clearFocus()
        self.FiveBtn.clearFocus()

    def addFeedback(self):
        self.listWidget.clear()
        allFeedbacks = userServices.getAllFeedbacks()
        for feedbackItem in allFeedbacks:
            feedback_text = f"Rating: {feedbackItem['rating']}/5"
            if feedbackItem['title'] != "": 
                feedback_text += f"\n{feedbackItem['title']}"
            if feedbackItem['detail'] != "":
                feedback_text += f"\n{feedbackItem['detail']}"
            
            self.listWidget.insertItem(0, feedback_text)
            #set font size
            self.listWidget.item(0).setFont(QtGui.QFont("KoHo", 14))
            #set font color
            self.listWidget.item(0).setForeground(QtGui.QColor(0, 0, 0))
    
    def ratingOne(self):
        self.rating(1)
                
    def ratingTwo(self):
        self.rating(2)
                
    def ratingThree(self):
        self.rating(3)
                
    def ratingFour(self):
        self.rating(4)
                
    def ratingFive(self):
        self.rating(5)
            
    
    def rating(self, rating):
        self.listWidget.clear()
        allFeedbacks = userServices.getFeedbacksByRating(rating)
        for feedbackItem in allFeedbacks:
            feedback_text = f"Rating: {feedbackItem['rating']}/5"
            if feedbackItem['title'] != "": 
                feedback_text += f"\n{feedbackItem['title']}"
            if feedbackItem['detail'] != "":
                feedback_text += f"\n{feedbackItem['detail']}"
            
            self.listWidget.insertItem(0, feedback_text)
            #set font size
            self.listWidget.item(0).setFont(QtGui.QFont("KoHo", 14))
            #set font color
            self.listWidget.item(0).setForeground(QtGui.QColor(0, 0, 0))
                

