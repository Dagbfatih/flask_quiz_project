from src.server.models.exam import Exam
from src.server.configs.db import db
from src.server.models.question import Question


class ExamService:

    def get_list(self):
        return Exam.query.all()

    def get_by_id(self, exam_id: int):
        return Exam.query.get(exam_id)

    def create(self, exam: Exam, questions: list[Question] | None):
        exam.questions = questions
        db.session.add(exam)
        db.session.commit()
        return exam

    def update(self, exam_id: int, data: dict):
        exam: Exam = Exam.query.get(exam_id)
        if not exam:
            return None

        exam.name = data.get("name", exam.name)
        exam.description = data.get("description", exam.description)

        db.session.commit()
        return exam

    def delete(self, exam_id: int):
        exam: Exam = Exam.query.get(exam_id)
        if not exam:
            return False

        db.session.delete(exam)
        db.session.commit()
        return True
