import os
from aiogram import executor
from dispatcher import dp
import handlers
from db import BotDB
os.chdir(os.path.dirname(os.path.realpath(__file__)))
BotDB = BotDB('db.sql')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)