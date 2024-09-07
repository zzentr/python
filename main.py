from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from asyncio import run
import os
load_dotenv()

from core.handlers import commands, text, callbacks
from core.database.models import async_main


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

async def main():
    dp.include_routers(commands.router, text.router, callbacks.router)
    await async_main()
    await dp.start_polling(bot)


if __name__ == '__main__':
    run(main())