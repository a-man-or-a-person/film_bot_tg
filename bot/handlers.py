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
    # await message.answer(f'Hello\nYour id is {message.from_user.id}\nYour name is {message.from_user.first_name}')
    await message.reply(
        f"Hello\nYour id is {message.from_user.id}\nYour name is {message.from_user.first_name}",
        reply_markup=kb.main,
    )


@router.message(Command("help"))
async def start(message: Message):
    await message.answer("Okay, ЦАО", reply_markup=kb.settings)


@router.message(F.text == "Bruh")
async def start(message: Message):
    await message.answer("fuck you")


@router.message(F.photo)
async def start(message: Message):
    await message.answer(f"ID foto: {message.photo[-1].file_id}")


@router.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAMMZ0Lum5oreuRUEZd5VWpA9JY2J0YAAnLpMRsk6BhKrPx3gnl4fTsBAAMCAAN5AAM2BA",
        caption="This is a photo",
    )


@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('Chose catalog')
    await callback.message.edit_text('Hello', reply_markup=await kb.inline_cars())


@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите ваше имя')


@router.message(Reg.name)
async def reg_second(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите ваш номер телефона')


@router.message(Reg.number)
async def reg_third(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f'Регистрация завершена!\n{data["name"], data["number"]}\n{data}')
    await state.clear()



