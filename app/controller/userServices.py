from app.controller.databaseServices import DatabaseServices


class UserServices:
    def login(self,usernameInput, passwordInput):
        return DatabaseServices.validateUserLogin(usernameInput, passwordInput)
    
    def getClientInfo(self,userId):
        client = DatabaseServices.getClientInfo(userId)
        return client
    
    def getAdminInfo(self,userId):
        admin = DatabaseServices.getAdminInfo(userId)
        return admin
        
    def getClientID(self,username):
        client = DatabaseServices.getClient(username)
        return client.id
    
    def getAdminID(self,username):
        admin = DatabaseServices.getAdmin(username)
        return admin.id
    
    
    