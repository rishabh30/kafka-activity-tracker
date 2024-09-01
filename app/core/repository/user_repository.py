from app.db import database_session
from sqlalchemy import select

from app.models.user import User


class UserRepository:

    async def get_users(self, filter_params: dict):
        async with database_session.get_session() as session:
            result = await session.execute(select(User).filter_by(**filter_params))

            user_objects = result.scalars().all()
            return user_objects

    async def create(
        self,
        name: str,
        mobile: str,
        email: str,
    ):
        async with database_session.get_session() as session:
            new_user = User(
                name=name,
                mobile=mobile,
                email=email,
            )
            session.add(new_user)
            await session.commit()
            return new_user
