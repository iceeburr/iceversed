import time
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dispatcher import dp
from bot import BotDB

@dp.callback_query_handler()
async def handler(callback: types.callback_query):
    if callback.data == "en":
        BotDB.set_language("en", callback.from_user.id)
        await callback.message.edit_text(text='Settings successfully changed! ✅')
        time.sleep(1)
        inlinekeyboard = InlineKeyboardMarkup(resize_keyboard=True)
        inlinebutton1 = InlineKeyboardButton(text='Language ❓', callback_data='language')
        inlinebutton2 = InlineKeyboardButton(text= 'Return back 🔙', callback_data='settingsreturn')
        inlinekeyboard.row(inlinebutton1)
        inlinekeyboard.row(inlinebutton2)
        return await callback.message.edit_text(text='Please pick an option below and I will tell you more about it.', reply_markup=inlinekeyboard)
    elif callback.data == "ru":
        BotDB.set_language("ru", callback.from_user.id)
        await callback.message.edit_text(text='Настройки успешно изменены! ✅')
        time.sleep(1)
        inlinekeyboard = InlineKeyboardMarkup(resize_keyboard=True)
        inlinebutton1 = InlineKeyboardButton(text='Язык ❓', callback_data='language')
        inlinebutton2 = InlineKeyboardButton(text= 'Вернуться назад 🔙', callback_data='settingsreturn')
        inlinekeyboard.row(inlinebutton1)
        inlinekeyboard.row(inlinebutton2)
        return await callback.message.edit_text(text='Пожалуйста, выберите позицию ниже, и я расскажу вам о ней подробнее.', reply_markup=inlinekeyboard)
    elif callback.data == "firsten":
        BotDB.set_language("en", callback.from_user.id)
        await callback.message.edit_text(text='Settings successfully changed! ✅')
        time.sleep(1)
        inlinekeyboard = InlineKeyboardMarkup(resize_keyboard=True)
        inlinebutton1 = InlineKeyboardButton(text='Settings ⚙️', callback_data='settings')
        inlinekeyboard.row(inlinebutton1)
        await callback.message.bot.send_photo(callback.message.chat.id, open('./assets/start.png', 'rb'), 'Welcome to my bot!\nHere you can find out more about me. Click the buttons below!', reply_markup=inlinekeyboard)
        return await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    elif callback.data == "firstru":
        BotDB.set_language("ru", callback.from_user.id)
        await callback.message.edit_text(text='Настройки успешно изменены! ✅')
        time.sleep(1)
        inlinekeyboard = InlineKeyboardMarkup(resize_keyboard=True)
        inlinebutton1 = InlineKeyboardButton(text='Настройки ⚙️', callback_data='settings')
        inlinekeyboard.row(inlinebutton1)
        await callback.message.bot.send_photo(callback.message.chat.id, open('./assets/start.png', 'rb'), 'Добро пожаловать на моего бота!\nЗдесь ты сможеть узнать больше обо мне. Жми на кнопки ниже!', reply_markup=inlinekeyboard)
        return await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    elif callback.data == "language":
        defaultLanguage = BotDB.get_Language(callback.from_user.id)
        if defaultLanguage == "en":
            inlinekeyboard = InlineKeyboardMarkup(resize_keyboard=True)
            inlinebutton1 = InlineKeyboardButton(text='Русский 🇷🇺', callback_data='ru')
            inlinebutton2 = InlineKeyboardButton(text='English 🇺🇸', callback_data='en')
            inlinebutton3 = InlineKeyboardButton(text= 'Return back 🔙', callback_data='languagereturn')
            inlinekeyboard.row(inlinebutton1, inlinebutton2)
            inlinekeyboard.row(inlinebutton3)
            return await callback.message.edit_text(text='Выберите язык перевода по умолчанию.\nChoose the default language.', reply_markup=inlinekeyboard)
        elif defaultLanguage == "ru":
            inlinekeyboard = InlineKeyboardMarkup(resize_keyboard=True)
            inlinebutton1 = InlineKeyboardButton(text='Русский 🇷🇺', callback_data='ru')
            inlinebutton2 = InlineKeyboardButton(text='English 🇺🇸', callback_data='en')
            inlinebutton3 = InlineKeyboardButton(text= 'Вернуться назад 🔙', callback_data='languagereturn')
            inlinekeyboard.row(inlinebutton1, inlinebutton2)
            inlinekeyboard.row(inlinebutton3)
            return await callback.message.edit_text(text='Выберите язык перевода по умолчанию.\nChoose the default language.', reply_markup=inlinekeyboard)
    elif callback.data == "languagereturn":
        defaultLanguage = BotDB.get_Language(callback.from_user.id)
        if defaultLanguage == "en":
            inlinekeyboard = InlineKeyboardMarkup(resize_keyboard=True)
            inlinebutton1 = InlineKeyboardButton(text='Language ❓', callback_data='language')
            inlinebutton2 = InlineKeyboardButton(text= 'Return back 🔙', callback_data='settingsreturn')
            inlinekeyboard.row(inlinebutton1)
            inlinekeyboard.row(inlinebutton2)
            return await callback.message.edit_text(text='Please pick an option below and I will tell you more about it.', reply_markup=inlinekeyboard)
        elif defaultLanguage == "ru":
            inlinekeyboard = InlineKeyboardMarkup(resize_keyboard=True)
            inlinebutton1 = InlineKeyboardButton(text='Язык ❓', callback_data='language')
            inlinebutton2 = InlineKeyboardButton(text= 'Вернуться назад 🔙', callback_data='settingsreturn')
            inlinekeyboard.row(inlinebutton1)
            inlinekeyboard.row(inlinebutton2)
            return await callback.message.edit_text(text='Пожалуйста, выберите позицию ниже, и я расскажу вам о ней подробнее.',reply_markup=inlinekeyboard)
    elif callback.data == "settingsreturn":
        defaultLanguage = BotDB.get_Language(callback.from_user.id)
        if defaultLanguage == "en":
            inlinekeyboard = InlineKeyboardMarkup(resize_keyboard=True)
            inlinebutton1 = InlineKeyboardButton(text='Settings ⚙️', callback_data='settings')
            inlinekeyboard.row(inlinebutton1)
            await callback.message.bot.send_photo(callback.message.chat.id, open('./assets/start.png', 'rb'), 'Welcome to my bot!\nHere you can find out more about me. Click the buttons below!', reply_markup=inlinekeyboard)
            return await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        elif defaultLanguage == "ru":
            inlinekeyboard = InlineKeyboardMarkup(resize_keyboard=True)
            inlinebutton1 = InlineKeyboardButton(text='Настройки ⚙️', callback_data='settings')
            inlinekeyboard.row(inlinebutton1)
            await callback.message.bot.send_photo(callback.message.chat.id, open('./assets/start.png', 'rb'), 'Добро пожаловать на моего бота!\nЗдесь ты сможеть узнать больше обо мне. Жми на кнопки ниже!', reply_markup=inlinekeyboard)
            return await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    elif callback.data == 'settings':
        defaultLanguage = BotDB.get_Language(callback.from_user.id)
        if defaultLanguage == "en":
            inlinekeyboard = InlineKeyboardMarkup(resize_keyboard=True)
            inlinebutton1 = InlineKeyboardButton(text='Language ❓', callback_data='language')
            inlinebutton2 = InlineKeyboardButton(text= 'Return back 🔙', callback_data='settingsreturn')
            inlinekeyboard.row(inlinebutton1)
            inlinekeyboard.row(inlinebutton2)
            await callback.message.bot.send_message(callback.message.chat.id, text='Please pick an option below and I will tell you more about it.', reply_markup=inlinekeyboard)
            return await callback.message.delete()
        elif defaultLanguage == "ru":
            inlinekeyboard = InlineKeyboardMarkup(resize_keyboard=True)
            inlinebutton1 = InlineKeyboardButton(text='Язык ❓', callback_data='language')
            inlinebutton2 = InlineKeyboardButton(text= 'Вернуться назад 🔙', callback_data='settingsreturn')
            inlinekeyboard.row(inlinebutton1)
            inlinekeyboard.row(inlinebutton2)
            await callback.message.bot.send_message(callback.message.chat.id, text='Пожалуйста, выберите позицию ниже, и я расскажу вам о ней подробнее.', reply_markup=inlinekeyboard)
            return await callback.message.delete()