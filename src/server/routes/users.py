from flask import Blueprint, jsonify, request, abort
from injector import inject

from src.server.models.user import User
from src.server.services.user_service import UserService

users_bp = Blueprint("users", __name__)


@users_bp.route("/getlist", methods=["GET"])
@inject
def get_list(userService: UserService):
    result = userService.get_list()
    return jsonify([user.to_dict() for user in result])


@users_bp.route("/create", methods=["POST"])
@inject
def create(userService: UserService):
    data = request.get_json(force=True)

    if not data.get("full_name") or not data.get("password"):
        abort(400, description="Incorrect request format")

    user = User(full_name=data["full_name"], password=data["password"])

    res = userService.create(user)
    return jsonify(res.to_dict())


@users_bp.route("/update/<int:user_id>", methods=["PUT"])
@inject
def update(user_id: int, userService: UserService):
    data = request.get_json(force=True)

    if not data.get("full_name") and not data.get("password"):
        abort(400, description="No valid fields provided for update")

    updated_user = userService.update(user_id, data)

    if not updated_user:
        abort(404, description="User not found")

    return jsonify(updated_user.to_dict())


@users_bp.route("/delete/<int:user_id>", methods=["DELETE"])
@inject
def delete(user_id: int, userService: UserService):
    deleted = userService.delete(user_id)

    if not deleted:
        abort(404, description="User not found")

    return jsonify({"message": "User deleted successfully"})
