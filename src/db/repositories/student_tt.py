""" User repository file """
from typing import Optional, Type

from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.structures.role import Role

from ..models import Base, Student_tt
from .abstract import Repository
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, insert, update, and_
from src import Time


class Student_tt_Repo(Repository[Student_tt]):
    """
    User repository for CRUD and other SQL queries
    """

    def __init__(self, session: AsyncSession):
        """
        Initialize user repository as for all users or only for one user
        """
        super().__init__(type_model=Student_tt, session=session)

    async def new(
            self,
            group_number: Optional[str] = None,
            weekday: Optional[str] = None,
            timetable: Optional[str] = None
    ) -> None:
        """
        Insert a new user into the database
        :param user_id: Telegram user id
        :param user_name: Telegram username

        """

        new_user_tt = await self.session.merge(
            Student_tt(
                group_number=group_number,
                weekday=weekday,
                timetable=timetable,
            )
        )
        await self.session.commit()
        return new_user_tt

    async def exist(self, tg_id: int) -> bool:
        sql = select(Student_tt).where(Student_tt.tg_id == tg_id)
        request = (await self.session.execute(sql)).unique().one_or_none()
        return bool(request)

    async def get_student_tt(self, tg_id: int) -> Student_tt:
        async with self.session as session:
            async with session.begin():
                return (await session.execute(
                    select(Student_tt).where(Student_tt.tg_id == tg_id))).scalars().unique().one_or_none()

    async def change_student_tt(self, tg_id: int, new_group: str):
        await self.session.execute(update(Student_tt).where(Student_tt.tg_id == tg_id).values(group_number=new_group))
        await self.session.commit()

    async def get_tt_tomorrow(self, group_number: str, weekday: str):
        if weekday == "sunday":
            return "Завтра пар нет)"
        else:
            sql = select(Student_tt.timetable).where(Student_tt.group_number == group_number,
                                                     Student_tt.weekday == weekday)
            print(sql)
            tt = (await self.session.execute(sql)).scalars().unique().one_or_none()
            return f"Вот твое расписание на завтра\n{tt}"

    async def get_tt_today(self, group_number, weekday):
        if weekday == "sunday":
            return "Сегодня пар нет)"
        else:
            sql = select(Student_tt.timetable).where(Student_tt.group_number == group_number,
                                                     Student_tt.weekday == weekday)
            tt = (await self.session.execute(sql)).scalars().unique().one_or_none()
            return f"Вот твое расписание на сегодня\n{tt}"

    # async def get_tt_week(self, group_number):
    #     await self.check_connect()
    #     self.cur = await self.conn.cursor()
    #     mes = ''
    #     ind = 0
    #     await self.cur.execute(f"""SELECT * FROM timetable WHERE group_number = "{group_number}" """)
    #     for weekday_ind in self.cur.fetchall():
    #         mes += f"{weekdaysRus[ind]}\n{weekday_ind[3]}\n\n"
    #         ind += 1
    #     await self.cur.close()
    #     return mes

    async def get_tt_week(self, group_number: str):
        sql = select(Student_tt.timetable).where(Student_tt.group_number == group_number)

        week_tt = "Вот твое расписание на неделю\n\n"
        tt_ind = 0
        tt = await self.session.execute(sql)
        for weekday_tt in tt.fetchall():
            week_tt += f"{Time.weekdaysRus[tt_ind]}\n{weekday_tt[0]}\n\n"
            tt_ind += 1
        return week_tt

    async def get_subjects(self, group_number: str):
        sql = select(Student_tt.timetable).where(Student_tt.group_number == group_number)
        subjects_request = (await self.session.execute(sql)).all()
        subjects_list = []
        subjects_set = set()
        for subject_day in subjects_request:
            for subject_period in subject_day[0].split("• ")[1:]:
                subject = subject_period.split("- ")[1]
                subject = subject.split(',')[0]
                subject = subject.split('.')[0]
                print("sub" + subject)
                if subject[0] == '/':
                    subject = subject[2:]
                subjects_set.add(subject)

        for subject in subjects_set:
            subjects_list.append(subject)
        return subjects_list

    async def axax(self):
        print("axaxaxa)")

