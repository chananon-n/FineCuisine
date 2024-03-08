import random

import persistent

from app.db.database import booking_id


class Booking(persistent.Persistent):
    
    def __init__(self,clientID,course,time,date,partySize,persons,userNotes):
        self.bookingID = booking_id()
        self.clientID = clientID
        self.course = course
        self.time = time
        self.date = date
        self.partySize = partySize
        self.persons = persons
        self.userNotes = userNotes
        self.status = "pending"
        
    def toJson(self):
        return {
            "bookingID": self.bookingID,
            "clientID": self.clientID, 
            "course": self.course,
            "time": self.time,
            "date": self.date,
            "partySize": self.partySize,
            "persons": self.persons,
            "userNotes": self.userNotes,
            "status": self.status
        }

    
    
    