from aiogram import Router
from aiogram.filters import Command
from aiogram import types as t

router = Router()


@router.message(Command("start"))
async def start_handler(message: t.Message):
    text = "Hello World!"
    await message.answer(text=text)
