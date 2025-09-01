import json
from flask import Blueprint, request, jsonify

from services.user_service import userService

user_bp = Blueprint("user_bp", __name__)

service = userService()

@user_bp.route("/user", methods=["POST"])
def create():
    data = request.get_json()
    user_data = service.register(data)
    return jsonify({"message": user_data})