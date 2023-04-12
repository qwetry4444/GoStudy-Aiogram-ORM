""" This file represents a start logic """


from aiogram import Router, types
from aiogram.filters import Command

from src.language.translator import LocalizedTranslator
from src.bot.create_message import welcome_message
from src.messages import WELCOME_MESSAGE
from src.bot.keyboards.keyboards import START

help_router = Router(name="help")


@help_router.message(Command(commands="help"))
async def help(message: types.Message):
    """Help command handler"""
    await message.answer(welcome_message(message.from_user.first_name), reply_markup=START)
