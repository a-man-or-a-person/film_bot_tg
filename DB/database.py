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
        echo=False,
    )
else:
    path = pathlib.Path(os.getenv("DB_PATH", ".data/user.db")).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)

    async_engine = create_async_engine(url=rf"sqlite+aiosqlite:///{path}", echo=False)

async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass
