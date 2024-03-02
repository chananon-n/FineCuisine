import random

import persistent

from app.db.database import booking_id


class Booking(persistent.Persistent):
    
    def __init__(self,time,date,partySize,persons,userNotes):
        self.bookingID = booking_id()
        self.time = time
        self.date = date
        self.partySize = partySize
        self.persons = persons
        self.userNotes = userNotes
        self.status = "pending"
        
    def toJson(self):
        return {
            "bookingID": self.bookingID,
            "time": self.time,
            "date": self.date,
            "partySize": self.partySize,
            "persons": self.persons,
            "userNotes": self.userNotes,
            "status": self.status
        }

    
    
    