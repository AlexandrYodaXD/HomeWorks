from aiogram import types

callback_list = [
    'kb_minus_100', 'kb_minus_25', 'kb_minus_5', 'kb_minus_1',
    'kb_plus_100', 'kb_plus_25', 'kb_plus_5', 'kb_plus_1',
    'kb_plusminus_accept',
]

def get_kb() -> types.ReplyKeyboardMarkup:

    buttons = [
        [
            types.InlineKeyboardButton(text='-25 🍬', callback_data='kb_minus_25'),
            types.InlineKeyboardButton(text='-5 🍬', callback_data='kb_minus_5'),
            types.InlineKeyboardButton(text='-1 🍬', callback_data='kb_minus_1'),
            types.InlineKeyboardButton(text='+1 🍬', callback_data='kb_plus_1'),
            types.InlineKeyboardButton(text='+5 🍬', callback_data='kb_plus_5'),
            types.InlineKeyboardButton(text='+25 🍬', callback_data='kb_plus_25'),
        ],
        [
            types.InlineKeyboardButton(text='Подтвердить', callback_data='kb_plusminus_accept'),
        ],
    ]
    markup = types.InlineKeyboardMarkup(inline_keyboard=buttons)

    return markup
