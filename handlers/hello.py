from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
router = Router()

@router.message(Command('hello'))
async def send_first_message(message: Message):
    await message.answer("Привет я тест бот для установки гита!")