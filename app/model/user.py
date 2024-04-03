from abc import ABC, abstractmethod
import persistent

from app.db.database import *

from datetime import datetime, timedelta

class User(persistent.Persistent, ABC):
    def __init__(self, username, password, email, phone):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        
    @abstractmethod
    def toJson(self):
        pass
    
class Client(User):
    def __init__(self, username, password, email, phone, ):
        super().__init__(username, password, email, phone)
        self.membership = None
        self.history = []
        self.id = client_id()    
        
    def addHistory(self, booking):
        self.history.append(booking) 
    
    def addMembership(self,membership):
        self.membership = membership
    
    def getUsername(self):
        return self.username
    
    def getEmail(self):
        return self.email
    
    def getTel(self):
        return self.phone
    
    def getMembership(self):
        return self.membership
    
    def getFname(self):
        return self.membership.get('memberName')
    
    def getLname(self):
        return self.membership.get('memberSurname')
    
    def getDob(self):
        return self.membership.get('memberBirth')
    
    def getExpireDate(self):
        return self.membership.get('dateExpired')
    
    def toJson(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "phone": self.phone,
            "membership": self.membership,
            "history": self.history
        }
        
class Admin(User):
    def __init__(self, username, password, email, phone):
        super().__init__(username, password, email, phone)
        self.id = admin_id()
        
    def getUsername(self):
        return self.username
        
    def toJson(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "phone": self.phone
        }
        
