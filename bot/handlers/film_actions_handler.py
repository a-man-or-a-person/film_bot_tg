from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from Pydantic import pydantic_valid_classes as pyd_val

import bot.fsm_classes as fsm_cl
import DB.requests as rq
from Pydantic.pydantic_validation import validate_film

film_router = Router()


# Film deletion
@film_router.callback_query(F.data == "delete_film_admin")
async def delete_film_admin_init(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(fsm_cl.Film_deletion.film_id)
    await callback_query.answer("Send film id")


@film_router.message(fsm_cl.Film_deletion.film_id)
async def delete_film_admin_get_id(message: Message, state: FSMContext):
    await state.update_data(film_id=message.text)
    data = await state.get_data()
    await rq.delete_film(**data)
    await message.reply("Film deleted")
    await state.clear()


# Film addition
@film_router.callback_query(F.data == "add_film_admin")
async def add_film_admin_init(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(fsm_cl.Film_addition.name)
    await callback_query.answer("Send film name")


@film_router.message(fsm_cl.Film_addition.name)
async def add_film_admin_set_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(fsm_cl.Film_addition.description)
    await message.answer("Send film description")


@film_router.message(fsm_cl.Film_addition.description)
async def add_film_admin_set_desc(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(fsm_cl.Film_addition.genre)
    await message.answer("Send film genre")


@film_router.message(fsm_cl.Film_addition.genre)
async def add_film_admin_set_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await state.set_state(fsm_cl.Film_addition.source_film)
    await message.answer("Send film source")


@film_router.message(fsm_cl.Film_addition.source_film)
async def add_film_admin_set_film_source(message: Message, state: FSMContext):
    await state.update_data(source_film=message.text)
    await state.set_state(fsm_cl.Film_addition.source_trailer)
    await message.answer("Send trailer source")


@film_router.message(fsm_cl.Film_addition.source_trailer)
async def add_film_admin_set_trailer_source(message: Message, state: FSMContext):
    await state.update_data(source_trailer=message.text)
    await state.set_state(fsm_cl.Film_addition.year)
    await message.answer("Send film year")


@film_router.message(fsm_cl.Film_addition.year)
async def add_film_admin_set_year(message: Message, state: FSMContext):
    await state.update_data(year=message.text)
    await state.set_state(fsm_cl.Film_addition.age_limit)
    await message.answer("Send film age limit")


@film_router.message(fsm_cl.Film_addition.age_limit)
async def add_film_admin_set_age_limit(message: Message, state: FSMContext):
    await state.update_data(age_limit=message.text)
    data = await state.get_data()

    await validate_film(**data)
    await message.reply("Film added")
    await state.clear()
