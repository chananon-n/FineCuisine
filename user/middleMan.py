import user as User
class MiddleMan(User):
    def __init__(self,username,password,tel):
        self.username = username
        self.password = password
        self.tel = tel
    
    def setUsername(self,username):
        self.username = username
        
    def setPassword(self,password):
        self.password = password
    
    def setTel(self,tel):
        self.tel = tel
    
    def getUsername(self):
        return self.username 
    
    def getTel(self):
        return self.tel
    
    def generateID(self):
        pass
    