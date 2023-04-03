from create_bot import dp, bot
from aiogram import types, Dispatcher
from files.keyboards.client_kb import kb_hello, kb_frequency, kb_last_messages
from aiogram.dispatcher.filters import Text


def register_files_keyboard_commands(dp:Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_frequency_command, Text(equals="Изменить частоту"))
    dp.register_message_handler(process_exit_command, Text(equals="Назад"))
    dp.register_message_handler(process_last_messages_command, Text(equals="Список последних сообщений"))


# Ответ на первую кнопку -> вызов кнопок помощи
async def process_start_command(message: types.Message):
    await message.reply("Hello!", reply_markup=kb_hello)

# Ответ на кнопку "Изменить частоту"
async def process_frequency_command(message: types.Message):
    await message.reply("Выбери желаемую частоту", reply_markup=kb_frequency)

# Ответ на кнопку "назад"
async def process_exit_command(message: types.Message):
    await message.reply("Теперь ты снова видишь мое основное меню", reply_markup=kb_hello)

# Ответ на кнопку "Список последних сообщений"
async def process_last_messages_command(message: types.Message):
    await message.reply("За какой период ты хочешь увидеть сообщения?", reply_markup=kb_last_messages)
