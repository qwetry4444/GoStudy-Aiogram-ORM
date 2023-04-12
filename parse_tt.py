from typing import Optional
from src.db.database import Database as db
from src.db.database import create_session_maker
def tt_one(tt_1):
#• 1 пара (08:30-09:50) - Иностранный язык, п/г1, У507 | Структурное программирование, п/г2, У408
    for i in tt_1:
        if "1 пара" in i:
            if " | " not in i:
                if "п/г" not in i:
                    tt_1p.append(i.split("- ")[1].split(", ")[0])
                    break
                else:
                    tt_1p.append(f"{i.split(', п/г')[0].split(', ')[0].split(' - ')[1]}, п/г{i.split(', п/г')[1].split(', ')[0]}")
                    break
            else:
                tt = i.split(" - ")[1]
                print(tt)
                tt_1p.append(f"{tt.split(' | ')[0].split(', п/г')[0]}, п/г{i.split(' | ')[0].split(', п/г')[1].split(', ')[0]} |"
                             f" {tt.split(' | ')[1].split(', п/г')[0]}, п/г{i.split(' | ')[1].split(', п/г')[1].split(', ')[0]}")
                break
    else:
        tt_1p.append(None)

    for i in tt_1:
        if "2 пара" in i:
            if " | " not in i:
                if "п/г" not in i:
                    tt_2p.append(i.split("- ")[1].split(", ")[0])
                    break
                else:
                    tt_2p.append(
                        f"{i.split(', п/г')[0].split(', ')[0].split(' - ')[1]}, п/г{i.split(', п/г')[1].split(', ')[0]}")
                    break
            else:
                tt = i.split(" - ")[1]
                print(tt)
                tt_2p.append(
                    f"{tt.split(' | ')[0].split(', п/г')[0]}, п/г{i.split(' | ')[0].split(', п/г')[1].split(', ')[0]} |"
                    f" {tt.split(' | ')[1].split(', п/г')[0]}, п/г{i.split(' | ')[1].split(', п/г')[1].split(', ')[0]}")
                break
    else:
        tt_2p.append(None)

    for i in tt_1:
        if "3 пара" in i:
            if " | " not in i:
                if "п/г" not in i:
                    tt_3p.append(i.split("- ")[1].split(", ")[0])
                    break
                else:
                    tt_3p.append(
                        f"{i.split(', п/г')[0].split(', ')[0].split(' - ')[1]}, п/г{i.split(', п/г')[1].split(', ')[0]}")
                    break
            else:
                tt = i.split(" - ")[1]
                print(tt)
                tt_3p.append(
                    f"{tt.split(' | ')[0].split(', п/г')[0]}, п/г{i.split(' | ')[0].split(', п/г')[1].split(', ')[0]} |"
                    f" {tt.split(' | ')[1].split(', п/г')[0]}, п/г{i.split(' | ')[1].split(', п/г')[1].split(', ')[0]}")
                break
    else:
        tt_3p.append(None)

    for i in tt_1:
        if "4 пара" in i:
            if " | " not in i:
                if "п/г" not in i:
                    tt_4p.append(i.split("- ")[1].split(", ")[0])
                    break
                else:
                    tt_4p.append(
                        f"{i.split(', п/г')[0].split(', ')[0].split(' - ')[1]}, п/г{i.split(', п/г')[1].split(', ')[0]}")
                    break
            else:
                tt = i.split(" - ")[1]
                print(tt)
                tt_4p.append(
                    f"{tt.split(' | ')[0].split(', п/г')[0]}, п/г{i.split(' | ')[0].split(', п/г')[1].split(', ')[0]} |"
                    f" {tt.split(' | ')[1].split(', п/г')[0]}, п/г{i.split(' | ')[1].split(', п/г')[1].split(', ')[0]}")
                break
    else:
        tt_4p.append(None)

    for i in tt_1:
        if "5 пара" in i:
            if " | " not in i:
                if "п/г" not in i:
                    tt_5p.append(i.split("- ")[1].split(", ")[0])
                    break
                else:
                    tt_5p.append(
                        f"{i.split(', п/г')[0].split(', ')[0].split(' - ')[1]}, п/г{i.split(', п/г')[1].split(', ')[0]}")
                    break
            else:
                tt = i.split(" - ")[1]
                print(tt)
                tt_5p.append(
                    f"{tt.split(' | ')[0].split(', п/г')[0]}, п/г{i.split(' | ')[0].split(', п/г')[1].split(', ')[0]} |"
                    f" {tt.split(' | ')[1].split(', п/г')[0]}, п/г{i.split(' | ')[1].split(', п/г')[1].split(', ')[0]}")
                break
    else:
        tt_5p.append(None)

    for i in tt_1:
        if "6 пара" in i:
            if " | " not in i:
                if "п/г" not in i:
                    tt_6p.append(i.split("- ")[1].split(", ")[0])
                    break
                else:
                    tt_6p.append(
                        f"{i.split(', п/г')[0].split(', ')[0].split(' - ')[1]}, п/г{i.split(', п/г')[1].split(', ')[0]}")
                    break
            else:
                tt = i.split(" - ")[1]
                print(tt)
                tt_6p.append(
                    f"{tt.split(' | ')[0].split(', п/г')[0]}, п/г{i.split(' | ')[0].split(', п/г')[1].split(', ')[0]} |"
                    f" {tt.split(' | ')[1].split(', п/г')[0]}, п/г{i.split(' | ')[1].split(', п/г')[1].split(', ')[0]}")
                break
    else:
        tt_6p.append(None)

    for i in tt_1:
        if "7 пара" in i:
            if " | " not in i:
                if "п/г" not in i:
                    tt_7p.append(i.split("- ")[1].split(", ")[0])
                    break
                else:
                    tt_7p.append(
                        f"{i.split(', п/г')[0].split(', ')[0].split(' - ')[1]}, п/г{i.split(', п/г')[1].split(', ')[0]}")
                    break
            else:
                tt = i.split(" - ")[1]
                print(tt)
                tt_7p.append(
                    f"{tt.split(' | ')[0].split(', п/г')[0]}, п/г{i.split(' | ')[0].split(', п/г')[1].split(', ')[0]} |"
                    f" {tt.split(' | ')[1].split(', п/г')[0]}, п/г{i.split(' | ')[1].split(', п/г')[1].split(', ')[0]}")
                break
    else:
        tt_7p.append(None)

    for i in tt_1:
        if "8 пара" in i:
            if " | " not in i:
                if "п/г" not in i:
                    tt_8p.append(i.split("- ")[1].split(", ")[0])
                    break
                else:
                    tt_8p.append(
                        f"{i.split(', п/г')[0].split(', ')[0].split(' - ')[1]}, п/г{i.split(', п/г')[1].split(', ')[0]}")
                    break
            else:
                tt = i.split(" - ")[1]
                print(tt)
                tt_8p.append(
                    f"{tt.split(' | ')[0].split(', п/г')[0]}, п/г{i.split(' | ')[0].split(', п/г')[1].split(', ')[0]} |"
                    f" {tt.split(' | ')[1].split(', п/г')[0]}, п/г{i.split(' | ')[1].split(', п/г')[1].split(', ')[0]}")
                break
    else:
        tt_8p.append(None)

