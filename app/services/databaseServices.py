from app.db import database
class DatabaseServices:
    def __init__(self):
        pass
    
    @staticmethod
    def validateUserLogin(username, password):
        return database.checkUser(username, password)
    
    
        
        
        

    
    