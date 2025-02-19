import random
from src.server.models.score import Score
from src.server.configs.db import db
from src.server.models.user import User
from src.server.models.exam import Exam
from faker import Faker
from src.server.core.seeders import BaseSeeder


class ScoreSeeder(BaseSeeder.BaseSeeder):
    @staticmethod
    def seed():
        faker = Faker()

        users = User.query.all()  # Assuming users have already been created
        exams = Exam.query.all()  # Assuming exams have already been created

        if not users or not exams:
            print("No users or exams to assign scores.")
            return

        for user in users:
            for exam in exams:
                for _ in range(3):
                    score = Score(
                        subject=faker.word(),
                        score=random.randint(50, 85),
                        date=faker.date_time_this_year(),
                        user_id=user.id,
                        exam_id=exam.id,
                    )
                    db.session.add(score)

        db.session.commit()
        print("Scores seeded successfully!")
