from DB.requests import add_film
from pydantic import BaseModel, TypeAdapter, ValidationError
from Pydantic.pydantic_valid_classes import Film, FilmCode


async def validate_film(**kwargs):
    try:
        film_val = TypeAdapter(Film)
        film = film_val.validate_python(kwargs)
        print(film)
        await add_film(**film)
    except ValidationError as e:
        print(e)


async def get_film_by_code_validator(**kwargs):
    try:
        film_code = FilmCode(**kwargs)
        print(film_code)
        return 'success'
        # Handler
    except ValidationError as e:
        print(e)
        return 'Wrong film code'
