from src.server.models.question import Question
from src.server.configs.db import db


class QuestionService:
    def get_list(self):
        return Question.query.all()

    def create(self, question: Question):
        db.session.add(question)
        db.session.commit()
        return question

    def update(self, question_id: int, data: dict):
        question: Question = Question.query.get(question_id)
        if not question:
            return None

        if data.get("question_text"):
            question.question_text = data["question_text"]
        if data.get("choice_a"):
            question.choice_a = data["choice_a"]
        if data.get("choice_b"):
            question.choice_b = data["choice_b"]
        if data.get("choice_c"):
            question.choice_c = data["choice_c"]
        if data.get("choice_d"):
            question.choice_d = data["choice_d"]
        if data.get("correct_answer"):
            question.correct_answer = data["correct_answer"]

        db.session.commit()
        return question

    def delete(self, question_id: int):
        question: Question = Question.query.get(question_id)

        if not question:
            return False

        db.session.delete(question)
        db.session.commit()
        return True
