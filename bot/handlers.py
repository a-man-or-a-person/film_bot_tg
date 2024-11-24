from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import bot.fsm_classes as fsm_cl
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


# Film deletion
@router.callback_query(F.data == 'delete_film_admin')
async def delete_film_admin_init(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(fsm_cl.Film_deletion.film_id)
    await callback_query.answer('Send film id')


@router.message(fsm_cl.Film_deletion.film_id)
async def delete_film_admin_get_id(message: Message, state: FSMContext):
    await state.update_data(film_id=message.text)
    data = await state.get_data()
    await rq.delete_film(**data)
    await message.reply('Film deleted')
    await state.clear()


# Film addition
@router.callback_query(F.data == 'add_film_admin')
async def add_film_admin_init(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(fsm_cl.Film_addition.name)
    await callback_query.answer('Send film name')


@router.message(fsm_cl.Film_addition.name)
async def add_film_admin_set_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(fsm_cl.Film_addition.description)
    await message.answer('Send film description')

@router.message(fsm_cl.Film_addition.description)
async def add_film_admin_set_desc(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(fsm_cl.Film_addition.genre)
    await message.answer('Send film genre')

@router.message(fsm_cl.Film_addition.genre)
async def add_film_admin_set_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await state.set_state(fsm_cl.Film_addition.source_film)
    await message.answer('Send film source')

@router.message(fsm_cl.Film_addition.source_film)
async def add_film_admin_set_film_source(message: Message, state: FSMContext):
    await state.update_data(source_film=message.text)
    await state.set_state(fsm_cl.Film_addition.source_trailer)
    await message.answer('Send trailer source')

@router.message(fsm_cl.Film_addition.source_trailer)
async def add_film_admin_set_trailer_source(message: Message, state: FSMContext):
    await state.update_data(source_trailer=message.text)
    await state.set_state(fsm_cl.Film_addition.year)
    await message.answer('Send film year')
@router.message(fsm_cl.Film_addition.year)
async def add_film_admin_set_year(message: Message, state: FSMContext):
    await state.update_data(year=message.text)
    await state.set_state(fsm_cl.Film_addition.age_limit)
    await message.answer('Send film age limit')

@router.message(fsm_cl.Film_addition.age_limit)
async def add_film_admin_set_age_limit(message: Message, state: FSMContext):
    await state.update_data(age_limit=message.text)
    data = await state.get_data()
    await rq.add_film(**data)
    await message.reply('Film added')
    await state.clear()