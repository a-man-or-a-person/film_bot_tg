from sqlalchemy import create_engine, String
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from typing_extensions import Annotated
import pathlib

# sync_engine = create_engine(
#     url='sqlite:///user.db',
#     echo=True
# )
path = pathlib.Path(r'DB\user.db').resolve()
# path = pathlib.Path(r'user.db').resolve()
print(path)
async_engine = create_async_engine(
    url=fr'sqlite+aiosqlite:///{path}',
    echo=False
)

async_session_factory = async_sessionmaker(async_engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass
