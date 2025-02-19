from flask import Blueprint, jsonify, request, abort
from injector import inject

from src.server.models.exam import Exam
from src.server.models.question import Question
from src.server.services.exam_service import ExamService

exams_bp = Blueprint("exams", __name__)


@exams_bp.route("/getlist", methods=["GET"])
@inject
def get_list(examService: ExamService):
    exams = examService.get_list()
    return jsonify([exam.to_dict() for exam in exams])


@exams_bp.route("/get/<int:exam_id>", methods=["GET"])
@inject
def get_by_id(exam_id: int, examService: ExamService):
    exam = examService.get_by_id(exam_id)
    if not exam:
        abort(404, description="Exam not found")
    return jsonify(exam.to_dict())


@exams_bp.route("/create", methods=["POST"])
@inject
def create(examService: ExamService):
    data = request.get_json(force=True)

    if not data.get("name"):
        abort(400, description="Name is required")

    exam = Exam(name=data["name"], description=data.get("description", ""))

    questions = []
    for question_data in data["questions"]:
        question = Question(
            question_text=question_data["question_text"],
            choice_a=question_data["choice_a"],
            choice_b=question_data["choice_b"],
            choice_c=question_data["choice_c"],
            choice_d=question_data["choice_d"],
            correct_answer=question_data["correct_answer"],
            exam=exam,
        )
        questions.append(question)

    created_exam = examService.create(exam, questions)
    return jsonify(created_exam.to_dict()), 201


@exams_bp.route("/update/<int:exam_id>", methods=["PUT"])
@inject
def update(exam_id: int, examService: ExamService):
    data = request.get_json(force=True)

    updated_exam = examService.update(exam_id, data)

    if not updated_exam:
        abort(404, description="Exam not found")

    return jsonify(updated_exam.to_dict())


@exams_bp.route("/delete/<int:exam_id>", methods=["DELETE"])
@inject
def delete(exam_id: int, examService: ExamService):
    deleted = examService.delete(exam_id)

    if not deleted:
        abort(404, description="Exam not found")

    return jsonify({"message": "Exam deleted successfully"})
