from flask import Blueprint, json, render_template, request
from flask_login import current_user, login_required
from injector import inject

from src.client.services.score_service import ScoreService
from src.server.models.exam import Exam
from src.server.services.exam_service import ExamService
from src.server.services.score_service import ScoreService as ScoreApiService
from src.server.models.score import Score

index_bp = Blueprint("index", __name__)


@index_bp.route("/")
@login_required
@inject
def home(score_service: ScoreApiService):
    res = score_service.get_list(current_user.id)

    all_scores = score_service.get_list()

    max_personal_score = ScoreService.max_score(res)
    latest_score = ScoreService.latest(res)
    max_score = ScoreService.max_score(all_scores)

    return render_template(
        "index.html",
        scores=res,
        max_personal_score=max_personal_score,
        max_score=max_score,
        latest_score=latest_score,
    )


@index_bp.route("/exam")
@login_required
@inject
def exam(score_service: ScoreApiService, exam_service: ExamService):
    # Scores
    user_scores = score_service.get_list(current_user.id)
    all_scores = score_service.get_list()

    max_personal_score = ScoreService.max_score(user_scores)
    max_score = ScoreService.max_score(all_scores)

    # Questions
    exam: Exam = exam_service.get_list()[0]

    questions = exam.questions

    return render_template(
        "pages/exam.html",
        max_personal_score=max_personal_score,
        max_score=max_score,
        questions=questions,
        exam=exam,
    )
