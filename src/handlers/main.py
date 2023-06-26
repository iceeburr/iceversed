import time
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dispatcher import dp
from bot import BotDB

@dp.message_handler(commands=['start'])
async def start(message: types.message):
    if (not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id)

        inlinekeyboard = InlineKeyboardMarkup(resize_keyboard=True)
        inlinebutton1 = InlineKeyboardButton(text='Русский 🇷🇺', callback_data='firstru')
        inlinebutton2 = InlineKeyboardButton(text='English 🇺🇸', callback_data='firsten')
        inlinekeyboard.row(inlinebutton1, inlinebutton2)
        await message.bot.send_message(message.chat.id, text='Выберите язык перевода по умолчанию.\nChoose the default language.', reply_markup=inlinekeyboard)
    else:
        defaultLanguage = BotDB.get_Language(message.from_user.id)
        if defaultLanguage == "en":
            inlinekeyboard = InlineKeyboardMarkup(resize_keyboard=True)
            inlinebutton1 = InlineKeyboardButton(text='Settings ⚙️', callback_data='settings')
            inlinekeyboard.row(inlinebutton1)
            await message.bot.send_photo(message.chat.id, open('./assets/start.png', 'rb'), 'Welcome to my bot!\nHere you can find out more about me. Click the buttons below!', reply_markup=inlinekeyboard)
        elif defaultLanguage == "ru":
            inlinekeyboard = InlineKeyboardMarkup(resize_keyboard=True)
            inlinebutton1 = InlineKeyboardButton(text='Настройки ⚙️', callback_data='settings')
            inlinekeyboard.row(inlinebutton1)
            await message.bot.send_photo(message.chat.id, open('./assets/start.png', 'rb'), 'Добро пожаловать на моего бота!\nЗдесь ты сможеть узнать больше обо мне. Жми на кнопки ниже!', reply_markup=inlinekeyboard)
    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)