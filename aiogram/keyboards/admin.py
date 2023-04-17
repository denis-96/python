from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from bot import dbase

load_btn = KeyboardButton('/upload')
delete_btn = KeyboardButton('/delete')

admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
admin_kb.row(load_btn, delete_btn)


