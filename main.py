from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import hello

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

async def main():
    print("🚀Запуск")
    bot = Bot(token=TOKEN)
    
    dp.include_router(hello.router)
    
   

    await dp.start_polling(bot)

try:
    if __name__ == "__main__":
        asyncio.run(main())

except KeyboardInterrupt:
        print("❌Бот выключен")