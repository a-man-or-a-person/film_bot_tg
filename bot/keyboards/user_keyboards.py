from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

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
        [KeyboardButton(text="РАНДОМНЫЙ ФИЛЬМ"), KeyboardButton(text="ЛУЧШИЕ")],
        [KeyboardButton(text="⬅️Назад")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите раздел",
)
