import user as User
class Customer(User):
    def __init__(self,username,password,tel):
        self.username = username
        self.password = password
        self.tel = tel
        
    def setUserName(self,username):
        self.username = username
        
    def setPassword(self,password):
        self.password = password    
        
    def setTel(self,tel):
        self.tel = tel
    
    def getUserName(self):
        return self.username
    
    def getTel(self):
        return self.tel
    
    def generateID(self):
        pass
    
    