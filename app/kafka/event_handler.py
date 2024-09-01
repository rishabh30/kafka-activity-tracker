import json
from app.kafka.constants import Topics
from app.services.activity_service import ActivityService


async def event_handler(topic: str, message: str):
    """
    Processes events according to the specified topic and message.

    Args:
        topic (str): The topic of the event, which determines the action to be taken.
        message (str): The message associated with the event, typically in JSON format.

    Returns: None
    """
    match topic:
        case Topics.ACTIVITY_TRACKING:
            details = json.loads(message)
            await ActivityService().track_activity_updates(details=details)
