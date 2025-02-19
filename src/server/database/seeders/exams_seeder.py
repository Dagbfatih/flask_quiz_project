from src.server.models.exam import Exam
from src.server.models.question import Question
from src.server.configs.db import db
from faker import Faker
from src.server.core.seeders import BaseSeeder


class ExamSeeder(BaseSeeder.BaseSeeder):
    @staticmethod
    def seed():
        faker = Faker()

        # Create an exam
        exam = Exam(
            name=faker.sentence(nb_words=4), description=faker.paragraph(nb_sentences=2)
        )
        db.session.add(exam)
        db.session.commit()

        # Create 5 random questions for the exam
        questions = [
            Question(
                question_text=faker.sentence(nb_words=7),
                choice_a=faker.word(),
                choice_b=faker.word(),
                choice_c=faker.word(),
                choice_d=faker.word(),
                correct_answer=faker.random_element(
                    elements=("A", "B", "C", "D")
                ),
                exam_id=exam.id,
            )
            for _ in range(5)
        ]
        db.session.bulk_save_objects(questions)
        db.session.commit()

        print("Exam and questions seeded successfully!")
