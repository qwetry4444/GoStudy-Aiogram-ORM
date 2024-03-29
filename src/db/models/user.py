""" User model file """
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped, mapped_column

from src.bot.structures.role import Role

from ...language.enums import Locales
from .base import Base
from .chat import Chat


class User(Base):
    """
    User model
    """

    id: Mapped[int] = mapped_column(sa.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(sa.BigInteger, unique=True, nullable=False)
    """ Telegram user id """
    user_name: Mapped[str] = mapped_column(sa.VARCHAR(32), unique=False, nullable=False)
    """ Telegram user name """
    group_number: Mapped[str] = mapped_column(sa.VARCHAR(10), unique=False, nullable=False)

