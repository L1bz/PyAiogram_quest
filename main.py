import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart

from config import TOKEN


bot = Bot(token= TOKEN)
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

