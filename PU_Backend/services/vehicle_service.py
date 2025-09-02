from repositories.vehicle_repo import VehicleRepo
from models.vehicle_model import Vehicle, VehicleRequest, VehicleResponse

class vehicleService:
    def __init__(self):
        self.repo = VehicleRepo()
    def register(self, vehicle):
        data=VehicleRequest(vehicle)
        return self.repo.create(data)