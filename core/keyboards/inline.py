from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

from core.database import requests as rq


async def tasks(tg_id):
    keyboard = InlineKeyboardBuilder()
    all_tasks = await rq.get_tasks(tg_id)
    
    if all_tasks == []:
        return None

    for el in all_tasks:
        keyboard.add(InlineKeyboardButton(text=el.task, callback_data=f'task_{el.id}'))

    return keyboard.adjust(2).as_markup()