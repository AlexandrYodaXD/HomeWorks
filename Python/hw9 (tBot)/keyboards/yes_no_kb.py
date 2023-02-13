from aiogram import types

callback_list = ['kb_yesno_yes', 'kb_yesno_no']


def get_kb() -> types.ReplyKeyboardMarkup:

    buttons = [
        [
            types.InlineKeyboardButton(text='🟢 Да', callback_data='kb_yesno_yes'),
            types.InlineKeyboardButton(text='🔴 Нет', callback_data='kb_yesno_no'),
        ],
    ]
    markup = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return markup
