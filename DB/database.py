from sqlalchemy import create_engine, String
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from typing_extensions import Annotated

# sync_engine = create_engine(
#     url='sqlite:///user.db',
#     echo=True
# )

async_engine = create_async_engine(
    url='sqlite+aiosqlite:///user.db',
    echo=True
)

async_session_factory = async_sessionmaker(async_engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass
