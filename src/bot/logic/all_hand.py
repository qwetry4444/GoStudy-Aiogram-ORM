""" This file represents a start logic """
import datetime
from distutils import command

from aiogram import Router, types, F
from aiogram.filters import Command, Text
from aiogram.filters import callback_data
from aiogram.fsm.context import FSMContext
from src.bot.keyboards import keyboards
from src.language.translator import LocalizedTranslator
from src.bot.create_message import welcome_message
import src.messages as mes
from src.bot.keyboards.keyboards import START
from src.db.database import Database
from src.bot.states import States
from src.bot.create_message import change_group_successful
from src import Time

all_hand_router = Router(name="all_hand_router")
callback_router = Router(name="callback_router")
message_router = Router(name="message_router")


@all_hand_router.message(Text(text="Функции"))
async def functions(message: types.Message):
    await message.answer(mes.FUNCTION_MESSAGE, reply_markup=keyboards.FUNCTIONS)


@all_hand_router.message(Text(text="О нас"))
async def about_us(message: types.Message):
    await message.answer(mes.ABOUT_US_MESSAGE, parse_mode='html')


@all_hand_router.message(Text(text="Изменить группу"))
async def change_group_request(message: types.Message, state: FSMContext):
    await message.answer(mes.change_group)
    await state.set_state(States.Change_user_group)


@all_hand_router.message(Text, States.Change_user_group)
async def change_group_finish(message: types.Message, db: Database, state: FSMContext):
    new_group = message.text
    if new_group in mes.groups:
        await db.user.change_user_group(tg_id=message.from_user.id, new_group=new_group)
        await message.answer(change_group_successful(new_group))
        await state.clear()
    else:
        await message.answer(mes.GROUP_NUMBER_FALL)


@all_hand_router.message(Text(text="Свое расписание"))
async def student_tt(message: types.Message):
    await message.answer(mes.WHAT_TT, reply_markup=keyboards.WHAT_TT)


@all_hand_router.message(Text(text="На завтра"))
async def student_tt_tomorrow(message: types.Message, db: Database):
    group = await db.user.get_user_group(message.from_user.id)
    print(group)
    tt = await db.student_tt.get_tt_tomorrow(group_number=group,
                                             weekday=Time.switchWeekday(datetime.datetime.today().weekday() + 1))
    await message.answer(tt, reply_markup=keyboards.FUNCTIONS)


@all_hand_router.message(Text(text="На сегодня"))
async def student_tt_today(message: types.Message, db: Database):
    group = await db.user.get_user_group(message.from_user.id)
    tt = await db.student_tt.get_tt_today(group_number=group,
                                          weekday=Time.switchWeekday(datetime.datetime.today().weekday()))
    await message.answer(tt, reply_markup=keyboards.FUNCTIONS)


@all_hand_router.message(Text(text="На неделю"))
async def student_tt_week(message: types.Message, db: Database):
    group = await db.user.get_user_group(message.from_user.id)
    tt = await db.student_tt.get_tt_week(group_number=group)
    await message.answer(tt, reply_markup=keyboards.FUNCTIONS)


@all_hand_router.message(Text(text="Расписание звонков"))
async def calls_tt(message: types.Message):
    await message.answer(mes.TT_cals)
    await message.answer(Time.tt_Time())


@all_hand_router.message(Text(text="Числитель / Знаменатель"))
async def ch_zn(message: types.Message):
    await message.answer(Time.get_ch_zn())


@all_hand_router.message(Text(text="Узнать ФИО преподавателя"))
async def lecturer_fio(message: types.Message, state: FSMContext, db: Database):
    await message.answer(mes.WHAT_LECTURER_TEACH, reply_markup=keyboards.create_subjects(
        await db.student_tt.get_subjects(await db.user.get_user_group(message.from_user.id))))
    await state.set_state(States.Get_Lecturer_name)


@all_hand_router.message(Text, States.Get_Lecturer_tt)
async def change_group_request(message: types.Message, db: Database, state: FSMContext):
    if message.text.lower() == mes.BACK:
        await message.answer(mes.CANSER_SEARCH, reply_markup=keyboards.FUNCTIONS)
        await state.clear()
        return
    if message.text.lower() not in mes.lecturers_lastnames:
        await message.answer(mes.TRY_AGAIN)
    else:
        lecturer_name = await db.lecturer_tt.get_lecturer_fullname(message.text)
        await message.answer(f"Расписание <b>{lecturer_name}</b>\n\n", parse_mode='html',
                             reply_markup=keyboards.FUNCTIONS)
        await message.answer(await db.lecturer_tt.get_lecturer_tt(message.text), parse_mode='html')
        await state.clear()


