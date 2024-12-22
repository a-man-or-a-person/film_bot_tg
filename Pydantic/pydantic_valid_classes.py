from typing_extensions import TypedDict

from pydantic import BaseModel, Field, TypeAdapter, ValidationError, validator


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


class FilmRating(BaseModel):
    kp: float
    imdb: float
    filmCritics: float


class FilmGenres(BaseModel):
    genre: str = Field(alias="name")


class APIKinoposikMovie(BaseModel):
    id: int
    name: str
    year: int
    description: str
    shortDescription: str
    rating: FilmRating
    ageRating: int
    genres: list[FilmGenres]

    @validator("description", *["shortDescription"])
    def transfirm_description(cls, value):
        return value.replace("\xa0", " ")


class ListFilms(BaseModel):
    films: list[APIKinoposikMovie] = Field(alias="docs")
