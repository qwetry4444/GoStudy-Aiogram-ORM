""" Chat repository file """
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Group_subjects
from ..models import Group_subjects
from .abstract import Repository
from sqlalchemy import select


class Group_subjectsRepo(Repository[Group_subjects]):
    def __init__(self, session: AsyncSession):
        super().__init__(type_model=Group_subjects, session=session)

    async def new(
            self,
            group_number: str = None,
            subjects: list = None,
    ):
        new_group_subjects = await self.session.merge(
            Group_subjects(
                group_number=group_number,
                subjects=subjects,

            )
        )
        await self.session.commit()
        return new_group_subjects

    async def get_by_group(self, group: str):
        sql = select(Group_subjects.subjects).where(Group_subjects.group_number == group)
        subjects = (await self.session.execute(sql)).scalars().first()
        return subjects
