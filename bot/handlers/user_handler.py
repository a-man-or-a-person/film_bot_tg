import os
import random

import aiohttp
from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
from dotenv import load_dotenv

import bot.fsm_classes as fsm_cl
import bot.keyboards.user_keyboards as kb
import DB.requests as rq
import Pydantic.pydantic_validation as pd_val
from apis.kinopoisk import get_best_films, get_random_films

load_dotenv()

KINOPOISK_API_KEY = os.getenv("KINOPOISK_API_KEY")


# KINOPOISK_API_KEY = '296e88f6-55f1-4f99-9bf4-8d93375773fd'


# class UserStates(StatesGroup):
#     MAIN_MENU = State()
#     FILM_CODE = State()


user_router = Router()


@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer(
        f"Приветствуем вас в нашем КиноБоте! {message.from_user.first_name}",
        reply_markup=kb.main,
    )


@user_router.message(F.text == "ФИЛЬМЫ")
async def show_recommendations_menu(message: Message, state: FSMContext):
    await message.answer("Выберите тип рекомендаций:", reply_markup=kb.code_film_menu)


@user_router.message(F.text == "⬅️Назад")
async def back_to_main_menu(message: Message, state: FSMContext):
    await message.answer("Вы вернулись в главное меню.", reply_markup=kb.main)


@user_router.message(F.text == "ПОДДЕРЖКА")
async def support(message: Message):
    await message.answer(f"По всем вопросам и предложениям пишите: @Smt_good, @fucject")


@user_router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("Эта команда /help")


@user_router.message(F.text == "КОД ФИЛЬМА")
async def get_film_code_from_user(message: Message, state: FSMContext):
    await message.answer("Отправьте код фильма")
    await state.set_state(fsm_cl.FilmCode.film_id)


@user_router.message(fsm_cl.FilmCode.film_id)
async def get_film_code(message: Message, state: FSMContext):
    await state.update_data(film_id=message.text)
    data = await state.get_data()
    a = await pd_val.get_film_by_code_validator(**data)
    await message.reply(a)
    await state.clear()


@user_router.message(F.text == "ЛУЧШИЕ")
async def random_movie(message: Message):
    films = await get_best_films()
    for film in films:
        await message.answer_photo(str(film.poster), caption=film.description)


@user_router.message(F.text == "РАНДОМНЫЙ ФИЛЬМ")
async def random_movie(message: Message):
    films = await get_random_films()
    for film in films:
        await message.answer_photo(str(film.poster), caption=film.description)
