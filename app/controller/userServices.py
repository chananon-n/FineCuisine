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
        role = dataManager.validationUserRegister(email)
        print(role)
        if role == "admin":
            dataManager.registerAdmin(username, password, email, phone)
        else:
            dataManager.registerClient(username, password, email, phone)
    
    def reservation(self,bookingInfo):
        checkAvailable = dataManager.checkBookingAvailable(bookingInfo.time,bookingInfo.date,bookingInfo.partySize,bookingInfo.course)

        if checkAvailable:
            dataManager.updateMealBooking(bookingInfo.course,bookingInfo.date,bookingInfo.time,bookingInfo.partySizes)
            dataManager.addUserBooking(bookingInfo.clientID,bookingInfo.course,bookingInfo.time,bookingInfo.date,bookingInfo.partySize,bookingInfo.persons,bookingInfo.userNotes)
            return True
        else:
            print("Booking not available")
            return False
    
    def registerMembership(self, clientID, fname, lname, dateOfBirth):
        dataManager.registerMembership(clientID, fname, lname, dateOfBirth)
        return True
       