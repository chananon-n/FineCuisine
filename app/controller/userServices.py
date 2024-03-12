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
            else:
                user = dataManager.registerClient(username, password, email, phone)
                dataManager.addNotification(user.id,"Welcome to the Fine Cuisine!!!")
            
        else:
            return False
    
    def reservation(self,bookingInfo):
        checkAvailable = dataManager.checkBookingAvailable(bookingInfo.time,bookingInfo.date,bookingInfo.partySize,bookingInfo.course)

        if checkAvailable:
            membership = dataManager.checkMembership(bookingInfo.clientID)
            dataManager.updateMealBooking(bookingInfo.course,bookingInfo.date,bookingInfo.time,bookingInfo.partySizes)
            dataManager.addUserBooking(bookingInfo.clientID,bookingInfo.course,bookingInfo.time,bookingInfo.date,bookingInfo.partySize,bookingInfo.persons,bookingInfo.userNotes)
            dataManager.addNotification(bookingInfo.clientID,"Your booking has been confirmed")
            return bookingInfo, membership
        else:
            print("Booking not available")
            return False
    
    def registerMembership(self, clientID, fname, lname, dateOfBirth):
        dataManager.registerMembership(clientID, fname, lname, dateOfBirth)
        dataManager.addNotification(clientID,"Congratulations, you have successfully registered for membership")
        dataManager.addNotification(clientID,"You have been awarded Birthday Cake on your birthday")
        return True
    
    def getNotifications(self,clientID):
        notifications = dataManager.getNotifications(clientID)
        return notifications
    
    
    
       