import os

from dotenv import load_dotenv

# Admin checker


def admin_authentication(func):
    async def wrapper(message):
        load_dotenv()
        if str(message.from_user.id) in os.getenv(
            "ADMIN"
        ):  # Replace with your Telegram user ID
            return await func(message)
        return await message.reply(
            "Unauthorized access. Only for administrators.", reply=False
        )

    return wrapper
