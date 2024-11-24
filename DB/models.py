from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from typing_extensions import Annotated

from DB.database import Base

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class UsersOrm(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    user_name: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str | None]
    age: Mapped[int | None]


class FilmsOrm(Base):
    __tablename__ = 'films'

    film_id: Mapped[intpk]
    name: Mapped[str]
    description: Mapped[str | None]
    genre: Mapped[str | None]
    source_film: Mapped[str]
    source_trailer: Mapped[str | None]
    year: Mapped[int | None]
    age_limit: Mapped[int | None]


class FavoritesOrm(Base):
    __tablename__ = 'favorites'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    film_id: Mapped[int] = mapped_column(ForeignKey('films.film_id'))

