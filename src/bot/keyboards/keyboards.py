from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
from aiogram.utils.keyboard import (
ReplyKeyboardMarkup, ReplyKeyboardBuilder, InlineKeyboardBuilder, InlineKeyboardMarkup, KeyboardButton,
InlineKeyboardButton
)



START = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Функции"), KeyboardButton(text="О нас"), KeyboardButton(text="Изменить группу")]],
    resize_keyboard=True
)

FUNCTIONS = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Свое расписание"), KeyboardButton(text="Расписание звонков")],
              [KeyboardButton(text="Узнать ФИО преподавателя"), KeyboardButton(text="Расписание преподавателя")],
              [KeyboardButton(text="Числитель / Знаменатель")]],
    resize_keyboard=True
)

WHAT_TT = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="На сегодня"), KeyboardButton(text="На завтра"), KeyboardButton(text="На неделю")]],
    resize_keyboard=True
)

BACK = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Назад")]], resize_keyboard=True
)

CONFIRM = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Да"), KeyboardButton(text="Нет")]], resize_keyboard=True
)



# def create_subjects(subjects: list):
#     SUBJECTS = ReplyKeyboardMarkup()
#
#     for subject in subjects:
#         SUBJECTS.row(text=subject)
#
#     return SUBJECTS.as_markup(resize_keyboard=True)

def create_subjects(subjects: list):
    SUBJECTS = InlineKeyboardBuilder()
    for subject in subjects:
        SUBJECTS.button(
            text=subject, callback_data=subject[:33]
        )
    SUBJECTS.adjust(1)
    return SUBJECTS.as_markup(resize_keyboard=True)