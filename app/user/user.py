from abc import ABC,abstractmethod


class User(ABC):
    
    @abstractmethod
    def setUsername(self,username):
        pass
    
    @abstractmethod
    def setPassword(self,password):
        pass
    
    @abstractmethod
    def setTel(self,tel):
        pass
    
    @abstractmethod
    def getUsername(self):
        pass
    
    @abstractmethod
    def getTel(self):
        pass
    