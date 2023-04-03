from create_bot import dp, bot
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
import time

def register_files_message_commands(dp:Dispatcher):
    dp.register_message_handler(process_message_command, Text(equals="Запуск"))


# Сообщение
async def process_message_command(message: types.Message):
    t=time.time()
    time.sleep(3)
    for i in range(0,10):
        await message.answer("Пора заниматься английским")
        t+=60



