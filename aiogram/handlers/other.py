from aiogram import types
from bot import dp
import json, string


# Общая часть
# @dp.message_handler()
async def other_messages(message: types.Message):
    if {word.lower().translate(str.maketrans('', '', string.punctuation)) for word in message.text.split()}\
        .intersection(json.load(open('cenz.json', encoding='utf-8'))):
        await message.reply('Маты запрещены')
        await message.delete()


def register_handlers():
    dp.register_message_handler(other_messages)