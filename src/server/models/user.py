from src.server.configs.db import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    password = db.Column(db.String(30))
    # Normally, password should be hashed and (optionally) salted
    # This project is for showing backend skills so we will use as it as not hashed

    scores = db.relationship("Score", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "scores": [score.to_dict() for score in self.scores],
        }
    
    def check_password(self, password):
        return self.password == password
