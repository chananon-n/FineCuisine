from abc import ABC, abstractmethod


class Menu(ABC):
    @abstractmethod
    def setAppetizer(self):
        pass
    
    @abstractmethod
    def setMainCourse(self):
        pass
    
    @abstractmethod
    def setDessert(self):
        pass
    
    @abstractmethod
    def setDrink(self):
        pass
    
    @abstractmethod
    def getAppitizer(self):
        pass
    
    @abstractmethod
    def getMainCourse(self):
        pass
    
    @abstractmethod
    def getDessert(self):
        pass
    
    @abstractmethod
    def getDrink(self):
        pass
    