from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import  Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data_base import DataBase



bot = Bot('token')
dp = Dispatcher(bot)
dbase = DataBase()


# Кнопка ссылка
url_kb = InlineKeyboardMarkup(row_width=3)
url_btn1 = InlineKeyboardButton(text='Link 1', url='https://www.youtube.com/watch?v=gpCIfQUbYlY&list=PLNi5HdK6QEmX1OpHj0wvf8Z28NYoV5sBJ&index=9&ab_channel=PythonHubStudio')
url_btn2 = InlineKeyboardButton(text='link 2', url='https://www.youtube.com/watch?v=_r0vlyp33pw&ab_channel=dreamscape')
url_kb.row(url_btn1, url_btn2)

clb_kb = InlineKeyboardMarkup(row_width=2)
for product in dbase.get_products():
    clb_btn = InlineKeyboardButton(text=product[1], callback_data=f'product-{product[1]}')
    clb_kb.insert(clb_btn)

@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.reply('Здорово')


@dp.message_handler(commands=['links'])
async def command_start(message: types.Message):
    await message.answer('Links: ', reply_markup=url_kb)
    

@dp.message_handler(commands=['buttons'])
async def command_start(message: types.Message):
    await message.answer('Buttons: ', reply_markup=clb_kb)


@dp.callback_query_handler(lambda callback: callback.data.startswith('first_data'))
async def taxi(callback: types.CallbackQuery):
    await callback.message.answer('1')
    await callback.answer('1', show_alert=True)


@dp.callback_query_handler(Text(startswith='product-'))
async def taxi(callback: types.CallbackQuery):
    await callback.message.answer(f'Котик: {callback.data.split("-")[1]}')
    await callback.answer()


@dp.message_handler()
async def empty(message: types.Message):
    await message.reply('Нет такой команды')
    await message.delete()

async def on_shutdown(_):
    dbase.close_db()
    print('Бот деактивирован')
    
executor.start_polling(dp, skip_updates=True, on_shutdown=on_shutdown)
