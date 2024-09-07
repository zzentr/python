from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('добрый день! я помогу вам незабывать важные дела, просто напишите задачу,'
                          ' а я запомню её и покажу ваш список дел')
    
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('отправьте мне задачу, я сохраню её чтобы вы не забыли! 😁')
