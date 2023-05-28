""" User repository file """
from typing import Optional, Type

from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.structures.role import Role

from ..models import Base, Lecturer_tt
from .abstract import Repository
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, insert, update, and_
from src import Time
from src.bot.states import States
from src import messages as mes
from parse2 import full_names, small_names

class Lecturer_tt_Repo(Repository[Lecturer_tt]):
    """
    User repository for CRUD and other SQL queries
    """

    def __init__(self, session: AsyncSession):
        """
        Initialize user repository as for all users or only for one user
        """
        super().__init__(type_model=Lecturer_tt, session=session)

    async def new(
            self,
            id: Optional[int] = None,
            lecturer_name: Optional[str] = None,

            department: Optional[int] = None,

            period_number: Optional[int] = None,

            monday_group: Optional[str] = None,
            monday_class: Optional[str] = None,

            tuesday_group: Optional[str] = None,
            tuesday_class: Optional[str] = None,

            wednesday_group: Optional[str] = None,
            wednesday_class: Optional[str] = None,

            thursday_group: Optional[str] = None,
            thursday_class: Optional[str] = None,

            friday_group: Optional[str] = None,
            friday_class: Optional[str] = None,

            saturday_group: Optional[str] = None,
            saturday_class: Optional[str] = None,
    ) -> None:

        new_lecturer_tt = await self.session.merge(
            Lecturer_tt(
                id=id,
                lecturer_name=lecturer_name,
                department=department,

                period_number=period_number,

                monday_group=monday_group,
                monday_class=monday_class,

                tuesday_group=tuesday_group,
                tuesday_class=tuesday_class,

                wednesday_group=wednesday_group,
                wednesday_class=wednesday_class,

                thursday_group=thursday_group,
                thursday_class=thursday_class,

                friday_group=friday_group,
                friday_class=friday_class,

                saturday_group=saturday_group,
                saturday_class=saturday_class
            )
        )
        await self.session.commit()
        return new_lecturer_tt

    async def get_lecturer_fullname(self, lecturer_name: str) -> str:
        last_name = lecturer_name.split()[0].lower()
        if last_name in mes.lecturers_lastnames:
            sql = select(Lecturer_tt.lecturer_name).where(Lecturer_tt.lecturer_name.like(f"{lecturer_name.title()}%"))
            name = (await self.session.execute(sql)).first()
            return name[0]

    async def get_lucturer_name(self, tt_spot: list, group: str) -> str:
        print(tt_spot)
        print(group)
        if tt_spot[1] == 0:
            sql = select(Lecturer_tt.lecturer_name).where(Lecturer_tt.period_number == tt_spot[0],
                                                          Lecturer_tt.monday_group.like(f"%{group}%"))
            print(sql)
            return (await self.session.execute(sql)).scalars().unique().first()
        if tt_spot[1] == 1:
            sql = select(Lecturer_tt.lecturer_name).where(Lecturer_tt.period_number == tt_spot[0],
                                                          Lecturer_tt.tuesday_group.like(f"%{group}%"))
            print(sql)
            return (await self.session.execute(sql)).scalars().unique().first()
        if tt_spot[1] == 2:
            sql = select(Lecturer_tt.lecturer_name).where(Lecturer_tt.period_number == tt_spot[0],
                                                          Lecturer_tt.wednesday_group.like(f"%{group}%"))
            print(sql)
            return (await self.session.execute(sql)).scalars().unique().first()
        if tt_spot[1] == 3:
            sql = select(Lecturer_tt.lecturer_name).where(Lecturer_tt.period_number == tt_spot[0],
                                                          Lecturer_tt.thursday_group.like(f"%{group}%"))
            print(sql)
            return (await self.session.execute(sql)).scalars().unique().first()
        if tt_spot[1] == 4:
            sql = select(Lecturer_tt.lecturer_name).where(Lecturer_tt.period_number == tt_spot[0],
                                                          Lecturer_tt.friday_group.like(f"%{group}%"))
            print(sql)
            return (await self.session.execute(sql)).scalars().unique().first()
        if tt_spot[1] == 5:
            sql = select(Lecturer_tt.lecturer_name).where(Lecturer_tt.period_number == tt_spot[0],
                                                          Lecturer_tt.saturday_group.like(f"%{group}%"))
            print(sql)
            return (await self.session.execute(sql)).scalars().unique().first()

    async def get_lecturer_tt(self, lecturer_name: str) -> str:
        last_name = lecturer_name.split()[0].lower()
        # print(last_name.title())
        # print(last_name in mes.lecturers_lastnames)
        if last_name in mes.lecturers_lastnames:
            tt_monday = "<b>Понедельник</b>\n"
            tt_tuesday = "<b>Вторник</b>\n"
            tt_wednesday = "<b>Среда</b>\n"
            tt_thursday = "<b>Четверг</b>\n"
            tt_friday = "<b>Пятница</b>\n"
            tt_saturday = "<b>Суббота</b>\n"

            sql = select(Lecturer_tt).where(Lecturer_tt.lecturer_name.like(f"{lecturer_name.title()}%"))
            tt = (await self.session.execute(sql)).all()
            # print(tt[1][0].id)
            tt_monday_exist = tt_tuesday_exist = tt_wednesday_exist = tt_thursday_exist = tt_friday_exist = tt_saturday_exist = 0
            for ind in range(8):
                tt_monday += f"{ind + 1} пара - {tt[ind][0].monday_group}  :  {tt[ind][0].monday_class}\n" * bool(tt[ind][0].monday_class)
                tt_monday_exist += bool(tt[ind][0].monday_class)

                tt_tuesday += f"{ind + 1} пара - {tt[ind][0].tuesday_group}  :  {tt[ind][0].tuesday_class}\n" * bool(tt[ind][0].tuesday_class)
                tt_tuesday_exist += bool(tt[ind][0].tuesday_class)

                tt_wednesday += f"{ind + 1} пара - {tt[ind][0].wednesday_group}  :  {tt[ind][0].wednesday_class}\n" * bool(tt[ind][0].wednesday_class)
                tt_wednesday_exist += bool(tt[ind][0].wednesday_class)

                tt_thursday += f"{ind + 1} пара - {tt[ind][0].thursday_group}  :  {tt[ind][0].thursday_class}\n" * bool(tt[ind][0].thursday_class)
                tt_thursday_exist += bool(tt[ind][0].thursday_class)

                tt_friday += f"{ind + 1} пара - {tt[ind][0].friday_group}  :  {tt[ind][0].friday_class}\n" * bool(tt[ind][0].friday_class)
                tt_friday_exist += bool(tt[ind][0].friday_class)

                tt_saturday += f"{ind + 1} пара - {tt[ind][0].saturday_group}  :  {tt[ind][0].saturday_class}\n" * bool(tt[ind][0].saturday_class)
                tt_saturday_exist += bool(tt[ind][0].saturday_class)
                # for weekday_tt in tt.fetchall():
                #     week_tt += f"{Time.weekdaysRus[tt_ind]}\n{weekday_tt[0]}\n\n"
                #     tt_ind += 1

            ans = tt_monday + (((int(not (bool(tt_monday_exist)))) * "Пар нет\n") + "\n" +
                               tt_tuesday + ((int(not (bool(tt_tuesday_exist)))) * "Пар нет\n") + "\n" +
                               tt_wednesday + ((int(not (bool(tt_wednesday_exist)))) * "Пар нет\n") + "\n" +
                               tt_thursday + (int(not (bool(tt_thursday_exist))) * "Пар нет\n") + "\n" +
                               tt_friday + (int(not (bool(tt_friday_exist))) * "Пар нет\n") + "\n" +
                               tt_saturday + ((int(not (bool(tt_saturday_exist)))) * "Пар нет\n"))
            return ans

    async def change_lec_name(self):

        # full_names = mes.FULL_NAMES
        # full_names = full_names.replace("\n", " ").split(" ")
        # full_names_arr = []
        #
        # print(full_names)
        # for i in range(0, len(full_names), 3):
        #     full_names_arr.append(f"{full_names[i]} {full_names[i + 1]} {full_names[i + 2]}")
        # print(full_names_arr)



        sql = select(Lecturer_tt.lecturer_name)
        x = (await(self.session.execute(sql))).all()
        print(x)
        count = 0
        for i in range(len(x)):
            if '.' in x[i][0]:
                count += 1
        print(count)
        print(len(x))
        #
        # full_names = full_names_arr
        # small_names = []
        # for i in range(len(full_names)):
        #     print(i)
        #     small_names.append(f"{full_names[i].split(' ')[0]} {full_names[i].split(' ')[1][0]}.{full_names[i].split(' ')[2][0]}.")
        #
        # for i in range(len(full_names)):
        #     print(full_names[i], small_names[i])
        #     sql = update(Lecturer_tt).where(Lecturer_tt.lecturer_name.like(small_names[i])).values(lecturer_name=full_names[i])
        #     print(sql)
        #     await self.session.execute(sql)
        #     await self.session.commit()
