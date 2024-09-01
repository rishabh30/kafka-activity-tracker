from app.db import database_session

from app.models.activity import Activity


class ActivityRepository:

    async def insert(
        self,
        name: str,
        description: str,
    ):
        async with database_session.get_session() as session:
            new_activity = Activity(
                name=name,
                description=description,
            )
            session.add(new_activity)
            await session.commit()
            return new_activity
