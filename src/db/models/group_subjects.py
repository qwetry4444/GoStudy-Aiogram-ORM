import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped, mapped_column

from src.bot.structures.role import Role

from .base import Base



class Group_subjects(Base):
    id: Mapped[int] = mapped_column(sa.INTEGER, unique=True, nullable=False, primary_key=True)
    group_number: Mapped[str] = mapped_column(sa.VARCHAR(10), unique=True, nullable=False)
    subjects: Mapped[list] = mapped_column(sa.ARRAY(sa.VARCHAR(200)))