def auid_one(tt_1):
    for i in tt_1:
        if "1 пара" in i:
            if " | " not in i:
                if "п/г" not in i:
                    tt_1pa.append(i.split("- ")[1].split(", ")[1].rstrip())
                    break
                else:
                    tt_1pa.append(
                        f"{i.split(', п/г')[1].split(', ')[1].rstrip()}")
                    break
            else:
                tt = i.split(" - ")[1]
                tt_1pa.append(f"{tt.split(' | ')[0].split(', п/г')[1].split(', ')[1]} | {tt.split(' | ')[1].split(', п/г')[1].split(', ')[1].rstrip()}")
    else:
        tt_1pa.append(None)

    for i in tt_1:
        if "2 пара" in i:
            if " | " not in i:
                if "п/г" not in i:
                    tt_2pa.append(i.split("- ")[1].split(", ")[1].rstrip())
                    break
                else:
                    tt_2pa.append(
                        f"{i.split(', п/г')[1].split(', ')[1].rstrip()}")
                    break
            else:
                tt = i.split(" - ")[1]
                tt_2pa.append(f"{tt.split(' | ')[0].split(', п/г')[1].split(', ')[1]} | {tt.split(' | ')[1].split(', п/г')[1].split(', ')[1].rstrip()}")
    else:
        tt_2pa.append(None)

    for i in tt_1:
        if "3 пара" in i:
            if " | " not in i:
                if "п/г" not in i:
                    tt_3pa.append(i.split("- ")[1].split(", ")[1].rstrip())
                    break
                else:
                    tt_3pa.append(
                        f"{i.split(', п/г')[1].split(', ')[1].rstrip()}")
                    break
            else:
                tt = i.split(" - ")[1]
                tt_3pa.append(f"{tt.split(' | ')[0].split(', п/г')[1].split(', ')[1]} | {tt.split(' | ')[1].split(', п/г')[1].split(', ')[1].rstrip()}")
    else:
        tt_3pa.append(None)

    for i in tt_1:
        if "4 пара" in i:
            if " | " not in i:
                if "п/г" not in i:
                    tt_4pa.append(i.split("- ")[1].split(", ")[1].rstrip())
                    break
                else:
                    tt_4pa.append(
                        f"{i.split(', п/г')[1].split(', ')[1].rstrip()}")
                    break
            else:
                tt = i.split(" - ")[1]
                tt_4pa.append(f"{tt.split(' | ')[0].split(', п/г')[1].split(', ')[1]} | {tt.split(' | ')[1].split(', п/г')[1].split(', ')[1].rstrip()}")
    else:
        tt_4pa.append(None)

    for i in tt_1:
        if "5 пара" in i:
            if " | " not in i:
                if "п/г" not in i:
                    tt_5pa.append(i.split("- ")[1].split(", ")[1].rstrip())
                    break
                else:
                    tt_5pa.append(
                        f"{i.split(', п/г')[1].split(', ')[1].rstrip()}")
                    break
            else:
                tt = i.split(" - ")[1]
                tt_5pa.append(f"{tt.split(' | ')[0].split(', п/г')[1].split(', ')[1]} | {tt.split(' | ')[1].split(', п/г')[1].split(', ')[1].rstrip()}")
    else:
        tt_5pa.append(None)

    for i in tt_1:
        if "6 пара" in i:
            if " | " not in i:
                if "п/г" not in i:
                    tt_6pa.append(i.split("- ")[1].split(", ")[1].rstrip())
                    break
                else:
                    tt_6pa.append(
                        f"{i.split(', п/г')[1].split(', ')[1].rstrip()}")
                    break
            else:
                tt = i.split(" - ")[1]
                tt_6pa.append(f"{tt.split(' | ')[0].split(', п/г')[1].split(', ')[1]} | {tt.split(' | ')[1].split(', п/г')[1].split(', ')[1].rstrip()}")
    else:
        tt_6pa.append(None)

    for i in tt_1:
        if "7 пара" in i:
            if " | " not in i:
                if "п/г" not in i:
                    tt_7pa.append(i.split("- ")[1].split(", ")[1].rstrip())
                    break
                else:
                    tt_7pa.append(
                        f"{i.split(', п/г')[1].split(', ')[1].rstrip()}")
                    break
            else:
                tt = i.split(" - ")[1]
                tt_7pa.append(f"{tt.split(' | ')[0].split(', п/г')[1].split(', ')[1]} | {tt.split(' | ')[1].split(', п/г')[1].split(', ')[1].rstrip()}")
    else:
        tt_7pa.append(None)

    for i in tt_1:
        if "8 пара" in i:
            if " | " not in i:
                if "п/г" not in i:
                    tt_8pa.append(i.split("- ")[1].split(", ")[1].rstrip())
                    break
                else:
                    tt_8pa.append(
                        f"{i.split(', п/г')[1].split(', ')[1].rstrip()}")
                    break
            else:
                tt = i.split(" - ")[1]
                tt_8pa.append(f"{tt.split(' | ')[0].split(', п/г')[1].split(', ')[1]} | {tt.split(' | ')[1].split(', п/г')[1].split(', ')[1].rstrip()}")
    else:
        tt_8pa.append(None)





