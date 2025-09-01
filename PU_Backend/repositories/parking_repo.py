from db_config import get_connection
from models.parking_model import Parking, ParkingRequest, ParkingResponse


class ParkingRepo:
    def creat(self, request: ParkingRequest):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            query = """
                INSERT INTO Parking (ParkingID, Level) VALUES
                (%s,%s)
            """
            cursor.execute(
                query,
                (
                    request.ParkingID,
                    request.Level,
                ),
            )
            connection.commit()
            return "New Parking Spot created successfully"
        except Exception as e:
            return f"Error while creating parking spot"
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def delete(self, id):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            query = """
                DELETE FROM parking
                WHERE ParkingID=%s
            """
            cursor.execute(query, (id,))
            connection.commit()
            return "Parking Spot deleted successfully"
        except Exception as e:
            return f"Error while deleting parking spot: {e}"
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

