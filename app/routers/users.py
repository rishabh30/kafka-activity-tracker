from fastapi import APIRouter

from app.schemas import user_request, user_response
from app.services import user_service
from typing import List


router = APIRouter()


@router.post(
    "/user/v1/list",
    response_model=List[user_response.UserListResponse],
    description="Get list of users",
)
async def get_users(
    user_request: user_request.UserListRequest = None,
) -> List[user_response.UserListResponse]:
    return await user_service.UserService().get_users(
        user_request.model_dump(exclude_none=True)
    )


@router.post(
    "/v1/create",
    response_model=user_response.UserCreateResponse,
    description="Create a user",
)
async def create(
    user_request: user_request.CreateUserRequest,
) -> user_response.UserCreateResponse:
    return await user_service.UserService().create(
        user_request.model_dump(exclude_none=True)
    )
