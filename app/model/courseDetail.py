import persistent
from app.db.database import *

class CourseMenu(persistent.Persistent):
    def __init__(self, type, links):
        self.links = links
        self.type = type
        
    def toJson(self):
        return {
            "type": self.type,
            "links": self.links
        }