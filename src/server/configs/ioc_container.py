from flask_injector import FlaskInjector
from injector import singleton

from src.server.services.exam_service import ExamService
from src.server.services.question_service import QuestionService
from src.server.services.score_service import ScoreService
from src.server.services.user_service import UserService


def configure(binder):
    binder.bind(UserService, to=UserService, scope=singleton)
    binder.bind(QuestionService, to=QuestionService, scope=singleton)
    binder.bind(ExamService, to=ExamService, scope=singleton)
    binder.bind(ScoreService, to=ScoreService, scope=singleton)
