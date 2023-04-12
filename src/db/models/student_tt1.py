""" User model file """
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped, mapped_column

from src.bot.structures.role import Role

from ...language.enums import Locales
from .base import Base
from .chat import Chat


class Student_tt1(Base):
    """
    Lecturer_timetable model
    """

    id: Mapped[int] = mapped_column(sa.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    group_number: Mapped[str] = mapped_column(sa.VARCHAR(10), unique=False, nullable=False)

    period_number: Mapped[int] = mapped_column(sa.Integer, unique=False, nullable=False)

    monday_subject: Mapped[str] = mapped_column(sa.VARCHAR(128))
    monday_class: Mapped[str] = mapped_column(sa.VARCHAR(20))

    tuesday_subject: Mapped[str] = mapped_column(sa.VARCHAR(128))
    tuesday_class: Mapped[str] = mapped_column(sa.VARCHAR(20))

    wednesday_subject: Mapped[str] = mapped_column(sa.VARCHAR(128))
    wednesday_class: Mapped[str] = mapped_column(sa.VARCHAR(20))

    thursday_subject: Mapped[str] = mapped_column(sa.VARCHAR(128))
    thursday_class: Mapped[str] = mapped_column(sa.VARCHAR(20))

    friday_subject: Mapped[str] = mapped_column(sa.VARCHAR(128))
    friday_class: Mapped[str] = mapped_column(sa.VARCHAR(20))

    saturday_subject: Mapped[str] = mapped_column(sa.VARCHAR(128))
    saturday_class: Mapped[str] = mapped_column(sa.VARCHAR(20))
