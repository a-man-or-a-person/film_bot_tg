from typing_extensions import TypedDict

from pydantic import BaseModel, TypeAdapter, ValidationError


class Film(TypedDict):
    name: str
    description: str
    genre: str
    source_film: str
    source_trailer: str
    year: int
    age_limit: int


class FilmCode(BaseModel):
    film_id: int
