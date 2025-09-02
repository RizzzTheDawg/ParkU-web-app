class Vehicle:
    def __init__(self, VehicleID, studentID, type, brand):
        self.VehicleID = VehicleID
        self.studentID = studentID
        self.type = type
        self.brand = brand


class VehicleRequest:
    def __init__(self, data):
        self.VehicleID = data.get('VehicleID')     # Optional for insert, required for update
        self.studentID = data.get('studentID')
        self.type = data.get('type')
        self.brand = data.get('brand')


class VehicleResponse:
    def __init__(self, data):
        self.VehicleID = data.get('VehicleID')
        self.studentID = data.get('studentID')
        self.type = data.get('type')
        self.brand = data.get('brand')