def parse_tt(tt):
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

    group_number="609-21"
    create_session_maker()
    db.student_tt1.new(group_number=group_number, period_number=1, monday_subject=tt_1p[0], monday_class=tt_1pa[0], thursday_subject=tt_1p[1], thursday_class=tt_1pa[1], wednesday_subject=tt_1p[2], wednesday_class=tt_1pa[2], saturday_subject=tt_1p[3], saturday_class=tt_1pa[3], friday_subject=tt_1p[4], friday_class=tt_1pa[4], tuesday_subject=tt_1p[5], tuesday_class=tt_1pa[5])

    db.student_tt1.new(group_number=group_number, period_number=1, monday_subject=tt_2p[0], monday_class=tt_2pa[0], thursday_subject=tt_2p[1], thursday_class=tt_2pa[1], wednesday_subject=tt_2p[2], wednesday_class=tt_2pa[2], saturday_subject=tt_2p[3], saturday_class=tt_2pa[3], friday_subject=tt_2p[4], friday_class=tt_2pa[4], tuesday_subject=tt_2p[5], tuesday_class=tt_2pa[5])

    db.student_tt1.new(group_number=group_number, period_number=1, monday_subject=tt_3p[0], monday_class=tt_3pa[0], thursday_subject=tt_3p[1], thursday_class=tt_3pa[1], wednesday_subject=tt_3p[2], wednesday_class=tt_3pa[2], saturday_subject=tt_3p[3], saturday_class=tt_3pa[3], friday_subject=tt_3p[4], friday_class=tt_3pa[4], tuesday_subject=tt_3p[5], tuesday_class=tt_3pa[5])

    db.student_tt1.new(group_number=group_number, period_number=1, monday_subject=tt_4p[0], monday_class=tt_4pa[0], thursday_subject=tt_4p[1], thursday_class=tt_4pa[1], wednesday_subject=tt_4p[2], wednesday_class=tt_4pa[2], saturday_subject=tt_4p[3], saturday_class=tt_4pa[3], friday_subject=tt_4p[4], friday_class=tt_4pa[4], tuesday_subject=tt_4p[5], tuesday_class=tt_4pa[5])

    db.student_tt1.new(group_number=group_number, period_number=1, monday_subject=tt_5p[0], monday_class=tt_5pa[0], thursday_subject=tt_5p[1], thursday_class=tt_5pa[1], wednesday_subject=tt_5p[2], wednesday_class=tt_5pa[2], saturday_subject=tt_5p[3], saturday_class=tt_5pa[3], friday_subject=tt_5p[4], friday_class=tt_5pa[4], tuesday_subject=tt_5p[5], tuesday_class=tt_5pa[5])

    db.student_tt1.new(group_number=group_number, period_number=1, monday_subject=tt_6p[0], monday_class=tt_6pa[0], thursday_subject=tt_6p[1], thursday_class=tt_6pa[1], wednesday_subject=tt_6p[2], wednesday_class=tt_6pa[2], saturday_subject=tt_6p[3], saturday_class=tt_6pa[3], friday_subject=tt_6p[4], friday_class=tt_6pa[4], tuesday_subject=tt_6p[5], tuesday_class=tt_6pa[5])

    db.student_tt1.new(group_number=group_number, period_number=1, monday_subject=tt_7p[0], monday_class=tt_7pa[0], thursday_subject=tt_7p[1], thursday_class=tt_7pa[1], wednesday_subject=tt_7p[2], wednesday_class=tt_7pa[2], saturday_subject=tt_7p[3], saturday_class=tt_7pa[3], friday_subject=tt_7p[4], friday_class=tt_7pa[4], tuesday_subject=tt_7p[5], tuesday_class=tt_7pa[5])

    db.student_tt1.new(group_number=group_number, period_number=1, monday_subject=tt_8p[0], monday_class=tt_8pa[0], thursday_subject=tt_8p[1], thursday_class=tt_8pa[1], wednesday_subject=tt_8p[2], wednesday_class=tt_8pa[2], saturday_subject=tt_8p[3], saturday_class=tt_8pa[3], friday_subject=tt_8p[4], friday_class=tt_8pa[4], tuesday_subject=tt_8p[5], tuesday_class=tt_8pa[5])