@all_hand_router.message(Text(text="2"))
async def get_lecturer_name_by_subject(message: types.Message, db: Database):
    group = await db.user.get_user_group(message.from_user.id)
    tt_spot = await db.student_tt1.get_tt_spot(group_number=group, subject="Проектная деятельность (пр)")
    lecturer_name = await db.lecturer_tt.get_lucturer_name(tt_spot=tt_spot, group=group)
    await message.answer(lecturer_name)


@all_hand_router.message(Text(text="3"))
async def change_group_request(message: types.Message, db: Database):
    await db.lecturer_tt.change_lec_name()


@all_hand_router.message(Text(text="Расписание преподавателя"))
async def get_lecturer_tt(message: types.Message, state: FSMContext):
    await message.answer(mes.SELECT_NAME_LECTURER, reply_markup=keyboards.BACK)
    await state.set_state(States.Get_Lecturer_tt)


@all_hand_router.callback_query(Text)
async def logic_inline(call: types.CallbackQuery, db: Database):
    print(call.data)

    id = call.from_user.id
    print(id)
    await call.message.answer(call.data)
    group = await db.user.get_user_group(id)
    print(2)
    tt_spot = await db.student_tt1.get_tt_spot(group_number=group, subject=call.data)
    print(3)
    lecturer_name = await db.lecturer_tt.get_lucturer_name(tt_spot=tt_spot, group=group)
    print(4)
    await call.message.answer(lecturer_name)






# @all_hand_router.callback_query()
# async def logic_inline(call, db: Database):
#     group = await db.user.get_user_group(call.message.from_user.id)
#     tt_spot = await db.student_tt1.get_tt_spot(group_number=group, subject=call.message.data)
#     lecturer_name = await db.lecturer_tt.get_lucturer_name(tt_spot=tt_spot, group=group)
#     await call.message.answer(lecturer_name)


def tt_one_1(p, tt_p, tt_1):
    for i in tt_1:
        if p in i:
            if " | " not in i:
                if "п/г" not in i:
                    if "//" not in i:
                        tt_p.append(i.split("- ")[1].split(", ")[0])
                        break
                    else:
                        tt_p.append(
                            f"""{i.split("- ")[1].split("//")[0].split(", ")[0]}//{i.split("- ")[1].split("//")[1].split(", ")[0]}""")
                        break
                else:
                    tt_p.append(
                        f"{i.split(', п/г')[0].split(', ')[0].split(' - ')[1]}, п/г{i.split(', п/г')[1].split(', ')[0]}")
                    break
            else:
                tt = i.split(" - ")[1]
                print(tt)
                a = "• 4 пара (13:20-14:40) - Иностранный язык, п/г1, А517 | //Сопротивление материалов, п/г2, А213"
                x1 = tt.split(' | ')[0]
                if "//" in x1:
                    if ', п/г' in x1.split('//')[0]:
                        x11 = f"{x1.split('//')[0].split(', п/г')[0]}, п/г{x1.split('//')[0].split(', п/г')[1].split(', ')[0]}"
                    else:
                        x11 = f"{x1.split('//')[0].split(', ')[0]}"
                    if ', п/г' in x1.split('//')[1]:
                        x12 = f"{x1.split('//')[1].split(', п/г')[0]}, п/г{x1.split('//')[1].split(', п/г')[1].split(', ')[0]}"
                    else:
                        x12 = f"{x1.split('//')[1].split(', ')[0]}"
                else:
                    x11 = f"{x1.split(', п/г')[0]}, п/г{x1.split(', п/г')[1].split(', ')[0]}"

                x2 = tt.split(' | ')[1]
                if "//" in x2:
                    if ', п/г' in x2.split('//')[0]:
                        x21 = f"{x2.split('//')[0].split(', п/г')[0]}, п/г{x2.split('//')[0].split(', п/г')[1].split(', ')[0]}"
                    else:
                        x21 = f"{x2.split('//')[0].split(', ')[0]}"
                    if ', п/г' in x2.split('//')[0]:
                        x22 = f"{x2.split('//')[1].split(', п/г')[0]}, п/г{x2.split('//')[1].split(', п/г')[1].split(', ')[0]}"
                    else:
                        x22 = f"{x2.split('//')[1].split(', ')[0]}"
                else:
                    x21 = f"{x2.split(', п/г')[0]}, п/г{x2.split(', п/г')[1].split(', ')[0]}"

                if "//" in x1 and "//" in x2:
                    tt_p.append(f"{x11.rstrip()}//{x12.rstrip()} | {x21.rstrip()}//{x22.rstrip()}")
                elif "//" in x1:
                    tt_p.append(f"{x11.rstrip()}//{x12.rstrip()} | {x21.rstrip()}")
                elif "//" in x2:
                    tt_p.append(f"{x11.rstrip()} | {x21.rstrip()}//{x22.rstrip()}")
                break
    else:
        tt_p.append(None)


