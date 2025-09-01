from db_config import get_connection
from models.user_model import User, UserRequest, UserResponse

class UserRepo:
    def create(self, request: UserRequest):
        connection = get_connection()
        cursor = connection.cursor()
        if "@g.bracu.ac.bd" in request.Gsuit:
            try:
                request.role="student"
                askiSum=0
                for i in range (len(request.password)):
                    askiSum+=ord(request.password[i])
                request.password=str(askiSum)

                query = """
                    INSERT INTO user (studentID, first_name, last_name, Gsuit, password, role)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query,(request.studentID, request.first_name, request.last_name, request.Gsuit, request.password, request.role,),)
                connection.commit()
                return "You account has been created successfully"
            except Exception as e:
                return "An Error Occured!"
            finally:
                if cursor:
                    cursor.close()
                if connection:
                    connection.close()
        else:
            return "Please enter a valid Gsuit."
