from app.services.databaseServices import DatabaseServices


class UserServices:
        
    def register(self):
        pass
    
    def login(self,usernameInput, passwordInput):
        loginResult = DatabaseServices.validateLogin(usernameInput, passwordInput)
        if (loginResult):
            if DatabaseServices.validateAdminLogin(usernameInput):
                return "Admin"
            else:
                return "Client"
        else:
            return "Invalid"
        
    
def booking(self):
        pass
    
    
    