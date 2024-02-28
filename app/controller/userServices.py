from app.services.databaseServices import DatabaseServices


class UserServices:
        
    def register(self,usernameInput,emailInput, phoneInput, passwordInput):
        #check user role
        role = DatabaseServices.validationUserRegister(emailInput)
        return True
        
    
    def login(self,usernameInput, passwordInput):
        return DatabaseServices.validateUserLogin(usernameInput, passwordInput)
        
    
def booking(self):
        pass
    
    
    