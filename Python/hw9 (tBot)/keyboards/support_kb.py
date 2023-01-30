from aiogram import types


def get_kb() -> types.ReplyKeyboardMarkup:
    kb = [
        [
            types.KeyboardButton(text='/старт'),
            types.KeyboardButton(text='/поддержка'),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True)
    return keyboard
