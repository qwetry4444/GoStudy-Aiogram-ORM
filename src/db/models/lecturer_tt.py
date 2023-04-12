""" User model file """
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped, mapped_column

from src.bot.structures.role import Role

from ...language.enums import Locales
from .base import Base
from .chat import Chat


class Lecturer_tt(Base):
    """
    Lecturer_timetable model
    """

    id: Mapped[int] = mapped_column(sa.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    lecturer_name: Mapped[str] = mapped_column(sa.VARCHAR(40), unique=False, nullable=False)

    department: Mapped[int] = mapped_column(sa.Integer, unique=False, nullable=False, default=0)

    period_number: Mapped[int] = mapped_column(sa.Integer, unique=False, nullable=False)

    monday_group: Mapped[str] = mapped_column(sa.VARCHAR(70))
    monday_class: Mapped[str] = mapped_column(sa.VARCHAR(20))

    tuesday_group: Mapped[str] = mapped_column(sa.VARCHAR(70))
    tuesday_class: Mapped[str] = mapped_column(sa.VARCHAR(20))

    wednesday_group: Mapped[str] = mapped_column(sa.VARCHAR(70))
    wednesday_class: Mapped[str] = mapped_column(sa.VARCHAR(20))

    thursday_group: Mapped[str] = mapped_column(sa.VARCHAR(70))
    thursday_class: Mapped[str] = mapped_column(sa.VARCHAR(20))

    friday_group: Mapped[str] = mapped_column(sa.VARCHAR(70))
    friday_class: Mapped[str] = mapped_column(sa.VARCHAR(20))

    saturday_group: Mapped[str] = mapped_column(sa.VARCHAR(70))
    saturday_class: Mapped[str] = mapped_column(sa.VARCHAR(20))
