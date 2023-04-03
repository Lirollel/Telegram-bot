import logging
logging.basicConfig(level=logging.INFO)

from aiogram import executor
from create_bot import dp

from files.commands import keyboard_commands
from files.commands import message_commands

keyboard_commands.register_files_keyboard_commands(dp)
message_commands.register_files_message_commands(dp)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
