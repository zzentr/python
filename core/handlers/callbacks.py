from aiogram import F, Router
from aiogram.types import CallbackQuery

from core.database import requests as rq
from core.keyboards import inline


router = Router()


@router.callback_query(F.data.startswith('task_'))
async def rem_task(callback: CallbackQuery):
    await rq.remove_task(callback.data.split('_')[1])
    markup = await inline.tasks(callback.from_user.id)
    if markup:
        await callback.answer('вы выполнили задачу')
        await callback.message.edit_text('молодец, осталось еще немного!', 
                                        reply_markup=markup)
        return
    await callback.message.edit_text('🎉 кажется все задачи выполнены, поздравляю!!! 🎉')