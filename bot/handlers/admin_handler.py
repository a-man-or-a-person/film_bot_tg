from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

import bot.fsm_classes as fsm_cl
import bot.keyboards.admin_keyboard as kb
import DB.requests as rq
import Pydantic.pydantic_validation as val
from bot.wrappers import AdminAuthorization

admin_router = Router()
admin_router.message.middleware(AdminAuthorization())
admin_router.callback_query.middleware(AdminAuthorization())


class Reg(StatesGroup):
    name = State()
    number = State()


@admin_router.message(Command("admin"))
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


@admin_router.callback_query(F.data == "get_admins_panel")
async def get_admins_params(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.edit_text(
        "Admins params", reply_markup=kb.admin_add_del_kb
    )


@admin_router.callback_query(F.data == "add_admin")
async def add_admin_1(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(fsm_cl.AdminAdd.admin_tg_id)
    await callback_query.message.answer("Send admin tg_id")


@admin_router.message(fsm_cl.AdminAdd.admin_tg_id)
async def add_admin_call(message: Message, state: FSMContext):
    await state.update_data(admin_tg_id=message.text)
    data = await state.get_data()

    ans = await val.add_admin_id_val(**data)
    await message.answer(ans)
    await state.clear()


@admin_router.callback_query(F.data == "del_admin")
async def add_admin_1(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(fsm_cl.AdminDel.admin_tg_id)
    await callback_query.message.answer("Send admin tg_id")


@admin_router.message(fsm_cl.AdminDel.admin_tg_id)
async def add_admin_call(message: Message, state: FSMContext):
    await state.update_data(admin_tg_id=message.text)
    data = await state.get_data()

    ans = await val.del_admin_id_val(**data)
    await message.answer(ans)
    await state.clear()


@admin_router.callback_query(F.data == "get_admins_ids")
async def get_all_admins(callback_query: CallbackQuery):
    admins = await rq.get_admins()
    ans = ""
    for num, id in enumerate(admins):
        ans += f"num:{num}\t tg_id: {id}\n"
    await callback_query.message.answer(ans)
