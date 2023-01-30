from aiogram import types
# from handlers.candy_game import GRAB_COUNT_CANDY
# устанавливаю хардкодно, потому что ругается на исключение:
# "ImportError: cannot import name 'GRAB_COUNT_CANDY' from partially initialized module 'handlers.candy_game' (most likely due to a circular import)"
GRAB_COUNT_CANDY = 28
callback_list = ['kb_grab_' + str(x) for x in range(1, GRAB_COUNT_CANDY + 1)]


def get_kb(available: int) -> types.ReplyKeyboardMarkup:
    buttons = [types.InlineKeyboardButton(text=str(x) + ' 🍬', callback_data='kb_grab_' + str(x)) for x in
               range(1, available + 1)]
    markup = types.InlineKeyboardMarkup(row_width=7)
    markup.add(*buttons)

    return markup
