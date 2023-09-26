from Model.user import User
from config import db
from sqlalchemy.sql import select
from sqlalchemy import update as sql_update, delete as sql_delete


class UserRepository:

    @staticmethod
    async def create(user_data: User):
        async with db as session:
            async with session.begin():
                session.add(user_data)
            await db.commit_rollback()

    @staticmethod
    async def get_by_id(user_id: int):
        async with db as session:
            stmt = select(User).where(User.id == user_id)
            result = await session.execute(stmt)
            user = result.scalars().first()
            return user

    @staticmethod
    async def get_all():
        async with db as session:
            query = select(User)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update(user_id: int, user_data: User):
        async with db as session:
            stmt = select(User).where(User.id == user_id)
            result = await session.execute(stmt)

            user = result.scalars().first()
            user.name = user_data.name
            user.email = user_data.email
            user.password = user_data.password

            query = sql_update(User).where(User.id == user_id).values(
                **user.dict()).execution_options(synchronize_session="fetch")

            await session.execute(query)
            await db.commit_rollback()

    @staticmethod
    async def delete(user_id: int):
        async with db as session:
            query = sql_delete(User).where(User.id == user_id)
            await session.execute(query)
            await db.commit_rollback()

    @staticmethod
    async def get_by_email(email: str):
        async with db as session:
            stmt = select(User).where(User.email == email)
            result = await session.execute(stmt)
            user = result.scalars().first()
            return user
