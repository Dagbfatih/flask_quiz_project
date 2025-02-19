from src.server.configs.db import db
from src.server.models.user import User


class UserService:
    def get_list(self):
        return db.session.query(User).all()

    def create(self, user:User):
        db.session.add(user)
        db.session.commit()
        return user

    def update(self, user_id: int, data: User):
        user = db.session.query(User).filter_by(id=user_id).first()
        if not user:
            return None

        if "full_name" in data:
            user.full_name = data["full_name"]
        if "password" in data:
            user.password = data["password"]

        db.session.commit()
        return user

    def delete(self, user_id:int):
        user = db.session.query(User).filter_by(id=user_id).first()
        if not user:
            return False

        db.session.delete(user)
        db.session.commit()
        return True
