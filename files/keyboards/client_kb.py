from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Кнопки "Помощь"
button_h1= KeyboardButton('Последнее сообщение')
button_h2= KeyboardButton('Список последних сообщений')
button_h3= KeyboardButton('Изменить частоту')
button_h4= KeyboardButton('Переводчик')

kb_hello = ReplyKeyboardMarkup(resize_keyboard=True)
kb_hello.add (button_h1).add(button_h2).row (button_h3, button_h4)

#Кнопки изменения частоты
button_fr = KeyboardButton('Чаще')
button_fd = KeyboardButton('Реже')
button_fe = KeyboardButton('Назад')

kb_frequency = ReplyKeyboardMarkup(resize_keyboard=True)
kb_frequency.row(button_fr, button_fd).add(button_fe)

#Кнопки последних сообщений
button_lmd = KeyboardButton('День')
button_lmw = KeyboardButton('Неделю')
button_lmm = KeyboardButton('Месяц')
button_lmhy = KeyboardButton('Полгода')
button_lmy = KeyboardButton('Год')
button_lme = KeyboardButton('Назад')

kb_last_messages = ReplyKeyboardMarkup(resize_keyboard=True)
kb_last_messages.row(button_lmd, button_lmw, button_lmm).row(button_lmhy, button_lmy).add(button_lme)