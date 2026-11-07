from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery

from DB.requests import get_admins


class AdminAuthorization(BaseMiddleware):
    async def __call__(self, handler, event, data):
        user = event.from_user
        if user is not None and user.id in await get_admins():
            return await handler(event, data)
        if isinstance(event, CallbackQuery):
            await event.answer("Unauthorized access.", show_alert=True)
        else:
            await event.answer("Unauthorized access. Only for administrators.")
        return None
