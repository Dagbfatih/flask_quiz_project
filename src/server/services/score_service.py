from datetime import datetime
from src.server.models.score import Score
from src.server.configs.db import db


class ScoreService:
    def get_list(self, user_id=None):
        if user_id:
            return Score.query.filter_by(user_id=user_id).all()
        return Score.query.all()

    def get(self, id: int):
        return Score.query.get(id)

    def create(self, data: dict):
        score = Score(
            subject=data["subject"],
            score=data["score"],
            date=datetime.now(),
            user_id=data["user_id"],
            exam_id=data["exam_id"],
        )
        db.session.add(score)
        db.session.commit()
        return score

    def update(self, id: int, data: dict):
        score: Score = Score.query.get(id)
        if not score:
            return None

        score.subject = data.get("subject", score.subject)
        score.score = data.get("score", score.score)
        score.user_id = data.get("user_id", score.user_id)
        score.exam_id = data.get("exam_id", score.exam_id)

        db.session.commit()
        return score

    def delete(self, id: int):
        score: Score = Score.query.get(id)
        if not score:
            return False

        db.session.delete(score)
        db.session.commit()
        return True
