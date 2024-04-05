from abc import ABC, abstractmethod
import persistent

from app.db.database import lunch_booking_id,dinner_booking_id


class Meal(persistent.Persistent,ABC):
    def __init__(self,date,time,totalSize) -> None:
        self.date = date
        self.time = time
        self.totalSize = totalSize
    
    @abstractmethod
    def toJson(self):
        pass
        

class Lunch(Meal):
    def __init__(self,date,time,totalSize) -> None:
        super().__init__(date,time,totalSize)
        self.id = lunch_booking_id()
        
    
    def toJson(self):
        return {
            "T_ID": self.id,
            "T_Date": self.date,
            "T_Time": self.time,
            "T_Size": self.totalSize
        }
    
class Dinner(Meal):
    def __init__(self,date,time,totalSize) -> None:
        super().__init__(date,time,totalSize)
        self.id = dinner_booking_id()
        
    
    def toJson(self):
        return {
            "T_ID": self.id,
            "T_Date": self.date,
            "T_Time": self.time,
            "T_Size": self.totalSize
        }    
    