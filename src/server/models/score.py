import datetime
from src.server.configs.db import db


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey("exam.id"), nullable=False)

    ### Relations
    user = db.relationship("User", back_populates="scores")
    exam = db.relationship("Exam", back_populates="scores")

    def to_dict(self):
        return {
            "id": self.id,
            "subject": self.subject,
            "score": self.score,
            "date": self.date,
            "user_id": self.user_id,
            "exam_id": self.exam_id,
        }
