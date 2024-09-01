from typing import List
from app.core.repository.user_repository import UserRepository
from app.schemas import user_response, user_request
from app.db.config import Messages


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    async def get_users(
        self, filter_params: dict
    ) -> List[user_response.UserListResponse]:
        return await self.repository.get_users(filter_params)

    async def create(
        self, params: user_request.CreateUserRequest
    ) -> user_response.UserCreateResponse:
        res = await self.repository.create(params)
        return {"id": str(res.id), "message": Messages.CREATE_USER_SUCCESS}
