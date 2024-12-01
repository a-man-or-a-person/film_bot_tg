import asyncio
import logging
from aiogram import Bot, Dispatcher #импорт классов
from config import TOKEN
from app.handlers import router

#создаем экземпляры классв от Bot и Dispatcher
bot = Bot(token=TOKEN) #инициализирует подключние к боту
dp = Dispatcher() #основной роутер, задача: обрабатывать входящие знач


async def main():

    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')