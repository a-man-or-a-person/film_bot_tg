from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

import bot.fsm_classes as fsm_cl
import bot.keyboards.admin_keyboard as kb
import DB.requests as rq
from bot.wrappers import admin_authentication

admin_router = Router()


class Reg(StatesGroup):
    name = State()
    number = State()


@admin_router.message(CommandStart())
async def start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.reply(f"Set user func is working, {message.from_user.id}")


@admin_router.message(Command("admin"))
@admin_authentication
async def admin_panel(message: Message):
    # Use middleware to check if it is admin
    await message.reply("Admin panel", reply_markup=kb.admin_panel)


@admin_router.callback_query(F.data == "get_statistics_admin")
async def get_statistics_admin(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        "Statistics", reply_markup=kb.admin_statistics
    )


@admin_router.callback_query(F.data == "get_films_admin")
async def get_statistics_admin(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("Films editor", reply_markup=kb.admin_films)


@admin_router.callback_query(F.data == "main_menu_admin")
async def get_statistics_admin(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("Admin panel", reply_markup=kb.admin_panel)
