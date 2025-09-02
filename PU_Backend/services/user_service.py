from repositories.user_repo import UserRepo
from models.user_model import User, UserRequest, UserResponse

class userService:
    def __init__(self):
        self.repo = UserRepo()
    def register(self, user):
        data=UserRequest(user)
        return self.repo.create(data)
    def login(self,user):
        data=UserResponse(user)
        return self.repo.get_by_id(data)