# Физика, п/г1, А316// | //Физика, п/г2, А316
def tt_one(tt_1):
    # • 1 пара (08:30-09:50) - Иностранный язык, п/г1, У507 | Структурное программирование, п/г2, У408
    tt_one_1("1 пара", tt_1p, tt_1)
    tt_one_1("2 пара", tt_2p, tt_1)
    tt_one_1("3 пара", tt_3p, tt_1)
    tt_one_1("4 пара", tt_4p, tt_1)
    tt_one_1("5 пара", tt_5p, tt_1)
    tt_one_1("6 пара", tt_6p, tt_1)
    tt_one_1("7 пара", tt_7p, tt_1)
    tt_one_1("8 пара", tt_8p, tt_1)


def auid_one_1(p, tt_pa, tt_1):
    for i in tt_1:
        a = ' '
        if ", У" in i:
            a = ", У"
        elif ", А" in i:
            a = ", А"
        elif ", С" in i:
            a = ", С"
        elif ", К" in i:
            a = ", K"
        elif ", Г" in i:
            a = ", Г"
        elif ", Э" in i:
            a = ", ЭОиДОТ"
        if p in i and "," in i:
            if " | " not in i:
                if "п/г" not in i:
                    if "//" not in i:
                        tt_pa.append(f"""{a[2:]}{i.split("- ")[1].split(a)[1].rstrip()}""")
                        break
                    else:
                        if a == ", С":
                            tt_pa.append(
                                f"""С""")
                            break
                        else:
                            tt_pa.append(
                            f"""{a[2:] * bool(len(i.split("- ")[1].split("//")[0]) > 1)}{i.split("- ")[1].split("//")[0].split(a)[-1].rstrip() * bool(len(i.split("- ")[1].split("//")[0]) > 1)}//{a[2:] * bool(len(i.split("- ")[1].split("//")[1]) > 1)}{(i.split("- ")[1].split("//")[1].split(a)[-1].rstrip()) * bool(len(i.split("- ")[1].split("//")[1]) > 1)}""")
                            break
                else:
                    tt_pa.append(
                        f"{i.split(', п/г')[1].split(', ')[1].rstrip()}")
                    break
            else:
                # tt = i.split(" - ")[1]
                # tt_pa.append(
                #     f"{tt.split(' | ')[0].split(', п/г')[1].split(', ')[1]} | {'//' * (tt.split(' | ')[1][1] == '/')}{tt.split(' | ')[1].split(', п/г')[1].split(', ')[1].rstrip()}")


                tt = i.split(" - ")[1]
                print(tt)
                a = "• 1 пара (08:30-09:50) - Иностранный язык, п/г1, У506 | Иностранный язык, п/г2, А518"
                x1 = tt.split(' | ')[0]
                if "//" in x1:
                    if ', п/г' in x1.split('//')[0]:
                        x11 = f"{x1.split('//')[0].split(', п/г')[1].split(', ')[1]}"
                    else:
                        x11 = f""
                    if ', п/г' in x1.split('//')[1]:
                        x12 = f"{x1.split('//')[1].split(', п/г')[1].split(', ')[1]}"
                    else:
                        x12 = f""
                else:
                    x11 = f"{x1.split(', п/г')[1].split(', ')[1]}"

                x2 = tt.split(' | ')[1]
                if "//" in x2:
                    if ', п/г' in x2.split('//')[0]:
                        x21 = f"{x2.split('//')[0].split(', п/г')[1].split(', ')[1]}"
                    else:
                        x21 = f""
                    if ', п/г' in x2.split('//')[1]:
                        x22 = f"{x2.split('//')[1].split(', п/г')[1].split(', ')[1]}"
                    else:
                        x22 = f""
                else:
                    x21 = f"{x2.split(', п/г')[1].split(', ')[1]}"

                if "//" in x1 and "//" in x2:
                    tt_pa.append(f"{x11.rstrip()}//{x12.rstrip()} | {x21.rstrip()}//{x22.rstrip()}")
                elif "//" in x1:
                    tt_pa.append(f"{x11.rstrip()}//{x12.rstrip()} | {x21.rstrip()}")
                elif "//" in x2:
                    tt_pa.append(f"{x11.rstrip()} | {x21.rstrip()}//{x22.rstrip()}")
                break
    else:
        tt_pa.append(None)
    df = "• 1 пара (08:30-09:50) - //Физика (пр), А314"

