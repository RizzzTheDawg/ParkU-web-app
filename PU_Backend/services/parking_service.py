from repositories.parking_repo import ParkingRepo
from models.parking_model import Parking, ParkingRequest, ParkingResponse


class ParkingService:
    def __init__(self):
        self.repo = ParkingRepo()

    def creat_parking(self, data):
        data = ParkingRequest(data)
        return self.repo.creat(data)
    def delete_parking(self, data):
        return self.repo.delete(data)
