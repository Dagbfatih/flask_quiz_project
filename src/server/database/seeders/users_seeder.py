from src.server.models.user import User
from src.server.configs.db import db
from faker import Faker
from src.server.core.seeders import BaseSeeder


class UserSeeder(BaseSeeder.BaseSeeder):
    @staticmethod
    def seed():
        faker = Faker()

        users = [
            User(full_name="user", password="12345678"),
            User(full_name="user2", password="12345678"),
            User(full_name=faker.name(), password="12345678"),
            User(full_name=faker.name(), password="12345678"),
            User(full_name=faker.name(), password="12345678"),
            User(full_name=faker.name(), password="12345678"),
        ]

        # Insert users into the database
        db.session.bulk_save_objects(users)
        db.session.commit()

        print("Users seeded successfully!")
