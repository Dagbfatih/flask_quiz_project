from src.server.models.score import Score


class ScoreService:
    @staticmethod
    def max_score(scores: list[Score]) -> Score | None:
        if not scores:
            return None
        
        # Temporarily assumed that scores will be taken as dictionary, not list[Score]
        return max(scores, key=lambda score: score.score)
    
    @staticmethod
    def latest(scores: list[Score]) -> Score | None:
        if not scores:
            return None
        
        # Find the score with the latest date
        return max(scores, key=lambda score: score.date)
