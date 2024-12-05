from sqlalchemy import String, ForeignKey, BigInteger
from sqlalchemy.orm import mapped_column, Mapped
from typing_extensions import Annotated
import datetime

from DB.database import Base

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
created_at = Annotated[
    datetime.datetime, mapped_column(default=datetime.datetime.utcnow())
]


class UserOrm(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    tg_id = mapped_column(BigInteger, unique=True)
    user_name: Mapped[str] = mapped_column(String(255), nullable=True)
    password: Mapped[str | None]
    age: Mapped[int | None]
    created_at: Mapped[created_at]


class FilmOrm(Base):
    __tablename__ = "films"

    film_id: Mapped[intpk]
    name: Mapped[str]
    description: Mapped[str | None]
    genre: Mapped[str | None]
    source_film: Mapped[str]
    source_trailer: Mapped[str | None]
    year: Mapped[int | None]
    age_limit: Mapped[int | None]
    created_at: Mapped[created_at]


class FavoriteOrm(Base):
    __tablename__ = "favorites"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.tg_id"))
    film_id: Mapped[int] = mapped_column(ForeignKey("films.film_id"))


class AdminOrm(Base):
    __tablename__ = "admins"

    id: Mapped[intpk]
    tg_id = mapped_column(BigInteger, unique=True)
