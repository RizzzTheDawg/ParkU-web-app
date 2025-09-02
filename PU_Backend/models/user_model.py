class User:
    def __init__(self, studentID, first_name, last_name, Gsuit, password, role):
        self.studentID = studentID
        self.first_name = first_name
        self.last_name = last_name
        self.Gsuit = Gsuit
        self.password = password
        self.role = role

class UserRequest:
    def __init__(self, data):
        self.studentID = data.get('studentID')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.Gsuit = data.get('Gsuit')
        self.password = data.get('password')
        self.role = data.get('role')


class UserResponse:
    def __init__(self, data):
        self.studentID = data.get('studentID')
        self.password = data.get('password')
        self.role = data.get('role')