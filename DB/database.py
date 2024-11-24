from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from typing_extensions import Annotated

sync_engine = create_engine(
    url='sqlite:///user.db',
    echo=True
)

session_factory = sessionmaker(sync_engine)

str_256 = Annotated[str, 256]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }
