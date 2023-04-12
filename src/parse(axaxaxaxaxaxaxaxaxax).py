from typing import Optional


def tt_one(tt_1):
    for i in tt_1:
        if "1 пара" in i:
            if "п/г" not in i:
                tt_1p.append(i.split("- ")[1].split(", ")[0])
                break
        else:

            t12 = i.split("- ")
            t1 = t12[1].split("//")[0].split(", ")[0]
            t2 = t12[1].split("//")[1].split(", ")[0]
            tt_1p.append(f"{t1}//{t2}")
    else:
        tt_1p.append(None)
    for i in tt_1:
        if "2 пара" in i:
            if "//" not in i:
                tt_2p.append(i.split("- ")[1].split(", ")[0])
                break
            else:
                t12 = i.split("- ")
                t1 = t12[1].split("//")[0].split(", ")[0]
                t2 = t12[1].split("//")[1].split(", ")[0]
                tt_2p.append(f"{t1}//{t2}")
    else:
        tt_2p.append(None)

    for i in tt_1:
        if "3 пара" in i:
            if "//" not in i:
                tt_3p.append(i.split("- ")[1].split(", ")[0])
                break
            else:
                t12 = i.split("- ")
                t1 = t12[1].split("//")[0].split(", ")[0]
                t2 = t12[1].split("//")[1].split(", ")[0]
                tt_3p.append(f"{t1}//{t2}")
    else:
        tt_3p.append(None)

    for i in tt_1:
        if "4 пара" in i:
            if "//" not in i:
                tt_4p.append(i.split("- ")[1].split(", ")[0])
                break
            else:
                t12 = i.split("- ")
                t1 = t12[1].split("//")[0].split(", ")[0]
                t2 = t12[1].split("//")[1].split(", ")[0]
                tt_4p.append(f"{t1}//{t2}")
    else:
        tt_4p.append(None)

    for i in tt_1:
        if "5 пара" in i:
            if "//" not in i:
                tt_5p.append(i.split("- ")[1].split(", ")[0])
                break
            else:
                t12 = i.split("- ")
                t1 = t12[1].split("//")[0].split(", ")[0]
                t2 = t12[1].split("//")[1].split(", ")[0]
                tt_5p.append(f"{t1}//{t2}")
    else:
        tt_5p.append(None)

    for i in tt_1:
        if "6 пара" in i:
            if "//" not in i:
                tt_6p.append(i.split("- ")[1].split(", ")[0])
                break
            else:
                t12 = i.split("- ")
                t1 = t12[1].split("//")[0].split(", ")[0]
                t2 = t12[1].split("//")[1].split(", ")[0]
                tt_6p.append(f"{t1}//{t2}")
    else:
        tt_6p.append(None)
    for i in tt_1:
        if "7 пара" in i:
            if "//" not in i:
                tt_7p.append(i.split("- ")[1].split(", ")[0])
                break
            else:
                t12 = i.split("- ")
                t1 = t12[1].split("//")[0].split(", ")[0]
                t2 = t12[1].split("//")[1].split(", ")[0]
                tt_7p.append(f"{t1}//{t2}")
    else:
        tt_7p.append(None)

    for i in tt_1:
        if "8 пара" in i:
            if "//" not in i:
                tt_8p.append(i.split("- ")[1].split(", ")[0])
                break
            else:
                t12 = i.split("- ")
                t1 = t12[1].split("//")[0].split(", ")[0]
                t2 = t12[1].split("//")[1].split(", ")[0]
                tt_8p.append(f"{t1}//{t2}")
    else:
        tt_8p.append(None)


def parse_tt(tt):
    tt = tt.split("\n\n")
    global tt_1, tt_2, tt_4, tt_5, tt_6, tt_1p, tt_2p, tt_3p, tt_4p, tt_5p, tt_6p, tt_7p, tt_8p
    tt_1 = tt[0].split("• ")
    tt_2 = tt[1].split("• ")
    tt_3 = tt[2].split("• ")
    tt_4 = tt[3].split("• ")
    tt_5 = tt[4].split("• ")
    tt_6 = tt[5].split("• ")

    tt_1p = []
    tt_2p = []
    tt_3p = []
    tt_4p = []
    tt_5p = []
    tt_6p = []
    tt_7p = []
    tt_8p = []

    tt_one(tt_1)
    tt_one(tt_2)
    tt_one(tt_3)
    tt_one(tt_4)
    tt_one(tt_5)
    tt_one(tt_6)

    print(tt_1p)
    print(tt_2p)
    print(tt_3p)
    print(tt_4p)
    print(tt_5p)
    print(tt_6p)
    print(tt_7p)
    print(tt_8p)


