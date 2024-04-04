import copy
import datetime
import random
import ZODB, ZODB.FileStorage
import BTrees

import transaction

from app.model.courseDetail import CourseMenu


storage = ZODB.FileStorage.FileStorage('app/db/data.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

if not hasattr(root, 'clients'):
    root.clients = BTrees.OOBTree.BTree()
if not hasattr(root, 'admins'):
    root.admins = BTrees.OOBTree.BTree()  
if not hasattr(root, 'feedbacks'):
    root.feedbacks = BTrees.OOBTree.BTree()
if not hasattr(root, 'booking'):
    root.booking = BTrees.OOBTree.BTree()
if not hasattr(root,'DinnerBooking'):
    root.DinnerBooking = BTrees.OOBTree.BTree()
if not hasattr(root,'LunchBooking'):
    root.LunchBooking = BTrees.OOBTree.BTree()
if not hasattr(root,'notification'):
    root.notification = BTrees.OOBTree.BTree()
if not hasattr(root, 'courseMenu'):
    root.courseMenu = BTrees.OOBTree.BTree()
if not hasattr(root,'news'):
    root.news = BTrees.OOBTree.BTree()

def client_id():
    if not hasattr(root, 'client_id'):
        root.client_id = 0
    root.client_id += 1
    formatted_id = f'C{root.client_id:04d}'
    return formatted_id

def admin_id():
    if not hasattr(root, 'admin_id'):
        root.admin_id = 0
    root.admin_id += 1
    formatted_id = f'A{root.admin_id:04d}'
    return formatted_id

def feedback_id():
    if not hasattr(root, 'feedback_id'):
        root.feedback_id = 0
    root.feedback_id += 1
    return root.feedback_id

def booking_id():
    if not hasattr(root, 'booking_id'):
        root.booking_id = 0
    root.booking_id += 1
    return root.booking_id

def membership_id():
    if not hasattr(root, 'membership_id'):
        root.membership_id = 0
    root.membership_id += 1
    return root.membership_id

def news_id():
    if not hasattr(root, 'news_id'):
        root.news_id = 0
    root.news_id += 1
    return root.news_id

def dinner_booking_id():
    if not hasattr(root, 'dinner_id'):
        root.dinner_id = 0
    root.dinner_id += 1
    return root.dinner_id

def lunch_booking_id():
    if not hasattr(root, 'lunch_id'):
        root.lunch_id = 0
    root.lunch_id += 1
    return root.lunch_id

def getClient(username):
    for client in root.clients.values():
        if client.username == username:
            return client
    return None

def getAdmin(username):
    for admin in root.admins.values():
        if admin.username == username:
            return admin
    return None

def getClientDBInfo(clientID):
    for client in root.clients.values():
        if client.id == clientID:
            return client

def getAdminDBInfo(adminID):
    for admin in root.admins.values():
        if admin.id == adminID:
            return admin

def checkUser(username, password):
    for client in root.clients.values():
        if client.username == username and client.password == password:
            return "client"
    for admin in root.admins.values():
        if admin.username == username and admin.password == password:
            return "admin"
    return "Incorrect username or password"

#regitser user
def assignRole(email):
    if email.endswith("@finecuisine.ac.th"):
        return "admin"
    else:
        return "client"
    
# check database
def getAllClientsDB():
    return [client.toJson() for client in root.clients.values()]

def getAllAdminsDB():
    return [admin.toJson() for admin in root.admins.values()]

def clearDB():
    root.clients.clear()
    root.admins.clear()
    root.memberships.clear()
    transaction.commit()    

def getAllBookings():
    return [booking.toJson() for booking in root.booking.values()]

def getBookingDB(bookingID):
    for booking in root.booking.values():
        if booking.bookingID == bookingID:
            return booking
    return "Booking not found"

def getMembership(clientID):
    for client in root.clients.values():
        if client.id == clientID:
            return client.membership
    return "Not found user"

def registerMembership(clientID,membership):
    for client in root.clients.values():
        if client.id == clientID:
            client.membership = membership
            transaction.commit()
            return True
    return False

# def registerAdmin(admin):
#     root.admins[admin.id] = admin
#     transaction.commit()
        
# def registerClient(client):
#     root.clients[client.id] = client
#     transaction.commit()


def checkMembershipDB(clientID):
    for client in root.clients.values():
        if client.id == clientID and client.membership != None:
            return client.membership
    return False

def generateMealBooking(mealType,num_bookings,booking):
    booking_id = booking.id
    base_date = datetime.datetime.strptime(booking.date, "%d/%m/%Y")

    for i in range(num_bookings):
        date = base_date + datetime.timedelta(days=i)
        booking.date = date.strftime("%d/%m/%Y")
        booking_id += 1

        # Create a new booking object with incremented ID and updated date
        new_booking = copy.deepcopy(booking)  # Avoid modifying the original booking object
        new_booking.id = booking_id
        new_booking.date = booking.date
        getattr(root, f'{mealType}Booking')[booking_id] = new_booking
        transaction.commit()
        

def getAllMealBookingsDB(meal_type):
    return [booking.toJson() for booking in getattr(root, f'{meal_type}Booking').values()]
    # return [getattr(root, f'{meal_type}Booking')[booking_key] for booking_key in getattr(root, f'{meal_type}Booking')]

def clearMealBookings(meal_type):
    getattr(root, f'{meal_type}Booking').clear()
    transaction.commit()
    
@staticmethod
def getMealBooking(meal_type, t_date, t_time):
    for booking in getattr(root, f'{meal_type}Booking').values():
        if booking.date == t_date and booking.time == t_time:
            return booking
    return None
        
def clearUserBookings():
    root.booking.clear()
    transaction.commit()
    
def updateMealBookingDB(meal_type, t_date, t_time, t_left):
    for booking in getattr(root, f'{meal_type}Booking').values():
        if booking.date == t_date and booking.time == t_time:
            booking.totalSize -= t_left
            transaction.commit()
            return True
    return False

def addUserBooking(booking):
    root.booking[booking.bookingID] = booking
    transaction.commit()
    return True

def getUserBookings(clientID):
    return [booking.toJson() for booking in root.booking.values() if booking.clientID == clientID]

def updateBookingStatus(bookingID, status):
    for booking in root.booking.values():
        if booking.bookingID == bookingID:
            booking.status = status
            transaction.commit()
            return True
    return False

def clearClientInfo():
    root.clients.clear()
    transaction.commit()
    
def clearAdminInfo():
    root.admins.clear()
    transaction.commit()
    
def removeClient(clientID):
    for client in root.clients.values():
        if client.id == clientID:
            del root.clients[client.id]
            transaction.commit()
            return True
    return False

def removeAdmin(adminID):
    for admin in root.admins.values():
        if admin.id == adminID:
            del root.admins[admin.id]
            transaction.commit()
            return True
    return False

def createNotification(clientID, message):
    for client in root.notification.values():
        if client.id == clientID:
            client.notifications.append(message)
            transaction.commit()
            return True
        elif client.id != clientID:
            root.notification[clientID] = message
            transaction.commit()
            return True
    return False

def getNotifications(clientID):
    for client in root.notification.values():
        if client.id == clientID:
            return client.notifications
        
def addCourseMenuDB(courseType, courseLink):
    if courseType in root.courseMenu:
        autoRemoveCourseMenu(courseType)
    course = CourseMenu(courseType, courseLink)
    root.courseMenu[courseType] = course
    transaction.commit()
    print("Course Menu Added")
    return True

def autoRemoveCourseMenu(courseType):
    del root.courseMenu[courseType]
    transaction.commit()
    print("Course Menu Removed")
    return True
        
def getCourseMenuDB(type):
    for course in root.courseMenu.values():
        if course.type == type:
            return course.links
    return False

def clearCourseMenu():
    root.courseMenu.clear()
    transaction.commit()
    
def addNews(information):
    root.news[information.id] = information
    transaction.commit()
    print("News Added")
    return True

def getAllNews():
    return [news.toJson() for news in root.news.values()]

def getNewsInformation(newsID):
    for news in root.news.values():
        if news.id == newsID:
            return news
    return False

def delNews():
    root.news.clear()
    #set id to 0
    root.news_id = 0
    transaction.commit()
    return True

def createFeedbackDB(feedback):
    root.feedbacks[feedback.id] = feedback
    transaction.commit()
    return True

def getFeedbacksByID(feedbackID):
    for feedback in root.feedbacks.values():
        if feedback.id == feedbackID:
            return feedback
    return False

def getAllFeedbacksDB():
    return [feedback.toJson() for feedback in root.feedbacks.values()]

def clearFeedbacksDB():
    root.feedbacks.clear()
    transaction.commit()
    return True

 