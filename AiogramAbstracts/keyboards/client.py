from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Обычные кнопки отправляют то, что на них написано
b1 = KeyboardButton('/open_hours')
b2 = KeyboardButton('/location')
b3 = KeyboardButton('/menu')

# Конпки исключения
# b4 = KeyboardButton('Отправить номер', request_contact=True)
# b5 = KeyboardButton('Отправить местоположение', request_location=True)



client_kb = ReplyKeyboardMarkup(resize_keyboard=True) #one_time_keyboard=True

client_kb.row(b1, b2, b3)
# client_kb.row(b4, b5)

# Способы добавления кнопок
# client_kb.add(b1).add(b2)  - добавляет каждую кнопку на новую строку
# client_kb.insert(b1)  - добавлят кнопку в ту же строку
# client_kb.row(b1, b2, b3)  - добавляет указанные кнопки в одну строку

