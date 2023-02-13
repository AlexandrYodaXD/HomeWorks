from random import choice
from bot import dp, bot
from aiogram import types
from keyboards import support_kb


@dp.message_handler(commands=['поддержка'])
async def start(message: types.Message):
    with open('media\\support_words.db', 'r', encoding='UTF-8') as file:
        support_list = file.readlines()
        await message.answer(text=choice(support_list))
