from DB.orm import create_tables
import asyncio
import logging
import os

import dotenv
from aiogram import Bot, Dispatcher

from bot.handlers.admin_handler import admin_router
from bot.handlers.film_actions_handler import film_router
from bot.handlers.user_handler import user_router


async def main():
    dotenv.load_dotenv()
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    await create_tables()
    dp = Dispatcher()

    dp.include_router(admin_router)
    dp.include_router(user_router)
    dp.include_router(film_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")
