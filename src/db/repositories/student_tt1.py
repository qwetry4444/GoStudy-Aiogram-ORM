""" User repository file """
from typing import Optional, Type

from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.structures.role import Role

from ..models import Base, Student_tt1
from .abstract import Repository
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, insert, update, and_
from src import Time
from src.bot.states import States
from src import messages as mes
from src.Time import convert_tt_day


class Student_tt_Repo1(Repository[Student_tt1]):
    """
    User repository for CRUD and other SQL queries
    """

    def __init__(self, session: AsyncSession):
        """
        Initialize user repository as for all users or only for one user
        """
        super().__init__(type_model=Student_tt1, session=session)

    async def new(
            self,
            id: Optional[int] = None,
            group_number: Optional[str] = None,

            period_number: Optional[int] = None,

            monday_subject: Optional[str] = None,
            monday_class: Optional[str] = None,

            tuesday_subject: Optional[str] = None,
            tuesday_class: Optional[str] = None,

            wednesday_subject: Optional[str] = None,
            wednesday_class: Optional[str] = None,

            thursday_subject: Optional[str] = None,
            thursday_class: Optional[str] = None,

            friday_subject: Optional[str] = None,
            friday_class: Optional[str] = None,

            saturday_subject: Optional[str] = None,
            saturday_class: Optional[str] = None,
    ) -> None:

        new_student_tt1 = await self.session.merge(
            Student_tt1(
                id=id,
                group_number=group_number,
                period_number=period_number,

                monday_subject=monday_subject,
                monday_class=monday_class,

                tuesday_subject=tuesday_subject,
                tuesday_class=tuesday_class,

                wednesday_subject=wednesday_subject,
                wednesday_class=wednesday_class,

                thursday_subject=thursday_subject,
                thursday_class=thursday_class,

                friday_subject=friday_subject,
                friday_class=friday_class,

                saturday_subject=saturday_subject,
                saturday_class=saturday_class
            )
        )
        await self.session.commit()
        return new_student_tt1

    async def get_tt_spot(self, group_number: str, subject: str):
        spot = []
        for period_number in range(1, 8):
            sql = select(Student_tt1.monday_class, Student_tt1.monday_subject, Student_tt1.tuesday_class,
                         Student_tt1.tuesday_subject, Student_tt1.wednesday_class, Student_tt1.wednesday_subject,
                         Student_tt1.thursday_class, Student_tt1.thursday_subject, Student_tt1.friday_class,
                         Student_tt1.friday_subject, Student_tt1.saturday_class, Student_tt1.saturday_subject).where \
                (Student_tt1.group_number == group_number, Student_tt1.period_number == period_number)
            tt = (await self.session.execute(sql)).unique().one_or_none()
            print(tt)
            tt_ind = convert_tt_day(tt=tt, subject=subject)
            if tt_ind != -1:
                spot.append(period_number)
                spot.append(tt_ind)
                break
        print("!!!!!!!!!!!!!")
        print(spot)
        print("!!!!!!!!!!!!!")

        return spot
