from app.db.database import *
from app.model.booking import Booking
from app.model.feedback import Feedback
from app.model.meal import Dinner, Lunch
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
        return getAllClientsDB()
    
    def getAllAdmin():
        return getAllAdminsDB()
    
    def validationUserRegister(email):
        return assignRole(email)
    
    def getClient(username):
        return getClient(username)
    
    def getAdmin(username):
        return getAdmin(username)
    
    def getClientInfo(clientID):
        return getClientDBInfo(clientID)
    
    def getAdminInfo(adminID):
        return getAdminDBInfo(adminID)
    
    def registerAdmin(username, password, email, phone):
        user = Admin(username, password, email, phone)
        root.admins[user.id] = user
        transaction.commit()
        
    def registerClient(username, password, email, phone):
        user = Client(username, password, email, phone)
        root.clients[user.id] = user
        transaction.commit()
        return user
        
    def createMealBooking(mealType, time, partySize, numberBooking):
        date = datetime.now().strftime("%d/%m/%Y")
        if mealType == "Dinner":
            meal = Dinner(date,time,partySize)
        elif mealType == "Lunch":
            meal = Lunch(date,time,partySize)
        generateMealBooking(mealType, numberBooking, meal)
        return True
    
    def getBookingByID(bookingID):
        return getBookingDB(bookingID)
    
    def getAllUserBookings():
        return getAllBookings()
    
    def getAllMealBookings(mealType):
        return getAllMealBookingsDB(mealType)
    
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
    
    def updateMealBooking( mealType, date, time, partySize):
        return updateMealBookingDB( mealType, date, time, partySize)
    
    def changeBookingStatus(bookingID, status):
        return updateBookingStatus(bookingID, status)
   
    def checkBookingAvailable(time, date, partySize, mealType):
        print("\nChecking booking availability")

        print("Time: ", time)
        print("Date: ", date)
        print("Party Size: ", partySize)
        print("Meal Type: ", mealType)

        booking = getMealBooking(mealType, date, time).toJson()
        if booking is not None:
            return True
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
        return checkMembershipDB(clientID)
    
    def checkDuplicateUser(username, email):
        clientInfo = getAllClientsDB()
        adminInfo = getAllAdminsDB()
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
        return appendNotification(clientID,notification)
    
    def markBirthday(clientID):
        data = getClientDBInfo(clientID)
        for i in data['notifications']:
            if i == "Happy Birthday!!!":
                return True
        return False
    
    def getUserNotifications(clientID):
        return getNotifications(clientID)
    
    # Course Menu
    def addCourseMenu(type, links):
        return addCourseMenuDB(type, links)
    
    def getCourseMenu(courseType):
        return getCourseMenuDB(courseType)
    
    def addNews(title,image,details,PostDate):
        new = News(title,image,details,PostDate)
        addNews(new)
        return True
    
    def getNews():
        return getAllNews()
    
    def getNewByID(id):
        data = getNewsInformation(id)
        return data

    def addFeedback(title,description, rating):
        feedback = Feedback(title,description, rating)
        createFeedbackDB(feedback)
        return True
    
    def getFeedbackInfo(feedbackID):
        return getFeedbacksByID(feedbackID)
    
    def getFeedbacks():
        return getAllFeedbacksDB()
  
    
        
         