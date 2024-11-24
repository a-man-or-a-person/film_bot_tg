import asyncio
import os
import dotenv
import aiogram
import logging

from aiogram import Bot, Dispatcher

from bot.handlers import router

dotenv.load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")