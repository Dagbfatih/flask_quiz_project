from flask import Blueprint, jsonify, request, abort
from injector import inject

from src.server.models.question import Question
from src.server.services.question_service import QuestionService

questions_bp = Blueprint("questions", __name__)

@questions_bp.route("/getlist", methods=["GET"])
@inject
def get_list(questionService: QuestionService):
    result: list[Question] = questionService.get_list()
    return jsonify([question.to_dict() for question in result])

@questions_bp.route("/create", methods=["POST"])
@inject
def create(questionService: QuestionService):
    data = request.get_json(force=True)

    if not data.get("question_text") or not all(
        data.get(choice) for choice in ["choice_a", "choice_b", "choice_c", "choice_d"]
    ):
        abort(400, description="Incorrect request format")

    question = Question(
        question_text=data["question_text"],
        choice_a=data["choice_a"],
        choice_b=data["choice_b"],
        choice_c=data["choice_c"],
        choice_d=data["choice_d"],
        correct_answer=data["correct_answer"],
        exam_id=data["exam_id"],
    )

    res = questionService.create(question)
    return jsonify(res.to_dict())

@questions_bp.route("/update/<int:question_id>", methods=["PUT"])
@inject
def update(question_id: int, questionService: QuestionService):
    data = request.get_json(force=True)

    if not any(
        data.get(field)
        for field in [
            "question_text",
            "choice_a",
            "choice_b",
            "choice_c",
            "choice_d",
            "correct_answer",
        ]
    ):
        abort(400, description="No valid fields provided for update")

    updated_question = questionService.update(question_id, data)

    if not updated_question:
        abort(404, description="Question not found")

    return jsonify(updated_question.to_dict())

@questions_bp.route("/delete/<int:question_id>", methods=["DELETE"])
@inject
def delete(question_id: int, questionService: QuestionService):
    deleted = questionService.delete(question_id)

    if not deleted:
        abort(404, description="Question not found")

    return jsonify({"message": "Question deleted successfully"})
