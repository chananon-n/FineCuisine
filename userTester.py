from app.db.database import *
from app.model.user import *
from app.services.userServices import UserServices

def register(username, password, email, phone):
    role = assignRole(email)
    if role == "admin":
        user = Admin(username, password, email, phone)
        root.admins[user.id] = user
    else:
        user = Client(username, password, email, phone)
        root.clients[user.id] = user

def main():
    user = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    register(user, password, email, phone)
    transaction.commit()
    
    print(getAllClients())
    print(getAllAdmins())
    
    # print(UserServices().login(user, password))
    
    # clearDB()
    
if __name__ == "__main__":
    main()