from aiogram.fsm.state import StatesGroup, State


class Film_deletion(StatesGroup):
    film_id = State()


class Film_addition(StatesGroup):
    name = State()
    description = State()
    genre = State()
    source_film = State()
    source_trailer = State()
    year = State()
    age_limit = State()