a = """Расписание на понедельник:
• 2 пара (10:00-11:20) - Структурное программирование (лек), У903
• 3 пара (11:30-12:50) - Математический анализ (лек), У903
• 4 пара (13:20-14:40) - Физика, п/г1, А316// | //Физика, п/г2, А316
• 6 пара (16:20-17:40) - Базы данных (лек), ЭОиДОТ

Расписание на вторник:
• 3 пара (11:30-12:50) - Проектная деятельность (пр), У408
• 4 пара (13:20-14:40) - Адаптивная верстка с исп. HTML5 и CSS3 (12ч), п/г1, А320// | //Адаптивная верстка с исп. HTML5 и CSS3 (12ч), п/г2, А320

Расписание на среду:
• 1 пара (08:30-09:50) - Работа в команде (пр), А504
• 2 пара (10:00-11:20) - История России (пр), А514
• 3 пара (11:30-12:50) - Математический анализ (пр), У504
• 5 пара (15:00-16:25) - Физическая культура и спорт//Элективные дисциплины по физической культуре и спорту, С

Расписание на четверг:
• 1 пара (08:30-09:50) - Физика (пр), А314//
• 2 пара (10:00-11:20) - Физика (лек), А314
• 4 пара (13:20-14:40) - Адаптивная верстка с использованием HTML5 и CSS3 (20ч), п/г2, ЭОиДОТ
• 5 пара (14:50-16:10) - Адаптивная верстка с использованием HTML5 и CSS3 (лек), ЭОиДОТ//
• 6 пара (16:20-17:40) - Адаптивная верстка с использованием HTML5 и CSS3 (20ч), п/г1, ЭОиДОТ

Расписание на пятницу:
• 2 пара (10:00-11:20) - Иностранный язык, п/г2, У507
• 3 пара (11:30-12:50) - Иностранный язык, п/г1, У507 | Структурное программирование, п/г2, У408
• 4 пара (13:20-14:40) - Структурное программирование, п/г1, У408 | Базы данных, п/г2, А320
• 5 пара (14:50-16:10) - Базы данных, п/г1, А320

Расписание на субботу:
• 3 пара (12:00-13:20) - Элективные дисциплины по физической культуре и спорту, С
• ЭУК - Работа в команде (лек 32 ч)"""
parse_tt(a)


