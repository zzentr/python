from aiogram import F, Router
from aiogram.types import Message

from core.database import requests as rq
from core.keyboards import inline


router = Router()


@router.message(F.text)
async def add_task(message: Message):
    await rq.set_task(message.from_user.id, message.text)
    await message.answer('все ваши текущие задачи, выполните их быстрее!', 
                   reply_markup=await inline.tasks(message.from_user.id))
    
@router.message()
async def other(message: Message):
    await message.answer('и че это, задачу мне пришли')

