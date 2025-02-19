from flask import Blueprint, jsonify, request, abort
from flask_login import current_user
from injector import inject
from src.server.models.exam import Exam
from src.server.models.question import Question
from src.server.services.score_service import ScoreService

scores_bp = Blueprint("score", __name__)


@scores_bp.route("/getlist", methods=["GET"])
@inject
def get_list(scoreService: ScoreService):
    user_id = request.args.get("user_id")
    scores = scoreService.get_list(user_id)
    return jsonify([score.to_dict() for score in scores])


@scores_bp.route("/get/<int:score_id>", methods=["GET"])
@inject
def get(score_id: int, scoreService: ScoreService):
    score = scoreService.get(score_id)
    if not score:
        abort(404, description="Score not found")
    return jsonify(score.to_dict())


@scores_bp.route("/create", methods=["POST"])
@inject
def create(scoreService: ScoreService):
    data = request.get_json(force=True)

    if (
        not data.get("subject")
        or not data.get("score")
        or not data.get("user_id")
        or not data.get("exam_id")
    ):
        abort(400, description="Missing required fields")

    score = scoreService.create(data)
    return jsonify(score.to_dict()), 201


@scores_bp.route("/submit-quiz", methods=["POST"])
@inject
def submit_quiz(scoreService: ScoreService):
    # Extract form data
    data = request.form
    exam_id = data.get("exam_id")
    username = data.get("username")

    # Get questions and their correct answers from the exam
    exam:Exam | None= Exam.query.get(exam_id)
    if not exam:
        return "Exam not found", 400

    questions:list[Question] = Question.query.filter_by(exam_id=exam_id).all()
    correct_answers = {q.id: q.correct_answer.name for q in questions}

    # Initialize score
    total_questions = len(questions)
    correct_count = 0

    print(data)

    # Check each question's answer
    for question in questions:
        choice = data.get(f"choice{question.id}")
        if choice == correct_answers.get(question.id):
            correct_count += 1

    # Calculate the score as percentage
    score_percentage = (correct_count / total_questions) * 100

    # Save score to the database
    score_data = {
        "subject": exam.name,  # assuming exam has a subject attribute
        "score": score_percentage,
        "user_id": current_user.id,
        "exam_id": exam.id,
    }
    score = scoreService.create(score_data)

    # Return score response
    return f"Quiz submitted. Your score: {score_percentage}%", 200


@scores_bp.route("/update/<int:score_id>", methods=["PUT"])
@inject
def update(score_id: int, scoreService: ScoreService):
    data = request.get_json(force=True)

    score = scoreService.update(score_id, data)
    if not score:
        abort(404, description="Score not found")

    return jsonify(score.to_dict())


@scores_bp.route("/delete/<int:score_id>", methods=["DELETE"])
@inject
def delete(score_id: int, scoreService: ScoreService):
    if not scoreService.delete(score_id):
        abort(404, description="Score not found")

    return jsonify({"message": "Score deleted successfully"})
