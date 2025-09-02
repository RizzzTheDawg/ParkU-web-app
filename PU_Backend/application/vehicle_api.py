import json
from flask import Blueprint, request, jsonify

from services.vehicle_service import vehicleService

vehicle_bp = Blueprint("vehicle_bp", __name__)

service = vehicleService()

@vehicle_bp.route("/vehicle", methods=["POST"])
def create():
    data = request.get_json()
    user_data = service.register(data)
    return jsonify({"message": user_data})