""" User model file """
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped, mapped_column

from src.bot.structures.role import Role

from ...language.enums import Locales
from .base import Base
from .chat import Chat


class Student_tt(Base):
    """
    User model
    """

    id: Mapped[int] = mapped_column(sa.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    group_number: Mapped[str] = mapped_column(sa.VARCHAR(10), unique=False, nullable=False)
    """ Telegram user id """
    weekday: Mapped[str] = mapped_column(sa.VARCHAR(10), unique=False, nullable=False)
    """ Telegram user name """
    timetable: Mapped[str] = mapped_column(sa.VARCHAR(2000), unique=False, nullable=False)

