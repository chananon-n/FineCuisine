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
    def __init__(self, username, password, email, phone):
        super().__init__(username, password, email, phone)
        self.membership = None
        self.id = client_id()
        
    def toJson(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "phone": self.phone,
            "membership": self.membership
        }
        
class Admin(User):
    def __init__(self, username, password, email, phone):
        super().__init__(username, password, email, phone)
        self.id = admin_id()
        
    def toJson(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "phone": self.phone
        }
        