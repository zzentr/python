from sqlalchemy import BigInteger, String, Integer
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from dotenv import load_dotenv
import os
load_dotenv()


engine = create_async_engine(url=os.getenv('BD_URL'))
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)


class Task(Base):
    __tablename__ = 'tasks'

    id = mapped_column(Integer, primary_key=True)
    task = mapped_column(String)
    tg_id = mapped_column(BigInteger)


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        