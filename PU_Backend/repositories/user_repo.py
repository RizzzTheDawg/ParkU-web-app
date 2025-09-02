from db_config import get_connection
from models.user_model import User, UserRequest, UserResponse
import bcrypt

class UserRepo:
    def create(self, request: UserRequest):
        connection = get_connection()
        cursor = connection.cursor()
        if "@g.bracu.ac.bd" in request.Gsuit:
            try:
                request.role="student"
                hashed_pw = bcrypt.hashpw(request.password.encode('utf-8'), bcrypt.gensalt())
                hashed_pw = hashed_pw.decode('utf-8')

                query = """
                    INSERT INTO user (studentID, first_name, last_name, Gsuit, password, role)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query,(request.studentID, request.first_name, request.last_name, request.Gsuit, hashed_pw, request.role,),)
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

    def get_by_id(self,request: UserResponse):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            query = """
                SELECT studentID,password FROM user
                WHERE studentID = %s
            """
            cursor.execute(query, (request.studentID,), )
            data = cursor.fetchone()
            if data:
                stored_password = data[1]
                password_matches = bcrypt.checkpw(request.password.encode('utf-8'), stored_password.encode('utf-8'))
                if password_matches:
                    return "Sign in successfully"
                else:
                    return "Wrong password!"
            else:
                return "User not found"

        except Exception as e:
            return "An Error Occured! please try again"
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
