from db_config import get_connection
from models.vehicle_model import Vehicle, VehicleRequest, VehicleResponse

class VehicleRepo:
    def creat(self, request: VehicleRequest):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            query="""
                INSERT INTO Vehicle (VehicleID, StudentID, Type, Brand)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (request.studentID, request.VehicleID,request.studentID,request.type,request.brand,),)
            connection.commit()
            return "Your vehicle has been register successfully"
        except Exception as e:
            return "Couldn't register your vehicle please try again after sometime."
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

