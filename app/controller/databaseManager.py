from app.db.database import *
from app.model.booking import Booking
from app.model.user import *
from app.model.courseDetail import CourseMenu
from app.model.news import *
import transaction

from datetime import datetime, timedelta
class dataManager:
    def __init__(self):
        pass
    
    @staticmethod
    def validateUserLogin(username, password):
        return checkUser(username, password)
    
    def getAllClients():
        return getAllClients()
    
    def getAllAdmin():
        return getAllAdmins()
    
    def validationUserRegister(email):
        return assignRole(email)
    
    def getClient(username):
        return getClient(username)
    
    def getAdmin(username):
        return getAdmin(username)
    
    def getClientInfo(clientID):
        return getClientInfo(clientID)
    
    def getAdminInfo(adminID):
        return getAdminInfo(adminID)
    
    def registerAdmin(username, password, email, phone):
        user = Admin(username, password, email, phone)
        root.admins[user.id] = user
        transaction.commit()
        
    def registerClient(username, password, email, phone):
        user = Client(username, password, email, phone)
        root.clients[user.id] = user
        transaction.commit()
        return user
        
    def createMealBooking(mealType, date, time, partySize):
        generateMealBooking(mealType, date, time, partySize)
        return True
    
    def getBooking(bookingID):
        return getBooking(bookingID)
    
    def getAllUserBookings():
        return getAllBookings()
    
    def getAllMealBookings(mealType):
        return getAllMealBookings(mealType)
        
    def getBooking(mealType, date, time):
        return getMealBooking(mealType, date, time)
    
    def clearBookingDB():
        clearMealBookings()
        
    def clearUserBookingDB():
        clearUserBookings()
    
    def addBookingDB(clientID, course, time, date, partySize, persons, userNotes):
        booking = Booking(clientID, course, time, date, partySize, persons, userNotes)
        addUserBooking(booking)
        return True
    
    def getUserBookings(clientID):
        return getUserBookings(clientID)
    
    def updateMealBooking(mealType, date, time, partySize):
        return updateMealBooking(mealType, date, time, partySize)
    
    def changeBookingStatus(bookingID, status):
        return updateBookingStatus(bookingID, status)
   
    def checkBookingAvailable(time, date, partySize, mealType):
        bookInfo = getMealBooking(mealType, date, time)
        if bookInfo['T_LEFT'] >= partySize:
            return True
        else:
            return False     
        
    def registerMembership(clientID, fname, lname, dateOfBirth):
        dateExpired = datetime.now() + timedelta(days=365)
        formatedDate = dateExpired.strftime("%d/%m/%Y")
        data = {
            "memberName": fname,
            "memberSurname": lname,
            "memberBirth": dateOfBirth,
            "dateExpired": formatedDate
        }
        return registerMembership(clientID, data)
    
    def checkMembership(clientID):
        return checkMembership(clientID)
    
    def checkDuplicateUser(username, email):
        clientInfo = getAllClients()
        adminInfo = getAllAdmins()
        for client in clientInfo:
            if username == client['username'] or email == client['email']:
                print("Username or email already exists")
                return False
        for admin in adminInfo:
            if username == admin['username'] or email == admin['email']:
                print("Username or email already exists")
                return False
        return True
    
    def addNotification(clientID,notification):
        return createNotification(clientID,notification)
    
    def getUserNotifications(clientID):
        client = root.clients.get(clientID)
        if client:
            notifications = client.notifications
            return [notification.message for notification in notifications]
        else:
            return []
        
    # Course Menu
    def addCourseMenu(type, links):
        return addCourseMenu(type, links)
    
    def getCourseMenu(courseType):
        return getCourseMenu(courseType)
    
    def addNews(title,image,details,PostDate):
        new = News(title,image,details,PostDate)
        addNews(new)
        return True
    
    def getNews():
        return getAllNews()
    
    def getNewByID(id):
        data = getNewsInformation(id)
        return data


    
        
        