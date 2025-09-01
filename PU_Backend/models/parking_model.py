class Parking:
    def __init__(self, ParkingID, Level):
        self.ParkingID = ParkingID
        self.Level = Level


class ParkingRequest:
    def __init__(self, data):
        self.ParkingID = data.get("ParkingID")
        self.Level = data.get("Level")


class ParkingResponse:
    def __init__(self, data):
        self.ParkingID = data.get("ParkingID")
        self.Level = data.get("Level")
