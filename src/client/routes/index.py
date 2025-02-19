from flask import Blueprint, json, render_template, request
from flask_login import current_user, login_required
import requests

from src.client.services.score_service import ScoreService
from src.server.models.score import Score

index_bp = Blueprint("index", __name__)


@index_bp.route("/")
@login_required
def home():
    res = requests.get(
        request.url_root + "/api/scores/getlist?user_id=" + str(current_user.id)
    )
    personal_scores = json.loads(res.content.decode("utf-8"))

    all_scores_res = requests.get(request.url_root + "/api/scores/getlist")
    all_scores = json.loads(all_scores_res.content.decode("utf-8"))

    max_personal_score = ScoreService.max_score(personal_scores)
    latest_score = ScoreService.latest(personal_scores)

    max_score = ScoreService.max_score(all_scores)

    return render_template(
        "index.html",
        scores=personal_scores,
        max_personal_score=max_personal_score,
        max_score=max_score,
        latest_score=latest_score,
    )


@index_bp.route("/exam")
@login_required
def exam():
    # Scores
    user_scores = requests.get(
        request.url_root + "/api/scores/getlist?user_id=" + str(current_user.id)
    )
    personal_scores = json.loads(user_scores.content.decode("utf-8"))
    all_scores_res = requests.get(request.url_root + "/api/scores/getlist")
    all_scores = json.loads(all_scores_res.content.decode("utf-8"))

    max_personal_score = ScoreService.max_score(personal_scores)
    max_score = ScoreService.max_score(all_scores)

    # Questions
    exam_res = requests.get(request.url_root + "/api/exams/getlist")
    exam = json.loads(exam_res.content.decode("utf-8"))[0]

    questions = exam["questions"]

    return render_template(
        "pages/exam.html",
        max_personal_score=max_personal_score,
        max_score=max_score,
        questions=questions,
        exam=exam,
    )
