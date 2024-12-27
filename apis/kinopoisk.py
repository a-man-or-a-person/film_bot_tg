import asyncio
import os
import random
import urllib.parse

import dotenv
import requests

from Pydantic.pydantic_valid_classes import APIKinopoiskMovie, KinopoiskFilmOut
from Pydantic.pydantic_validation import films_sec_val


async def get_films_by_params(**kwargs) -> list[APIKinopoiskMovie]:
    dotenv.load_dotenv()
    flattened_params = []
    for key, value in kwargs.items():
        if isinstance(value, list):
            for item in value:
                flattened_params.append((key, item))
        else:
            flattened_params.append((key, value))

    url = "https://api.kinopoisk.dev/v1.4/movie"
    url = f"{url}?{urllib.parse.urlencode(flattened_params)}"
    headers = {
        "accept": "application/json",
        "X-API-KEY": os.getenv("KINOPOISK_API_KEY"),
    }
    response = requests.get(url, headers=headers)
    data = await films_sec_val(**response.json())
    return data


async def get_random_films() -> list[KinopoiskFilmOut]:
    params = {
        "page": str(random.randint(1, 200)),
        "notNullFields": [
            "name",
            "shortDescription",
            "genres.name",
            "ageRating",
            "poster.url",
        ],
        "type": "movie",
        "limit": "5",
    }
    data = await get_films_by_params(**params)
    return await user_string_prep(data)


async def get_best_films() -> list[KinopoiskFilmOut]:
    params = {
        "page": str(random.randint(1, 50)),
        "notNullFields": [
            "name",
            "shortDescription",
            "genres.name",
            "ageRating",
            "poster.url",
        ],
        "type": "movie",
        "limit": "5",
        "rating.kp": "7.5-10",
        "rating.imdb": "7.5-10",
    }

    data = await get_films_by_params(**params)
    return await user_string_prep(data)


async def user_string_prep(films: list[APIKinopoiskMovie]) -> list[KinopoiskFilmOut]:
    output = []
    for film in films:
        film_desc = (
            f"Name: {film.name}\n"
            f"Description: {film.shortDescription}\n"
            f"Year: {film.year}\n"
            f"Age rating: {film.ageRating}\n"
            f"Rating:"
            f"\n\tkp:{round(film.rating.kp, 1)}"
            f"\n\timdb:{round(film.rating.imdb, 1)}\n"
            f'Genres: {", ".join([film.genre for film in film.genres])}'
        )
        film_desc += "\n\n"
        output.append(
            KinopoiskFilmOut(**{"poster": film.poster.url, "description": film_desc})
        )
    return output


async def main():
    pass


if __name__ == "__main__":
    asyncio.run(main())
