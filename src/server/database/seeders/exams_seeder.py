from src.server.models.exam import Exam
from src.server.models.question import Question
from src.server.configs.db import db
from faker import Faker
from src.server.core.seeders import BaseSeeder


class ExamSeeder(BaseSeeder.BaseSeeder):
    @staticmethod
    def seed():
        # Create an exam with fixed values
        exam = Exam(
            name="Basic Computer Science Quiz",
            description="This quiz tests fundamental concepts of computer science.",
        )
        db.session.add(exam)
        db.session.commit()

        # Manually define questions
        questions = [
            Question(
                question_text="What does CPU stand for?",
                choice_a="Central Process Unit",
                choice_b="Central Processing Unit",
                choice_c="Computer Personal Unit",
                choice_d="Central Peripheral Unit",
                correct_answer="B",
                exam_id=exam.id,
            ),
            Question(
                question_text="Which programming language is known as 'the mother of all languages'?",
                choice_a="C",
                choice_b="Python",
                choice_c="Assembly",
                choice_d="Fortran",
                correct_answer="A",
                exam_id=exam.id,
            ),
            Question(
                question_text="What is the main function of an operating system?",
                choice_a="Run antivirus software",
                choice_b="Manage computer hardware and software resources",
                choice_c="Edit documents",
                choice_d="Connect to the internet",
                correct_answer="B",
                exam_id=exam.id,
            ),
            Question(
                question_text="Which data structure uses LIFO (Last In, First Out)?",
                choice_a="Queue",
                choice_b="Array",
                choice_c="Stack",
                choice_d="Linked List",
                correct_answer="C",
                exam_id=exam.id,
            ),
            Question(
                question_text="What does HTML stand for?",
                choice_a="Hyper Text Markup Language",
                choice_b="High Tech Machine Learning",
                choice_c="Hyperlink Text Management Language",
                choice_d="Home Tool Markup Language",
                correct_answer="A",
                exam_id=exam.id,
            ),
        ]

        # Insert questions into the database
        db.session.bulk_save_objects(questions)
        db.session.commit()

        print("Manually seeded exam and questions successfully!")
