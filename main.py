import asyncio
import logging
import os

import dotenv
from aiogram import Bot, Dispatcher

from bot.handlers.admin_handler import router
from bot.handlers.user_handler import user_router


async def main():
    dotenv.load_dotenv()
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()

    dp.include_router(router)
    dp.include_router()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")
