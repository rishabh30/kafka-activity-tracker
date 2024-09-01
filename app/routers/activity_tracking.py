from fastapi import APIRouter

from app.schemas import activity_request
from app.services import activity_service


router = APIRouter()


@router.post(
    "activity/v1/insert",
    description="Insert an activity",
)
async def insert(
    activity_request: activity_request.InsertActivityRequest,
) -> None:
    return await activity_service.ActivityService().insert_activity_to_db(
        activity_request.model_dump(exclude_none=True)
    )
