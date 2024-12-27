import os

from dotenv import load_dotenv

from DB.requests import get_admins

# Admin checker


def admin_authentication(func):
    async def wrapper(message):
        load_dotenv()
        if message.from_user.id in await get_admins():
            return await func(message)
        return await message.reply(
            "Unauthorized access. Only for administrators.", reply=False
        )

    return wrapper
