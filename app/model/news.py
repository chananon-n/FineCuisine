import persistent
from app.db.database import *

class News(persistent.Persistent):
    def __init__(self,title,image,details,PostDate):
        self.id = news_id()
        self.title = title
        self.image = image
        self.details = details
        self.date = PostDate
        
    def toJson(self):
        return {
            "id": self.id,
            "title": self.title,
            "image": self.image,
            "details": self.details,
            "datePost": self.date
        }
        
