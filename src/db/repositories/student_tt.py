""" User repository file """
from typing import Optional, Type

from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.structures.role import Role

from ..models import Base, Student_tt, Group_subjects
from .abstract import Repository
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, insert, update, and_
from src import Time
from src.Time import get_corp

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

        week_tt = ''
        tt_ind = 0
        tt = await self.session.execute(sql)
        for weekday_tt in tt.fetchall():
            week_tt += f"{Time.weekdaysRus[tt_ind]}\n{weekday_tt[0]}\n\n"
            tt_ind += 1
        return week_tt

    async def get_subjects(self, group_number: str):
        sql = select(Group_subjects.subjects).where(Group_subjects.group_number == group_number)
        subjects_request = (await self.session.execute(sql)).scalar()
        print(subjects_request)
        return subjects_request


        # sql = select(Student_tt.timetable).where(Student_tt.group_number == group_number)
        # subjects_request = (await self.session.execute(sql)).all()
        # subjects_list = []
        # subjects_set = set()
        # for subject_day in subjects_request:
        #     for subject_period in subject_day[0].split("• ")[1:]:
        #         print(subject_period)
        #         subject_period = subject_period.split(" - ")[1]
        #         subject_period = subject_period.replace(".", ",")
        #         subject_period = subject_period.replace(" , ", ", ")
        #         subject_period = subject_period.replace(" | ", "|")
        #         for i in range(len(subject_period)):
        #             if subject_period[i] == "," and i != len(subject_period):
        #                 if subject_period[i + 1] != ' ':
        #                     subject_period = f"{subject_period[:i + 1]} {subject_period[i + 1:]}"
        #         if "," in subject_period:
        #             if "|" not in subject_period:
        #                 if "//" not in subject_period:
        #                     if "п/г" not in subject_period:
        #                         print(subject_period)
        #                         corp = get_corp(subject_period)
        #                         print(corp)
        #                         subject = subject_period.split(corp)[0]
        #                     else:
        #                         subject = f"""{subject_period.split(", п/г")[0]}, п/г{subject_period.split(", п/г")[1].split(',')[0]}"""
        #                     subjects_set.add(subject)
        #                 else:
        #                     subject1 = subject_period.split("//")[0]
        #                     subject2 = subject_period.split("//")[1]
        #                     corp1 = get_corp(subject1)
        #                     corp2 = get_corp(subject2)
        #                     if "," in subject1:
        #                         if "п/г" not in subject1:
        #                             subject1 = subject1.split(corp1)[0]
        #                         else:
        #                             subject1 = f"""{subject1.split(", п/г")[0]}, п/г{subject1.split(", п/г")[1].split(',')[0]}"""
        #                         subjects_set.add(subject1)
        #
        #                     if "," in subject2:
        #                         if "п/г" not in subject2:
        #                             subject2 = subject2.split(corp2)[0]
        #                         else:
        #                             subject2 = f"""{subject2.split(", п/г")[0]}, п/г{subject2.split(", п/г")[1].split(',')[0]}"""
        #                         subjects_set.add(subject2)
        #
        #             else:
        #                 subjects1 = subject_period.split("|")[0]
        #                 subjects2 = subject_period.split("|")[1]
        #
        #                 if "//" not in subjects1:
        #                     if "," in subjects1:
        #                         corp1 = get_corp(subjects1)
        #                         if "п/г" not in subjects1:
        #                             subject1 = subjects1.split(corp1)[0]
        #                         else:
        #                             subject1 = f"""{subjects1.split(", п/г")[0]}, п/г{subjects1.split(", п/г")[1].split(',')[0]}"""
        #                         subjects_set.add(subject1)
        #
        #                 else:
        #                     subject11 = subjects1.split("//")[0]
        #                     subject21 = subjects1.split("//")[1]
        #                     corp11 = get_corp(subject11)
        #                     corp21 = get_corp(subject21)
        #
        #                     if "," in subject11:
        #                         if "п/г" not in subject11:
        #                             subject11 = subject11.split(corp11)[0]
        #                         else:
        #                             subject11 = f"""{subject11.split(", п/г")[0]}, п/г{subject11.split(", п/г")[1].split(',')[0]}"""
        #                         subjects_set.add(subject11)
        #
        #                     if "," in subject21:
        #                         if "п/г" not in subject21:
        #                             subject21 = subject21.split(corp21)[0]
        #                         else:
        #                             subject21 = f"""{subject21.split(", п/г")[0]}, п/г{subject21.split(", п/г")[1].split(',')[0]}"""
        #                         subjects_set.add(subject21)
        #
        #
        #                 if "//" not in subjects2:
        #                     if "," in subjects2:
        #                         corp2 = get_corp(subjects2)
        #                         if "п/г" not in subjects2:
        #                             subject2 = subjects2.split(corp2)[0]
        #                         else:
        #                             subject2 = f"""{subjects2.split(", п/г")[0]}, п/г{subjects2.split(", п/г")[1].split(',')[0]}"""
        #
        #                         subjects_set.add(subject2)
        #
        #                 else:
        #                     subject12 = subjects2.split("//")[0]
        #                     subject22 = subjects2.split("//")[1]
        #                     corp12 = get_corp(subject12)
        #                     corp22 = get_corp(subject22)
        #
        #                     if "," in subject12:
        #                         if "п/г" not in subject12:
        #                             subject12 = subject12.split(corp12)[0]
        #                         else:
        #                             subject12 = f"""{subject12.split(", п/г")[0]}, п/г{subject12.split(", п/г")[1].split(',')[0]}"""
        #
        #                         subjects_set.add(subject12)
        #
        #                     if "," in subject22:
        #                         if "п/г" not in subject22:
        #                             subject22 = subject22.split(corp22)[0]
        #                         else:
        #                             subject22 = f"""{subject22.split(", п/г")[0]}, п/г{subject22.split(", п/г")[1].split(',')[0]}"""
        #                         subjects_set.add(subject22)
        #
        # for subject in subjects_set:
        #     subjects_list.append(subject)
        # return subjects_list

    async def axax(self):
        print("axaxaxa)")

