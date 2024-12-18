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
import Pydantic.pydantic_validation as pd_val
import DB.requests as rq

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


@user_router.message(F.text == "РАНДОМНЫЙ ФИЛЬМ")
async def random_movie(message: Message):
    films = await rq.get_random_films(10)
    await message.answer(films)








@user_router.message(F.text == "РАНДОМНЫЙ ФИЛЬМ")
async def random_movie(message: Message):
    """
    Хэндлер для получения случайного фильма.
    """
    try:
        # Устанавливаем соединение с API
        async with aiohttp.ClientSession() as session:
            # Получаем случайную страницу для большего разнообразия
            random_page = random.randint(
                1, 20
            )  # Настраиваем количество страниц в диапазоне
            async with session.get(
                    "https://kinopoiskapiunofficial.tech/api/v2.2/films",
                    headers={"X-API-KEY": KINOPOISK_API_KEY},
                    params={"page": random_page, "order": "RANDOM", "type": "ALL"},
            ) as response:
                # Проверяем успешность запроса
                if response.status != 200:
                    await message.answer(
                        "Не удалось получить данные о фильмах. Попробуйте позже."
                    )
                    return

                # Парсим ответ
                data = await response.json()
                movies = data.get("items", [])
                if not movies:
                    await message.answer("Фильмы не найдены.")
                    return

                # Выбираем случайный фильм
                movie = random.choice(movies)
                title = movie.get("nameRu", "Без названия")
                year = movie.get("year", "Год неизвестен")
                rating = movie.get("ratingKinopoisk", "Рейтинг неизвестен")
                poster_url = movie.get("posterUrl", None)
                description = movie.get("description", "Описание отсутствует")

                # Отправляем данные пользователю
                if poster_url:
                    await message.answer_photo(
                        photo=poster_url,
                        caption=f"🎬 *{title}* ({year})\n⭐ Рейтинг: {rating}\n\n{description}",
                        pasre_mode="Markdown",
                    )
                else:
                    await message.answer(
                        f"🎬 *{title}* ({year})\n⭐ Рейтинг: {rating}\n\n{description}",
                        parse_mode="Markdown",
                    )
    except Exception as e:
        # Логируем и выводим сообщение об ошибке
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка. Попробуйте позже.")
