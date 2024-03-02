from app.db.database import *
from app.model.user import *
import transaction
class DatabaseServices:
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
        
    
    
        
        
        

    
    