from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import bot.keyboard as kb
import DB.requests as rq

router = Router()


class Reg(StatesGroup):
    name = State()
    number = State()


@router.message(CommandStart())
async def start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.reply("Set user func is working")


@router.message(Command('admin'))
async def admin_panel(message: Message):
    # Use middleware to check if it is admin
    await message.reply("Admin panel", reply_markup=kb.admin_panel)


@router.callback_query(F.data == 'get_statistics_admin')
async def get_statistics_admin(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("Statistics", reply_markup=kb.admin_statistics)


@router.callback_query(F.data == 'get_films_admin')
async def get_statistics_admin(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("Films editor", reply_markup=kb.admin_films)


@router.callback_query(F.data == 'main_menu_admin')
async def get_statistics_admin(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("Admin panel", reply_markup=kb.admin_panel)