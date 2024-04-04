import datetime
from app.controller.databaseManager import dataManager


class UserServices:
    def login(self,usernameInput, passwordInput):
        return dataManager.validateUserLogin(usernameInput, passwordInput)
    
    def getClientInfo(self,userId):
        client = dataManager.getClientInfo(userId)
        return client
    
    def getAdminInfo(self,userId):
        admin = dataManager.getAdminInfo(userId)
        return admin
        
    def getClientID(self,username):
        client = dataManager.getClient(username)
        return client.id
    
    def getAdminID(self,username):
        admin = dataManager.getAdmin(username)
        return admin.id
    
    def register(self,username, password, email, phone):
        checkUser = dataManager.checkDuplicateUser(username,email)
        if checkUser:
            role = dataManager.validationUserRegister(email)
            print(role)
            if role == "admin":
                dataManager.registerAdmin(username, password, email, phone)
                return True
            else:
                user = dataManager.registerClient(username, password, email, phone)
                dataManager.addNotification(user.id,"Welcome to the Fine Cuisine!!!")
                return True
        else:
            return False
    
    def reservation(clientID, course, date, time, partySize, persons, userNotes):
        checkAvailable = dataManager.checkBookingAvailable(time, date, partySize, course)
        if checkAvailable:
            dataManager.updateMealBooking(course, date, time, partySize)
            dataManager.addBookingDB(clientID, course, time, date, partySize, persons, userNotes)
            dataManager.addNotification(clientID, "Your booking has been confirmed")
            return True
        else:

            return False
    
    def registerMembership(self, clientID, fname, lname, dateOfBirth):
        dataManager.registerMembership(clientID, fname, lname, dateOfBirth)
        dataManager.addNotification(clientID,"Congratulations, you have successfully registered for membership")
        dataManager.addNotification(clientID,"You have been awarded Birthday Cake on your birthday")
        return True
    
    def getNotifications(self,clientID):
        notifications = dataManager.getUserNotifications(clientID)
        return notifications
    
    def addCourseMenu(self, type, links):
        dataManager.addCourseMenu(type, links)
        return True
    
    def getCourseMenu(self, type):
        courseMenu = dataManager.getCourseMenu(type)
        return courseMenu
    
    def createNews(self, title, image, details, date):
        dataManager.addNews(title, image, details, date)
        return True
    
    def getAllNews(self):  
        data =  dataManager.getNews()
        return data
        
    def getNewInfo(self,id):
        data = dataManager.getNewByID(id)
        return data
    
    def createNewFeedback(self,title,description,rating):
        dataManager.addFeedback(title,description,rating)
        return True
    
    def getAllFeedbacks(self):
        data = dataManager.getFeedbacks()
        return data
    
    def getFeedback(self,id):
        data = dataManager.getFeedbackInfo(id)
        return data
    
    def getFeedbacksByRating(self,rating):
        data = dataManager.getFeedbacks()
        feedbacks = []
        for item in data:
            if item['rating'] == rating:
                feedbacks.append(item)
        return feedbacks
        
    def checkUserMembership(self,clientID):
        check = dataManager.checkMembership(clientID)
        return check

    def checkUserBirthday(self,clientID):
        check = UserServices.checkUserMembership(clientID)
        currentDate = datetime.now()
        currentMonth = currentDate.strftime("%d/%m/%Y").split('/')[1]
        userMonth = check['memberBirth'].split('/')[1]
        if currentMonth == userMonth:
            return True
        return False
        
    def getallMealsBooking(self, type):
        data = dataManager.getAllMealBookings(type)
        return data
    
    def getAllBookingsByDate(self, date):
        data = dataManager.getAllUserBookings()
        bookings = []
        for item in data:
            if item['date'] == date:
                bookings.append(item)
        return bookings
     
     
    def confirmBookingStatus(self,bookingID,status):
        dataManager.changeBookingStatus(bookingID,status)
        return True
    
    def closedReservation(self,mealType,date,time):
        dataManager.deleteMealBooking(mealType,date,time)
        return True
    
    def createMealReservation(self,mealType,time,partySize,numBooking):
        dataManager.createMealBooking(mealType,time,partySize,numBooking)
        return True