#['"Расписание на понедельник:\n• 1 пара (08:30-09:50) - Проектная деятельность (пр), У408\n• 2 пара (10:00-11:20) - Структурное программирование (лек), У903\n• 3 пара (11:30-12:50) - Математический анализ (лек). У903\n• 6 пара (16:20-17:40) - Базы данных (лек), ЭОиДОТ', 'Расписание на вторник:\n• 3 пара (12:00-13:20) - Физическая культура и спорт//Элективные дисциплины по физической культуре и спорту, С\n• 5 пара (14:50-16:10) - Адаптивная верстка с использ. HTML5 и CSS3, п/г2, А320\n• 6 пара (16:20-17:40) - Базы данных, п/г2, А320', 'Расписание на среду:\n• 1 пара (08:30-09:50) - Математический анализ (пр). У504\n• 2 пара (10:00-11:20) - Работа в команде (пр), А504\n• 3 пара (11:30-12:50) - Физика, п/г1, А316// | //Физика, п/г2, А316', 'Расписание на четверг:\n• 1 пара (08:30-09:50) - //Физика (пр), А314\n• 2 пара (10:00-11:20) - Физика (лек), А314\n• 5 пара (14:50-16:10) - Адаптивная верстка с использованием HTML5 и CSS3 (лек), ЭОиДОТ//', 'Расписание на пятницу:\n• 1 пара (08:30-09:50) - Иностранный язык, п/г1, У507 | Структурное программирование, п/г2, У408\n• 2 пара (10:00-11:20) - Структурное программирование, п/г1, У408 | Иностранный язык, п/г2, У508\n• 3 пара (11:30-12:50) - История России (пр), А404\n• 4 пара (13:30-14:50) - Элективные дисциплины по физической культуре и спорту, С', 'Расписание на субботу:\n• 3 пара (11:30-12:50) - Базы данных, п/г1, А320\n• 4 пара (13:20-14:40) - Адаптивная верстка с использованием HTML5 и CSS3, п/г1, А320\n• ЭУК - Работа в команде (лек 32 ч)']
