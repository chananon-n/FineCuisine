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
    
    @staticmethod
    def getAllClients():
        return getAllClients()
    
    @staticmethod
    def getAllAdmin():
        return getAllAdmins()
    
    @staticmethod
    def validationUserRegister(email):
        return assignRole(email)
    
    @staticmethod
    def getClient(username):
        return getClient(username)
    
    @staticmethod
    def getAdmin(username):
        return getAdmin(username)
    
    @staticmethod
    def getClientInfo(clientID):
        return getClientInfo(clientID)

    @staticmethod    
    def getAdminInfo(adminID):
        return getAdminInfo(adminID)

    @staticmethod 
    def registerAdmin(username, password, email, phone):
        user = Admin(username, password, email, phone)
        root.admins[user.id] = user
        transaction.commit()

    @staticmethod    
    def registerClient(username, password, email, phone):
        user = Client(username, password, email, phone)
        root.clients[user.id] = user
        transaction.commit()
        return user

    @staticmethod    
    def createMealBooking(mealType, date, time, partySize):
        generateMealBooking(mealType, date, time, partySize)
        return True
    
    @staticmethod
    def getBooking(bookingID):
        return getBooking(bookingID)
    
    @staticmethod
    def getAllUserBookings():
        return getAllBookings()
    
    @staticmethod
    def getAllMealBookings(mealType):
        return getAllMealBookings(mealType)

    @staticmethod    
    def getBooking(mealType, date, time):
        return getMealBooking(mealType, date, time)
    
    @staticmethod
    def clearBookingDB():
        clearMealBookings()
    
    @staticmethod
    def clearUserBookingDB():
        clearUserBookings()
    
    @staticmethod
    def addBookingDB(booking):
        addUserBooking(booking)
        return booking.bookingID
    
    @staticmethod
    def getUserBookings(clientID):
        return getUserBookings(clientID)
    
    @staticmethod
    def updateMealBooking(mealType, date, time, partySize):
        return updateMealBooking(mealType, date, time, partySize)
    
    @staticmethod
    def changeBookingStatus(bookingID, status):
        updateBookingStatus(bookingID, status)
        booking = getBooking(bookingID)
        clientID = booking.clientID
        if status == "Confirmed":
            notificationMessage = f"Your booking for {booking.course} on {booking.date} at {booking.time} has been confirmed."
            dataManager.addNotification(clientID, notificationMessage)
        elif status == "Cancelled":
            notificationMessage = f"Your booking for {booking.course} on {booking.date} at {booking.time} has been cancelled."
            dataManager.addNotification(clientID, notificationMessage)
        return True
   
    @staticmethod
    def checkBookingAvailable(time, date, partySize, mealType):
        bookInfo = getMealBooking(mealType, date, time)
        if bookInfo is not None and bookInfo.get('T_LEFT', 0) >= partySize:
            return True
        else:
            return False  

    @staticmethod    
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
    
    @staticmethod
    def checkMembership(clientID):
        return checkMembership(clientID)
    
    @staticmethod
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
    
    @staticmethod
    def addNotification(clientID,notification):
        return createNotification(clientID,notification)
    
    @staticmethod
    def getUserNotifications(clientID):
        client = root.clients.get(clientID)
        if client:
            notifications = client.notifications
            return [notification.message for notification in notifications]
        else:
            return []
        
    # Course Menu
    @staticmethod
    def addCourseMenu(type, links):
        return addCourseMenu(type, links)
    
    @staticmethod
    def getCourseMenu(courseType):
        return getCourseMenu(courseType)
    
    @staticmethod
    def addNews(title,image,details,PostDate):
        new = News(title,image,details,PostDate)
        addNews(new)
        return True
    
    @staticmethod
    def getNews():
        return getAllNews()
    
    @staticmethod
    def getNewByID(id):
        data = getNewsInformation(id)
        return data


    
        
        