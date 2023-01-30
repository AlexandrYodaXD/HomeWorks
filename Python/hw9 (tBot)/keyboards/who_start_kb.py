from aiogram import types

callback_list = [
    'kb_who_start_player', 'kb_who_start_bot', 'kb_who_start_fate'
]


def get_kb() -> types.ReplyKeyboardMarkup:
    buttons = [
        [
            types.InlineKeyboardButton(text='😎 Я начну!', callback_data='kb_who_start_player'),
            types.InlineKeyboardButton(text='🤡 Ты начнешь!', callback_data='kb_who_start_bot'),
        ],
        [
            types.InlineKeyboardButton(text='🎲 Пускай судьба решит! 🎲', callback_data='kb_who_start_fate'),
        ],
    ]
    markup = types.InlineKeyboardMarkup(inline_keyboard=buttons)

    return markup
