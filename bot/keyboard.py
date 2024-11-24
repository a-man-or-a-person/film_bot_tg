from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# main = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Catalog")],
#         [KeyboardButton(text="1"), KeyboardButton(text="2")],
#     ],
#     resize_keyboard=True,
#     input_field_placeholder="Choose smth in menu",
# )
main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Catalog", callback_data="catalog")],
        [
            InlineKeyboardButton(text="Basket", callback_data="basket"),
            InlineKeyboardButton(text="Contacts", callback_data="contacts"),
        ],
    ],
)

settings = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Wiki", url="https://www.wikipedia.org/")]
    ]
)

cars = ["Tesla", "BMW", "Honda", "VAS"]


async def reply_cars():
    keyboard = ReplyKeyboardBuilder()
    for car in cars:
        keyboard.add(KeyboardButton(text=car))
    return keyboard.adjust(2).as_markup()


async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url="https://www.wikipedia"))
    return keyboard.adjust(2).as_markup()
