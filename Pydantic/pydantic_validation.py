import DB.requests as rq
from pydantic import ValidationError
from Pydantic.pydantic_valid_classes import (AdminAddDelModel, Film, FilmCode,
                                             ListFilms)


async def validate_film(**kwargs):
    try:
        film = Film(**kwargs)
        await rq.add_film(**film.dict())
        return "film added"
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


async def del_admin_id_val(**kwargs) -> str:
    try:
        admin_id = AdminAddDelModel(**kwargs)
        await rq.del_admin(admin_id.admin_tg_id)
        return "success"
    except ValidationError as e:
        print(e)
        return "Something went wrong"


async def add_admin_id_val(**kwargs) -> str:
    try:
        admin_id = AdminAddDelModel(**kwargs)
        await rq.add_admin(admin_id.admin_tg_id)
        return "success"
    except ValidationError as e:
        print(e)
        return "Something went wrong"
