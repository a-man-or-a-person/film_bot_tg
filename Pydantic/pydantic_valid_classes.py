from pydantic import BaseModel, TypeAdapter, ValidationError
from typing_extensions import TypedDict


class Film(TypedDict):
    name: str
    description: str
    genre: str
    source_film: str
    source_trailer: str
    year: int
    age_limit: int


