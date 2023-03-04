from aiogram import types
from bot import bot, dp, dbase
from keyboards import client_kb



# Клиентская часть
# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет\nМои команды: /help , /open_hours , /location', reply_markup=client_kb)

    except Exception as e:
        print(e)
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/AiogramTrainingBot')

# @dp.message_handler(commands=['open_hours'])
async def schedule(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 9:00 до 22:00, Сб-Вс c 10:00 до 20:00')

    

# @dp.message_handler(commands=['location'])
async def location(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная 15') #reply_markup=types.ReplyKeyboardRemove()

    
    
async def menu(message: types.Message):
    products = dbase.get_products()
    for product in products:
        await bot.send_photo(message.from_user.id, product[0], 
                             f'{product[1]}\nОписание:\n{product[2]}\nЦена: {product[3]}')

def register_handlers():
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(schedule, commands=['open_hours'])
    dp.register_message_handler(location, commands=['location'])
    dp.register_message_handler(menu, commands=['menu'])
    