import persistent
from app.db.database import *

class Feedback(persistent.Persistent):
    def __init__(self, detail, rating):
        self.id = feedback_id()
        self.detail = detail
        self.rating = rating

    def toJson(self):
        return {
            "detail": self.detail,
            "rating": self.rating
        }