def auid_one(tt_1):
    auid_one_1("1 пара", tt_1pa, tt_1)
    auid_one_1("2 пара", tt_2pa, tt_1)
    auid_one_1("3 пара", tt_3pa, tt_1)
    auid_one_1("4 пара", tt_4pa, tt_1)
    auid_one_1("5 пара", tt_5pa, tt_1)
    auid_one_1("6 пара", tt_6pa, tt_1)
    auid_one_1("7 пара", tt_7pa, tt_1)
    auid_one_1("8 пара", tt_8pa, tt_1)


@all_hand_router.message(Text(text="1"))
async def parse_tt(message: types.Message, db: Database):
    tt = a
    tt = tt.split("\n\n")
    global tt_1, tt_2, tt_4, tt_5, tt_6, tt_1p, tt_2p, tt_3p, tt_4p, tt_5p, tt_6p, tt_7p, tt_8p
    global tt_1pa, tt_2pa, tt_3pa, tt_4pa, tt_5pa, tt_6pa, tt_7pa, tt_8pa
    tt_1 = tt[0].split("• ")
    tt_2 = tt[1].split("• ")
    tt_3 = tt[2].split("• ")
    tt_4 = tt[3].split("• ")
    tt_5 = tt[4].split("• ")
    tt_6 = tt[5].split("• ")
    print(tt_5)
    tt_1p = []
    tt_2p = []
    tt_3p = []
    tt_4p = []
    tt_5p = []
    tt_6p = []
    tt_7p = []
    tt_8p = []

    tt_1pa = []
    tt_2pa = []
    tt_3pa = []
    tt_4pa = []
    tt_5pa = []
    tt_6pa = []
    tt_7pa = []
    tt_8pa = []

    tt_one(tt_1)
    tt_one(tt_2)
    tt_one(tt_3)
    tt_one(tt_4)
    tt_one(tt_5)
    tt_one(tt_6)

    auid_one(tt_1)
    auid_one(tt_2)
    auid_one(tt_3)
    auid_one(tt_4)
    auid_one(tt_5)
    auid_one(tt_6)

    print(tt_1p)
    print(tt_2p)
    print(tt_3p)
    print(tt_4p)
    print(tt_5p)
    print(tt_6p)
    print(tt_7p)
    print(tt_8p)
    print("\nAuiditorii))\n")
    print(tt_1pa)
    print(tt_2pa)
    print(tt_3pa)
    print(tt_4pa)
    print(tt_5pa)
    print(tt_6pa)
    print(tt_7pa)
    print(tt_8pa)
    groups = ["601-21", "601-21м", "602-21", "602-21м", "603-21", "603-22", "603-21м", "604-21", "604-21м", "605-21",
              "605-21м", "606-21", "606-22", "606-21м", "607-21", "607-22", "607-21м", "608-21", "608-22", "608-21м",
              "609-21", "609-22", "601-11", "601-11м", "602-11", "602-11м", "603-11", "603-11м", "604-11", "604-11м",
              "605-11", "605-11м", "606-11", "606-12", "606-11м", "607-11", "607-12", "607-11м", "608-11", "608-12",


              "608-11м",

              "609-11", "609-12", "603-12", "601-01", "602-01", "603-01", "603-02", "604-01", "605-01",
              "606-01",
              "607-01", "608-01", "608-02", "609-01", "601-91", "602-91", "603-91", "603-92", "604-91", "605-91",
              "606-91",
              "607-91", "608-91", "608-92", "609-91"]
    group_number = "609-11"


    await db.student_tt1.new(group_number=group_number, period_number=1, monday_subject=tt_1p[0],
                             monday_class=tt_1pa[0], tuesday_subject=tt_1p[1], tuesday_class=tt_1pa[1],
                             wednesday_subject=tt_1p[2], wednesday_class=tt_1pa[2], thursday_subject=tt_1p[3],
                             thursday_class=tt_1pa[3], friday_subject=tt_1p[4], friday_class=tt_1pa[4],
                             saturday_subject=tt_1p[5], saturday_class=tt_1pa[5])

    await db.student_tt1.new(group_number=group_number, period_number=2, monday_subject=tt_2p[0],
                             monday_class=tt_2pa[0], tuesday_subject=tt_2p[1], tuesday_class=tt_2pa[1],
                             wednesday_subject=tt_2p[2], wednesday_class=tt_2pa[2], thursday_subject=tt_2p[3],
                             thursday_class=tt_2pa[3], friday_subject=tt_2p[4], friday_class=tt_2pa[4],
                             saturday_subject=tt_2p[5], saturday_class=tt_2pa[5])

    await db.student_tt1.new(group_number=group_number, period_number=3, monday_subject=tt_3p[0],
                             monday_class=tt_3pa[0], tuesday_subject=tt_3p[1], tuesday_class=tt_3pa[1],
                             wednesday_subject=tt_3p[2], wednesday_class=tt_3pa[2], thursday_subject=tt_3p[3],
                             thursday_class=tt_3pa[3], friday_subject=tt_3p[4], friday_class=tt_3pa[4],
                             saturday_subject=tt_3p[5], saturday_class=tt_3pa[5])

    await db.student_tt1.new(group_number=group_number, period_number=4, monday_subject=tt_4p[0],
                             monday_class=tt_4pa[0], tuesday_subject=tt_4p[1], tuesday_class=tt_4pa[1],
                             wednesday_subject=tt_4p[2], wednesday_class=tt_4pa[2], thursday_subject=tt_4p[3],
                             thursday_class=tt_4pa[3], friday_subject=tt_4p[4], friday_class=tt_4pa[4],
                             saturday_subject=tt_4p[5], saturday_class=tt_4pa[5])

    await db.student_tt1.new(group_number=group_number, period_number=5, monday_subject=tt_5p[0],
                             monday_class=tt_5pa[0], tuesday_subject=tt_5p[1], tuesday_class=tt_5pa[1],
                             wednesday_subject=tt_5p[2], wednesday_class=tt_5pa[2], thursday_subject=tt_5p[3],
                             thursday_class=tt_5pa[3], friday_subject=tt_5p[4], friday_class=tt_5pa[4],
                             saturday_subject=tt_5p[5], saturday_class=tt_5pa[5])

    await db.student_tt1.new(group_number=group_number, period_number=6, monday_subject=tt_6p[0],
                             monday_class=tt_6pa[0], tuesday_subject=tt_6p[1], tuesday_class=tt_6pa[1],
                             wednesday_subject=tt_6p[2], wednesday_class=tt_6pa[2], thursday_subject=tt_6p[3],
                             thursday_class=tt_6pa[3], friday_subject=tt_6p[4], friday_class=tt_6pa[4],
                             saturday_subject=tt_6p[5], saturday_class=tt_6pa[5])

    await db.student_tt1.new(group_number=group_number, period_number=7, monday_subject=tt_7p[0],
                             monday_class=tt_7pa[0], tuesday_subject=tt_7p[1], tuesday_class=tt_7pa[1],
                             wednesday_subject=tt_7p[2], wednesday_class=tt_7pa[2], thursday_subject=tt_7p[3],
                             thursday_class=tt_7pa[3], friday_subject=tt_7p[4], friday_class=tt_7pa[4],
                             saturday_subject=tt_7p[5], saturday_class=tt_7pa[5])

    await db.student_tt1.new(group_number=group_number, period_number=8, monday_subject=tt_8p[0],
                             monday_class=tt_8pa[0], tuesday_subject=tt_8p[1], tuesday_class=tt_8pa[1],
                             wednesday_subject=tt_8p[2], wednesday_class=tt_8pa[2], thursday_subject=tt_8p[3],
                             thursday_class=tt_8pa[3], friday_subject=tt_8p[4], friday_class=tt_8pa[4],
                             saturday_subject=tt_8p[5], saturday_class=tt_8pa[5])

