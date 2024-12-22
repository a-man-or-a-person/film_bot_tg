from DB.requests import add_film
from pydantic import ValidationError
from Pydantic.pydantic_valid_classes import Film, FilmCode, ListFilms


async def validate_film(**kwargs):
    try:
        film = Film(**kwargs)
        await add_film(**film.dict())
        return 'film added'
    except ValidationError as e:
        return str(e)


async def get_film_by_code_validator(**kwargs):
    try:
        film_code = FilmCode(**kwargs)
        print(film_code)
        return "success"
        # Handler
    except ValidationError as e:
        print(e)
        return "Wrong film code"


async def films_sec_val(**kwargs):
    try:
        films = ListFilms(**kwargs)
        return films.films
    except ValidationError as e:
        print(e)
        return "Wrong film data"
