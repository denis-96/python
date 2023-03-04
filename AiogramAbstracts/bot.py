from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from os import getenv
from data_base import DataBase


async def on_startup(_):
    print('Бот активирован')


async def on_shutdown(_):
    dbase.close_db()
    print('Бот деактивирован')

storage = MemoryStorage()
dbase = DataBase()

bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)