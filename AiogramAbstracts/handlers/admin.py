from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from bot import bot, dp, dbase
from keyboards import admin_kb


ID = None

# Админская часть
class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()
    

# Получаем ID текущего модератора
# @dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что надо, хозяин?', reply_markup=admin_kb)
    await message.delete()


# Начало диалога загрузки нового пункта меню
# @dp.message_handler(commands=['download'], state=None)
async def on_add(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузите фото', reply_markup=ReplyKeyboardRemove())
        
        
# @dp.message_handler(commands=['delete'], state=None)
async def on_delete(message: types.Message):
    if message.from_user.id == ID:
        admin_delete_kb = types.InlineKeyboardMarkup(row_width=3)
        for product in dbase.get_products():
            admin_delete_kb.insert(types.InlineKeyboardButton(text=product[1], callback_data=f'product-{product[1]}'))
        await message.answer('Выберите товар: ', reply_markup=admin_delete_kb)


# @dp.callback_query_handler(Text(startswith='product-'), state=None)
async def delete_product(callback: types.CallbackQuery):
    if callback.from_user.id == ID:
        product_name = callback.data.split('-')[1]
        dbase.delete_product(product_name)
        await callback.answer(f'Товар "{product_name}" удалён', show_alert=True)
        await callback.message.delete()


# Ловим первый ответ и пишем в словарь
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Теперь введите название')


# Ловим второй ответ
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Добавьте описание')


# Ловим третий ответ
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Укажите цену')
    

# Ловим четвёртый овтет
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    try:
        price = float(message.text)
    except:
        await message.reply('Цена должна быть в виде числа')
    else:
        async with state.proxy() as data:
            data['price'] = price
        await dbase.add_product(state)
        await state.finish()
        await message.answer('Добавлено успешно')


# @dp.message_handler(state='*', commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK', reply_markup=admin_kb)


def register_handlers():
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(on_add, commands=['upload'], state=None)
    dp.register_message_handler(on_delete, commands=['delete'], state=None)
    dp.register_callback_query_handler(delete_product, Text(startswith='product-'), state=None)
    dp.register_message_handler(cancel_handler, state='*', commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    
    