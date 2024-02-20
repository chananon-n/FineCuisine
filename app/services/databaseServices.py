from db import database
class DatabaseServices:
    def __init__(self):
        pass
    
    def validateUserLogin(username,password):
        result = database.check_user(username,password)
        return result
    
    def validateAdminLogin(username):
        result = database.checkAdmin(username)
        return result
    
    
        
        
        

    
    