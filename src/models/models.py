from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), index=True)
    last_name: Mapped[str] = mapped_column(String(50), index=True)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    email: Mapped[str] = mapped_column(String(50))
    birthday: Mapped[str] = mapped_column(String(10), nullable=True, default=None)
    addition: Mapped[str] = mapped_column(String(250), nullable=True)
