from app.db import database
class DatabaseServices:
    def __init__(self):
        pass
    
    @staticmethod
    def validateUserLogin(username, password):
        return database.checkUser(username, password)
    
    def getAllClients():
        return database.getAllClients()
    
    def getAllAdmin():
        return database.getAllAdmins()
    
    def validationUserRegister(email):
        return database.assignRole(email)
    
    
    
        
        
        

    
    