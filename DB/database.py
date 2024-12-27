import os
import pathlib

from dotenv import load_dotenv
from sqlalchemy import String, create_engine
from sqlalchemy.ext.asyncio import (AsyncAttrs, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from typing_extensions import Annotated

from DB.link_creation import connection_link

load_dotenv()
if os.getenv("SELECTED_DB") == "POSTGRES":
    async_engine = create_async_engine(
        url=connection_link(),
        echo=True,
    )
else:
    path = pathlib.Path(r"DB\user.db").resolve()

    async_engine = create_async_engine(url=rf"sqlite+aiosqlite:///{path}", echo=True)

async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass
