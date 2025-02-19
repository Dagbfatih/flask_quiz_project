import click
from flask.cli import with_appcontext

from src.server.configs.db import db
from src.server.database.seeders.exams_seeder import ExamSeeder
from src.server.database.seeders.scores_seeder import ScoreSeeder
from src.server.database.seeders.users_seeder import UserSeeder


@click.command(name="migration:fresh")
@with_appcontext
def migration_fresh():
    db.drop_all()
    print("All tables dropped successfully!")
    db.create_all()
    print("Tables migrated successfully!")


@click.command(name="db:seed")
@with_appcontext
def db_seed():
    UserSeeder.seed()
    ExamSeeder.seed()
    ScoreSeeder.seed()
