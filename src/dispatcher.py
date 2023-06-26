import logging
from aiogram import Bot, Dispatcher
from filters import IsOwnerFilter, IsAdminFilter, MemberCanRestrictFilter
from dotenv import dotenv_values

logging.basicConfig(level=logging.INFO)

config = dotenv_values('.env')
if not config["TOKEN"]:
    exit("No Token Provided.")

bot = Bot(token=config["TOKEN"], parse_mode="HTML")
dp = Dispatcher(bot)

dp.filters_factory.bind(IsOwnerFilter)
dp.filters_factory.bind(IsAdminFilter)
dp.filters_factory.bind(MemberCanRestrictFilter)