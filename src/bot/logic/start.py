""" This file represents a start logic """

from aiogram import Router, types
from aiogram.filters import CommandStart, Text
from aiogram.fsm.context import FSMContext

import src.messages as mes
from src.db.repositories.user import UserRepo
from src.bot.keyboards.keyboards import START
from src.bot.create_message import welcome_message
from sqlalchemy.orm import sessionmaker
from src.db.database import Database
from src.messages import REGISTRATION_MESSAGE
from src.bot.states import States

start_router = Router(name="start")


@start_router.message(CommandStart())
async def start(message: types.Message, db: Database, state: FSMContext):
    """Start command handler"""
    if await db.user.exist(tg_id=message.from_user.id):
        await message.answer(welcome_message(message.from_user.first_name), reply_markup=START)
        print('User exist')
    else:
        await message.answer(welcome_message(message.from_user.first_name))
        await message.answer(REGISTRATION_MESSAGE)
        await state.set_state(States.Create_user)


@start_router.message(Text, States.Create_user)
async def create_user(message: types.Message, db: Database, state: FSMContext):
    """Help command handler"""
    group = message.text
    if group in mes.groups:
        await db.user.new(tg_id=message.from_user.id, user_name=message.from_user.first_name,
                          group_number=group)
        await message.answer(mes.end_registration, reply_markup=START)
        await state.clear()
    else:
        await message.answer(mes.GROUP_NUMBER_FALL)
