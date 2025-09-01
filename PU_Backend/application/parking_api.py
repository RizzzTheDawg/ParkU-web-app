import json
from flask import Blueprint, request, jsonify

from services.parking_service import ParkingService

parking_bp = Blueprint("parking_bp", __name__)

service = ParkingService()


@parking_bp.route("/parking", methods=["POST"])
def create():
    data = request.get_json()
    parking_data = service.creat_parking(data)
    return jsonify({"message": parking_data})

@parking_bp.route("/parking/<string:ParkingID>", methods=["DELETE"])
def delete(ParkingID):
    data = service.delete_parking(ParkingID)
    return jsonify({"message": data})

