from typing import Any, Dict
from app.core.repository.activity_repository import ActivityRepository
from app.schemas import activity_request
import logging


class ActivityService:
    def __init__(self):
        self.repository = ActivityRepository()

    async def track_activity_updates(self, msg_details: Dict[str, Any]) -> None:
        """
        Handles new activity updates.

        Args:
            details (Dict[str, Any]): The details of the new logged activity.

        Extracts the necessary fields from the msg_details
        """
        name = msg_details.get(name)
        description = msg_details.get(description)
        activity = activity_request.InsertActi(name=name, description=description)
        await self.insert_activity_to_db(activity)

    async def insert_activity_to_db(self, activity) -> None:
        logging.info(f"logging activity with details: {activity}")
        await self.repository.insert_activity(activity)
