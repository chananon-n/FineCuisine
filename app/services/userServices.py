from app.services.databaseServices import DatabaseServices


class UserServices:
        
    def register(self):
        pass
    
    def login(self,usernameInput, passwordInput):
        return DatabaseServices.validateUserLogin(usernameInput, passwordInput)
        
    
def booking(self):
        pass
    
    
    