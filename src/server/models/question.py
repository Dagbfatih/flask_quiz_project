from enum import Enum

import sqlalchemy
from src.server.configs.db import db
from src.server.enums.choices import Choices


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(500), nullable=False)
    choice_a = db.Column(db.String(100), nullable=False)
    choice_b = db.Column(db.String(100), nullable=False)
    choice_c = db.Column(db.String(100), nullable=False)
    choice_d = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(
        sqlalchemy.Enum(Choices), nullable=False, default=Choices.Empty
    )
    exam_id = db.Column(db.Integer, db.ForeignKey("exam.id"), nullable=False)

    ### Relations
    exam = db.relationship("Exam", back_populates="questions")

    def to_dict(self):
        return {
            "id": self.id,
            "question_text": self.question_text,
            "choice_a": self.choice_a,
            "choice_b": self.choice_b,
            "choice_c": self.choice_c,
            "choice_d": self.choice_d,
            "correct_answer": self.correct_answer.name,  # Ensure this serializes Enum to string
            "exam_id": self.exam_id,
        }
