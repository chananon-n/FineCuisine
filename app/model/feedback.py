import persistent
from app.db.database import *

class Feedback(persistent.Persistent):
    def __init__(self,title, detail, rating):
        self.id = feedback_id()
        self.title = title
        self.detail = detail
        self.rating = rating

    def toJson(self):
        return {
            "title": self.title,
            "detail": self.detail,
            "rating": self.rating
        }