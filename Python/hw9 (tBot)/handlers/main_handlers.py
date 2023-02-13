from bot import dp, bot
from aiogram import types


@dp.message_handler(commands=['start', 'старт'])
async def start(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    print('New /start detected! user_id:', user_id, 'user_name: ', user_name)
    markup = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    candy_game_button = types.InlineKeyboardButton('"Candy Game" 🍬🍬', callback_data='candy_game')
    markup.add(candy_game_button)

    img = open('media\\saw_doll.jpeg', 'rb')
    await bot.send_photo(user_id, img, reply_markup=markup,
                         caption=f'Здравствуй, <b>{user_name}</b>!\n'
                                 'Я хочу сыграть с тобой в игру!\n'
                                 'А уж в какую сам выбирай...',
                         parse_mode='html')


@dp.message_handler()
async def all_message_handler(message: types.Message):
    print('message:', message)


@dp.callback_query_handler()
async def all_msg(callback: types.CallbackQuery):
    print('callback:', callback)
