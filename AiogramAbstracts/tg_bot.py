from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

# Клиентская часть
@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Приятного аппетита')



@dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == 'Hello':
        await message.answer('И тебе привет')
    # await message.answer(message.text)  # присылает сообщение оправителю 
    # await message.reply(message.text)  # отвечает на сообщение отправитлея
    # await bot.send_message(message.from_user.id, message.text)  # оптравляет сообщение пользователю с указанным id


executor.start_polling(dp, skip_updates=True)