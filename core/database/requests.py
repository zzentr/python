from sqlalchemy import select

from core.database.models import Task, async_session


async def set_task(tg_id, task):
    async with async_session() as session:
        task = Task(task=task, tg_id=tg_id)
        session.add(task)
        await session.commit()


async def get_tasks(tg_id):
    async with async_session() as session:
        result = await session.scalars(select(Task).where(Task.tg_id==tg_id))
        return result.all()
    

async def remove_task(id):
    async with async_session() as session:
        task = await session.scalar(select(Task).where(Task.id == int(id)))
        await session.delete(task)
        await session.commit()