from src.server.configs.db import db


class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=True)

    ### Relations
    questions = db.relationship("Question", back_populates="exam", lazy=True)
    scores = db.relationship("Score", back_populates="exam", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "questions": [question.to_dict() for question in self.questions],
            "scores": [score.to_dict() for score in self.scores],
        }