a = """Расписание на понедельник:
• 2 пара (10:30-11:50) - Элективные дисциплины по физической культуре и спорту, С
• 4 пара (13:20-14:40) - Теория вероятностей (лек), А410//
• 5 пара (14:50-16:10) - Теория вероятностей (пр), А410

Расписание на вторник:
• 1 пара (08:30-09:50) - Иностранный язык, п/г1, У506 | Иностранный язык, п/г2, А518
• 2 пара (10:00-11:20) - Правоведение (пр), А514
• 3 пара (11:30-12:50) - Программирование мобильных устройств, п/г1, У406 | Цифровая схемотехника, п/г2, У401
• 4 пара (13:20-14:40) - Программирование мобильных устройств (лек), У903//

Расписание на среду:
• 2 пара (10:00-11:20) - Цифровая схемотехника (лек), У903
• 3 пара (11:30-12:50) - Теория языков программирования и методы трансляции (лек), У903
• 4 пара (13:20-14:40) - Теория языков программирования и методы трансляции, п/г1, У408
• 5 пара (14:50-16:10) - Программирование на языке Python, п/г1, У406

Расписание на четверг:
• 2 пара (10:30-11:50) - Элективные дисциплины по физической культуре и спорту, С
• 4 пара (13:20-14:40) - Программирование на языке Python (лек), У903// Элементы и устройства автоматизированных систем (лек), У903
• 5 пара (14:50-16:10) - Программирование мобильных устройств, п/г2, У408
• 6 пара (16:20-17:40) - Программирование на языке Python, п/г2, У406

Расписание на пятницу:
• 5 пара (14:50-16:10) - Цифровая схемотехника, п/г1, У401 | Математические основы теории систем, п/г2, У406
• 6 пара (16:20-17:40) - Математические основы теории систем, п/г1, У406 | Теория языков программирования и методы трансляции, п/г2, У408

Расписание на субботу:
• 1 пара (08:30-09:50) - Математические основы теории систем (лек), У903
• 4 пара (13:20-14:40) - Проектная деятельность (пр), ЭОиДОТ
• МООК - Правоведение (лек 32 ч)"""

