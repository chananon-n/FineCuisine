from app.controller.uiServices import RegisterMembershipPage
from app.db.database import *
from app.model.booking import Booking
from app.model.user import *
from app.controller.userServices import UserServices

from app.model.feedback import *

# this function must in databaseServices
def checkBookingAvailable(time, date, partySize, mealType):
    bookInfo = getMealBooking(mealType, date, time)
    if bookInfo['T_LEFT'] >= partySize:
        return True
    else:
        return False
        
def clientMain():
    while True:
        print("1. View User Profile")
        print("2. View history")
        print("3. Give feedback")
        print("4. Logout")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            userServices = UserServices()
            user = userServices.getClientInfo(userID)
            print(user.getUsername())
        elif choice == 2:
            membershipMain()
        elif choice == 3:
            detail = input("Enter feedback: ")
            rating = int(input("Enter rating: "))
            feedback = Feedback(detail, rating)
            root.feedbacks[feedback.id] = feedback
            transaction.commit()
        else:
            break

def main():
    global userRole
    global userID
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            userServices = UserServices()
            userServices.register(username, password, email, phone)
            transaction.commit()
        elif choice == 2:
            username = input("Enter username: ")
            password = input("Enter password: ")
            userServices = UserServices()
            user = userServices.login(username, password)
            if user == "client":
                userRole = "client"
                userID = userServices.getClientID(username)
                clientMain()
            elif user == "admin":
                userRole = "admin"
                userID = getAdmin(username)
                # adminMain()
            else:
                print("Incorrect username or password")
        else:
            break
    
def bookingMain():
    while True:
        print("1. View booking")
        print("2. Make booking")
        print("3. Logout")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(getAllBookings())
        elif choice == 2:
            course = input("Enter course: ")
            time = input("Enter time: ")
            date = input("Enter date: ")
            partySize = int(input("Enter party size: "))
            persons = input("Enter persons: ")
            userNotes = input("Enter user notes: ")
            # status = checkBookingAvailable(time, date, partySize, course)
            # if status:
            #     updateMealBooking(course, date, time, partySize)
            #     booking = Booking(time, date, partySize, persons, userNotes)
            #     addUserBooking(booking)
            res = UserServices.reservation(userID, course, time, date, partySize, persons, userNotes)
            print(res)
        else:
            break
    
def membershipMain():
    while True:
        print("1. View membership")
        print("2. Make membership")
        print("3. Logout")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(getMembership(userID))
        elif choice == 2:
            memberName = input("Enter member name: ")
            memberSurname = input("Enter member surname: ")
            memberBirth = input("Enter member birth: ")    
            dateExpired = datetime.datetime.now() + datetime.timedelta(days=365)
            formatedDate = dateExpired.strftime("%Y-%m-%d")
            data = {"memberName": memberName, "memberSurname": memberSurname, "memberBirth": memberBirth, "dateExpired": formatedDate}
            print()
            print(data)
            registerMembership(userID, data)
        else:
            break
        
def feedbackMain():
    while True:
        print("1. View feedback")
        print("2. Make feedback")
        print("3. Logout")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(getAllFeedbacksDB())
        elif choice == 2:
            detail = input("Enter feedback: ")
            rating = int(input("Enter rating: "))
            title = detail.split(" ")[0]
            feedback = Feedback(title,detail, rating)
            createFeedbackDB(feedback)
            
            print("Feedback added")
        else:
            break

    
if __name__ == "__main__":
    feedbackMain()