from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="КОД ФИЛЬМА"), KeyboardButton(text="ФИЛЬМЫ")],
        [KeyboardButton(text="ПОДДЕРЖКА")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Лучшие фильмы только тут",
)

code_film_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="РАНДОМНЫЙ ФИЛЬМ"), KeyboardButton(text="ЛУЧШИЕ СЕГОДНЯ")],
        [KeyboardButton(text="⬅️Назад")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите раздел",
)
