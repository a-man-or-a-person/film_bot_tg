from pydantic import BaseModel, TypeAdapter, ValidationError

from DB.requests import add_film
from Pydantic.pydantic_valid_classes import Film


async def validate_film(**kwargs):
    try:
        film_val = TypeAdapter(Film)
        film = film_val.validate_python(kwargs)
        print(film)
        await add_film(**film)
    except ValidationError as e:
        print(e)
