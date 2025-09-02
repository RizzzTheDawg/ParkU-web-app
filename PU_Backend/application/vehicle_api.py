import json
from flask import Blueprint, request, jsonify

from services.Vehicle_service import VehicleService

vehicle_bp = Blueprint("vehicle_bp", __name__)

service = VehicleService()