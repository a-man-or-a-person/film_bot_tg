from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)

admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Statistics", callback_data="get_statistics_admin")],
        [InlineKeyboardButton(text="Films", callback_data="get_films_admin")],
    ]
)
admin_statistics = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Under Construction", callback_data="https://www.wikipedia.org/"
            )
        ],
        [InlineKeyboardButton(text="Admin panel", callback_data="main_menu_admin")],
    ]
)

admin_films = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Add film", callback_data="add_film_admin"),
            InlineKeyboardButton(text="Delete film", callback_data="delete_film_admin"),
        ],
        [InlineKeyboardButton(text="Admin panel", callback_data="main_menu_admin")],
    ]
)