a = """Расписание на понедельник:
• 1 пара (08:30-09:50) - Проектная деятельность (пр), У408
• 2 пара (10:00-11:20) - Структурное программирование (лек), У903
• 3 пара (11:30-12:50) - Математический анализ (лек), У903
• 6 пара (16:20-17:40) - Базы данных (лек), ЭОиДОТ

Расписание на вторник:
• 3 пара (12:00-13:20) - Физическая культура и спорт//Элективные дисциплины по физической культуре и спорту, С
• 5 пара (14:50-16:10) - Адаптивная верстка с использ. HTML5 и CSS3, п/г2, А320
• 6 пара (16:20-17:40) - Базы данных, п/г2, А320

Расписание на среду:
• 1 пара (08:30-09:50) - Математический анализ (пр), У504
• 2 пара (10:00-11:20) - Работа в команде (пр), А504
• 3 пара (11:30-12:50) - Физика, п/г1, А316// | //Физика, п/г2, А316

Расписание на четверг:
• 1 пара (08:30-09:50) - //Физика (пр), А314
• 2 пара (10:00-11:20) - Физика (лек), А314
• 5 пара (14:50-16:10) - Адаптивная верстка с использованием HTML5 и CSS3 (лек), ЭОиДОТ//

Расписание на пятницу:
• 1 пара (08:30-09:50) - Иностранный язык, п/г1, У507 | Структурное программирование, п/г2, У408
• 2 пара (10:00-11:20) - Структурное программирование, п/г1, У408 | Иностранный язык, п/г2, У508
• 3 пара (11:30-12:50) - История России (пр), А404
• 4 пара (13:30-14:50) - Элективные дисциплины по физической культуре и спорту, С

Расписание на субботу:
• 3 пара (11:30-12:50) - Базы данных, п/г1, А320
• 4 пара (13:20-14:40) - Адаптивная верстка с использованием HTML5 и CSS3, п/г1, А320
• ЭУК - Работа в команде (лек 32 ч)"""
parse_tt(a)


# ['"Расписание на понедельник:\n• 1 пара (08:30-09:50) - Проектная деятельность (пр), У408\n• 2 пара (10:00-11:20) - Структурное программирование (лек), У903\n• 3 пара (11:30-12:50) - Математический анализ (лек). У903\n• 6 пара (16:20-17:40) - Базы данных (лек), ЭОиДОТ', 'Расписание на вторник:\n• 3 пара (12:00-13:20) - Физическая культура и спорт//Элективные дисциплины по физической культуре и спорту, С\n• 5 пара (14:50-16:10) - Адаптивная верстка с использ. HTML5 и CSS3, п/г2, А320\n• 6 пара (16:20-17:40) - Базы данных, п/г2, А320', 'Расписание на среду:\n• 1 пара (08:30-09:50) - Математический анализ (пр). У504\n• 2 пара (10:00-11:20) - Работа в команде (пр), А504\n• 3 пара (11:30-12:50) - Физика, п/г1, А316// | //Физика, п/г2, А316', 'Расписание на четверг:\n• 1 пара (08:30-09:50) - //Физика (пр), А314\n• 2 пара (10:00-11:20) - Физика (лек), А314\n• 5 пара (14:50-16:10) - Адаптивная верстка с использованием HTML5 и CSS3 (лек), ЭОиДОТ//', 'Расписание на пятницу:\n• 1 пара (08:30-09:50) - Иностранный язык, п/г1, У507 | Структурное программирование, п/г2, У408\n• 2 пара (10:00-11:20) - Структурное программирование, п/г1, У408 | Иностранный язык, п/г2, У508\n• 3 пара (11:30-12:50) - История России (пр), А404\n• 4 пара (13:30-14:50) - Элективные дисциплины по физической культуре и спорту, С', 'Расписание на субботу:\n• 3 пара (11:30-12:50) - Базы данных, п/г1, А320\n• 4 пара (13:20-14:40) - Адаптивная верстка с использованием HTML5 и CSS3, п/г1, А320\n• ЭУК - Работа в команде (лек 32 ч)']

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
    return None
# group_number = "609-21"
# new(group_number=group_number, period_number=1, monday_subject=)
# new(group_number=group_number, period_number=2)
# new(group_number=group_number, period_number=3)
# new(group_number=group_number, period_number=4)
# new(group_number=group_number, period_number=5)
# new(group_number=group_number, period_number=6)
# new(group_number=group_number, period_number=7)
# new(group_number=group_number, period_number=8)
