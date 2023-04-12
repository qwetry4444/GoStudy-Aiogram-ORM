from aiogram.filters.state import StatesGroup, State


class States(StatesGroup):
    Ques_What_tt = State()
    Registration = State()
    Confirm = State()
    Get_Lecturer_tt = State()
    Change_user_group = State()
    Create_user = State()
    Get_Lecturer_name = State()