# if "//" in x1:
#     if ', п/г' in x1.split('//')[0]:
#         x11 = f"{x1.split('//')[0].split(', п/г')[1].split(', ')[1]}"
#     else:
#         x11 = f"{x1.split('//')[0].split(', ')[1]}"
#     if ', п/г' in x1.split('//')[1]:
#         x12 = f"{x1.split('//')[1].split(', п/г')[1].split(', ')[1]}"
#     else:
#         x12 = f"{x1.split('//')[1].split(', ')[1]}"
# else:
#     x11 = f"{x1.split(', п/г')[1].split(', ')[1]}"
#
# x2 = tt.split(' | ')[1]
# if "//" in x2:
#     if ', п/г' in x2.split('//')[0]:
#         x21 = f"{x2.split('//')[0].split(', п/г')[1].split(', ')[1]}"
#     else:
#         x21 = f"{x2.split('//')[0].split(', ')[1]}"
#     if ', п/г' in x2.split('//')[1]:
#         x22 = f"{x2.split('//')[1].split(', п/г')[1].split(', ')[1]}"
#     else:
#         x22 = f"{x2.split('//')[1].split(', ')[1]}"
# else:
#     x21 = f"{x2.split(', п/г')[1].split(', ')[1]}"
#
# if "//" in x1 and "//" in x2:
#     tt_pa.append(f"{x11}//{x12} | {x21}//{x22}")
# elif "//" in x1:
#     tt_pa.append(f"{x11}//{x12} | {x21}")
# elif "//" in x2:
#     tt_pa.append(f"{x11} | {x21}//{x22}")
# break