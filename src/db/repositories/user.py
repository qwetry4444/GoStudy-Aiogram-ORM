""" User repository file """
from typing import Optional, Type

from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.structures.role import Role

from ..models import Base, User
from .abstract import Repository
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, insert, update


class UserRepo(Repository[User]):
    """
    User repository for CRUD and other SQL queries
    """

    def __init__(self, session: AsyncSession):
        """
        Initialize user repository as for all users or only for one user
        """
        super().__init__(type_model=User, session=session)

    async def new(
            self,
            tg_id: int = None,
            user_name: Optional[str] = None,
            group_number: Optional[str] = None
    ) -> None:
        """
        Insert a new user into the database
        :param user_id: Telegram user id
        :param user_name: Telegram username
        """

        new_user = await self.session.merge(
            User(
                tg_id=tg_id,
                user_name=user_name,
                group_number=group_number,
            )
        )
        await self.session.commit()
        return new_user

    async def exist(self, tg_id: int) -> bool:
        sql = select(User).where(User.tg_id == tg_id)
        request = (await self.session.execute(sql)).unique().one_or_none()
        return bool(request)

    async def get_user(self, tg_id: int) -> User:
        async with self.session as session:
            async with session.begin():
                return (await session.execute(select(User).where(User.tg_id == tg_id))).scalars().unique().one_or_none()

    async def get_user_group(self, tg_id: int) -> str:
        sql = select(User.group_number).where(User.tg_id == tg_id)
        request = (await self.session.execute(sql)).unique().one_or_none()
        return request[0]

    async def change_user_group(self, tg_id: int, new_group: str):
        await self.session.execute(update(User).where(User.tg_id == tg_id).values(group_number=new_group))
        await self.session.commit()
