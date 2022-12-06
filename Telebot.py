# импортируем библиотеку
import telebot


# задаём токен своего бота
token = '5767999922:AAGbEz9x_zPp0UCfovxfpH6AvsgwVGH30wU'


# создаём объект класса TeleBot
bot = telebot.TeleBot(token)


# задаём обработчик @bot.message_handler()

@bot.message_handler(commands=['start'])

# фильтры обработчика:
# (commands= ['команда']) - проверка на ввод определённой команды
# (func= lambda message: message.text == 'слово') - проверка на ввод определённого слова
# (chat_types= ['тип чата']) - проверка на тип чата (privat, group, supergroup)
# (content_types= ['тип контента']) - проверка на тип отправляемого контента (text, photo, video)

def start(message):

    # bot.send_message(id чата, сообщение которое нужно отправить) - отправка сообщения
    # bot.reply_to(message, сообщение которое нужно отправить) - ответ на сообщение
    bot.send_message(message.chat.id, 'Привет')

# объект message хранит в себе много информации, самое важное:
# id чата (message.chat.id)
# id пользователя (message.from_user.id)
# текст сообщения (message.text)
# время сообщения, время unix (message.date)

# можно усложнить проверку обработчика:
# например перечислить фильтры через запятую
# @bot.message_handler(chat_types= ['privat'], content_types= ['text']) - логическое И (and)

# использовать два обработчика друг на друге
# @bot.message_handler(chat_types= ['privat']) - логическое ИЛИ (or)
# @bot.message_handler(commands= ['start'])


# ОТПРАВКА ФАЙЛА

@bot.message_handler(commands=['file'])

def f(message):

    # open('путь к файлу', 'параметр открытия')
    file = open('D:\photo.png', 'rb')
    # (id чата, файл, сообщение под фото(необязательно))
    bot.send_photo(message.chat.id, file, 'Привет')
    # bot.send_video() - отправить видео (сообщение под видео отправить не получится)

# второй способ отправки фото (через ссылку)

@bot.message_handler(commands=['photo'])

def photo(message):

    # (id чата, r'ссылка на фото')
    bot.send_photo(
        message.chat.id, r'https://cliply.co/wp-content/uploads/2021/08/472108440_HELLO_STICKER_400.png', 'Hello')


# ФОРМАТИРОВАНИЕ ТЕКСТА

@bot.message_handler(commands=['format'])

def format(message):
    
    bot.send_message(
        message.chat.id, '<b>форматированный</b> <i>текст</i>', parse_mode='HTML')
    #bot.send_message(message.chat.id, '*форматированный* _текст_', parse_mode='Markdown')
    # pars_mode=''  -  специальный пареметр для форматирования
    # для HTML <b>текст</b> - жирный, <i>текст</i> - курсив
    # для Markdown *текст* - жирный, _текст_ - курсив


# включаем постоянный запрос
bot.polling()
