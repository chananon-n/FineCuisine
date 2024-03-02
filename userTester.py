from app.db.database import *
from app.model.booking import Booking
from app.model.user import *
from app.controller.userServices import UserServices

from app.model.feedback import *

def register(username, password, email, phone):
    role = assignRole(email)
    if role == "admin":
        user = Admin(username, password, email, phone)
        root.admins[user.id] = user
    else:
        user = Client(username, password, email, phone)
        root.clients[user.id] = user
        
def clientMain():
    while True:
        print("1. View User Profile")
        print("2. View history")
        print("3. Give feedback")
        print("4. Logout")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            if userID in root.clients:
                print(root.clients[userID].toJson())
        elif choice == 2:
            pass
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
            register(username, password, email, phone)
            transaction.commit()
        elif choice == 2:
            username = input("Enter username: ")
            password = input("Enter password: ")
            userServices = UserServices()
            user = userServices.login(username, password)
            if user == "client":
                userRole = "client"
                userID = getClientID(username)
                clientMain()
            elif user == "admin":
                userRole = "admin"
                userID = user.id
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
            time = input("Enter time: ")
            date = input("Enter date: ")
            partySize = int(input("Enter party size: "))
            persons = input("Enter persons: ")
            userNotes = input("Enter user notes: ")
            booking = Booking(time, date, partySize, persons, userNotes)
            root.booking[booking.bookingID] = booking
            transaction.commit()
        else:
            break
    
if __name__ == "__main__":
    bookingMain()