from random import randint
from aiogram import types
from asyncio import sleep
from bot import dp, bot
from keyboards import plus_minus_num_kb, who_start_kb, grab_candy_kb, yes_no_kb, support_kb

MIN_RND_CANDY = 33
MAX_RND_CANDY = 333
GRAB_COUNT_CANDY = 28
user_data = {}


@dp.callback_query_handler(text='candy_game')
async def candy_game_handler(callback: types.CallbackQuery):
    await callback.message.answer('А смелости тебе не занимать я посмотрю! 💪\n'
                                  'Хорошо, сыграем в <b>"Candy Game"</b>! 🍬🍬\n\n'
                                  'ℹ️ Правила у игры просты:\n'
                                  '1️⃣ На стол кладется некоторое количество конфет.\n'
                                  '2️⃣ Мы с тобой по-очереди берём со стола произвольное количество конфет, '
                                  'но <b>не менее <u>одной</u></b> и <b>не более <u>двадцати восьми</u></b>.\n'
                                  '✅ <b>Победит тот кто заберёт со стола последние конфеты!</b>\n\n'
                                  '🆘 Если понадобится поддержка, нажми на кнопку снизу экрана.',
                                  reply_markup=support_kb.get_kb())
    await ask_total_candy(callback.message.chat.id)
    await callback.answer()


def get_random_candy():
    return randint(MIN_RND_CANDY, MAX_RND_CANDY)


def get_candy_ending(count: int):
    '''Возвращает слово "конфета" с правильным окончанием'''
    n = abs(count)
    n %= 100
    if 5 <= n <= 20:
        return 'конфет'
    n %= 10
    if n == 1:
        return 'конфета'
    elif 2 <= n <= 4:
        return 'конфеты'
    else:
        return 'конфет'


async def ask_total_candy(chat_id):
    # в словарь по ключу id_пользователя (это id чата для бота) заносится стартовое случайное значение
    user_data[chat_id] = {
        'total_candy': randint(MIN_RND_CANDY, MAX_RND_CANDY),
        'current_round': 0}
    print(user_data)
    # user_data[chat_id]['total_candy'] = randint(MIN_RND_CANDY, MAX_RND_CANDY)
    total_candy = user_data[chat_id].get('total_candy')
    candy_word = get_candy_ending(total_candy)
    await bot.send_message(chat_id=chat_id,
                           text=f'Перед началом игры нужно определить какое количество конфет будет на столе.'
                           )
    await bot.send_message(chat_id=chat_id,
                           text=f'Сейчас на столе <b>{total_candy}</b> 🍬 {candy_word}.',
                           reply_markup=plus_minus_num_kb.get_kb()
                           )


async def update_num_text(message: types.Message, new_value: int):
    candy_word = get_candy_ending(new_value)
    new_text = f'Сейчас на столе <b>{new_value}</b> 🍬 {candy_word}.'
    if message.html_text != new_text:
        await message.edit_text(
            new_text,
            reply_markup=plus_minus_num_kb.get_kb()
        )


@dp.callback_query_handler(text=plus_minus_num_kb.callback_list)
async def change_total_candy(callback: types.CallbackQuery):
    action = callback.data
    user_id = callback.from_user.id
    total_candy = user_data[user_id].get('total_candy', 0)
    _, operation, number = action.split('_')
    # увеличение/уменьшение значения конфет на столе в пользовательском словаре
    if operation == 'plus' and number.isdigit():
        user_data[user_id]['total_candy'] = total_candy + int(number)
    elif operation == 'minus' and number.isdigit():
        user_data[user_id]['total_candy'] = total_candy - int(number)
    # ограничение минимального количества конфет на столе
    if user_data[user_id]['total_candy'] < GRAB_COUNT_CANDY + 1:
        user_data[user_id]['total_candy'] = GRAB_COUNT_CANDY + 1
        await callback.answer(
            f'На столе не может лежать меньше {GRAB_COUNT_CANDY + 1} {get_candy_ending(GRAB_COUNT_CANDY + 1)}.'
        )
    # обновление текста в сообщении о текущем количестве конфет на столе
    await update_num_text(callback.message, user_data[user_id]['total_candy'])
    # действия при нажатии "подтвердить"
    if action == 'kb_plusminus_accept':
        candy_word = get_candy_ending(total_candy)
        await callback.message.edit_text(
            f'Итак, на столе <u><b>{total_candy}</b></u> 🍬 {candy_word}.',
        )
        await ask_who_start(callback.from_user.id)

    await callback.answer()


async def ask_who_start(chat_id):
    await bot.send_message(chat_id=chat_id,
                           text=f'Теперь определим кто будет ходить первым.',
                           reply_markup=who_start_kb.get_kb())


@dp.callback_query_handler(text=who_start_kb.callback_list)
async def set_who_start(callback: types.CallbackQuery):
    action = callback.data
    user_id = callback.from_user.id
    who_start = ''

    if action == 'kb_who_start_player':
        await callback.message.edit_text(text='Ну конечно же ты выбрал ходить первым! 😎\n'
                                              'Кукол-маньяков в наше время уже совсем не уважают... 👿')
        await lets_start_play(user_id, 'player')
    elif action == 'kb_who_start_bot':
        await callback.message.edit_text(text='Ооооууу! Это так мило что ты позволил мне ходить первым! 🤡\n'
                                              'Не пожалей теперь! 😈')
        await lets_start_play(user_id, 'bot')
    elif action == 'kb_who_start_fate':
        await callback.message.edit_text('Азартный, значит? Мне нравится! 👍\n\n'
                                         'Бросим кость! 🎲\n'
                                         'Чет - <b>ты</b> ходишь первым,\n'
                                         'Нечет - <b>я</b> хожу первым!')
        dice_msg = await callback.message.answer_dice()
        dice_value = dice_msg.dice.value
        await sleep(5)
        if dice_value % 2:
            await callback.message.answer(f'Выпало <b>{dice_value}</b> - чет.\n'
                                          f'Ты ходишь первым!\n'
                                          f'<s><em>Везунчик! 👿</em></s>')
            await lets_start_play(user_id, 'player')
        else:
            await callback.message.answer(f'Выпало <b>{dice_value}</b> - нечет.\n'
                                          f'Я хожу первым!\n'
                                          f'<s><em>Правда, ты уже проиграл... 😈</em></s>')
            await lets_start_play(user_id, 'bot')
    await callback.answer()


async def lets_start_play(user_id: int, who_start: str):
    await sleep(1)
    await bot.send_message(chat_id=user_id, text='Начнём игру!')
    user_data[user_id]['who_start'] = who_start

    await candy_game_round(user_id, whose_turn=who_start)


async def candy_game_round(user_id: int, whose_turn: str):
    leftover_candy = user_data[user_id]['total_candy']

    who_start = user_data[user_id]['who_start']
    # проверка на конец игры
    if leftover_candy <= 0:
        winner = ['bot', 'player'][whose_turn == 'bot']
        if winner == 'player':
            await bot.send_message(chat_id=user_id,
                                   text=f'🎉 Поздравляю! Ты победил! 👿\n'
                                        f'Вот твоя медаль - 🥇.')
        else:
            await bot.send_message(chat_id=user_id,
                                   text=f'🎉 ХА! Я победил! 😈\n'
                                        f'EZ, даже не вспотел!')
        await bot.send_message(chat_id=user_id,
                               text='Сыграем ещё?',
                               reply_markup=yes_no_kb.get_kb())
    else:
        candy_word = get_candy_ending(leftover_candy)
        if who_start == whose_turn:
            user_data[user_id]['current_round'] += 1
            # round_counter = user_data[user_id]['current_round']
            bot_text = f'Раунд {user_data[user_id]["current_round"]}.\n' \
                       f'Сейчас на столе <b>{leftover_candy}</b> 🍬 {candy_word}.'
        else:
            bot_text = f'Сейчас на столе <b>{leftover_candy}</b> 🍬 {candy_word}.'
        await bot.send_message(chat_id=user_id,
                               text=bot_text)
        # получение доступного для взятия кол-ва конфет
        if leftover_candy > GRAB_COUNT_CANDY:
            available = GRAB_COUNT_CANDY
        else:
            available = leftover_candy
        # ход игрока или бота
        if whose_turn == 'player':
            await get_player_grab(user_id, available)
        elif whose_turn == 'bot':
            await bot.send_message(chat_id=user_id,
                                   text='Мой ход... 🤔')
            await sleep(2)
            await get_bot_grab(user_id, available)


async def get_player_grab(user_id: int, available: int):
    await bot.send_message(chat_id=user_id,
                           text='Сколько конфет берешь?',
                           reply_markup=grab_candy_kb.get_kb(available)
                           )


@dp.callback_query_handler(text=grab_candy_kb.callback_list)
async def player_grab(callback: types.CallbackQuery):
    action = callback.data
    user_id = callback.from_user.id
    grab_count = int(action.split('_')[-1])
    user_data[user_id]['total_candy'] -= grab_count
    candy_word = get_candy_ending(grab_count)
    if user_data[user_id]['total_candy'] > 0:
        await callback.message.edit_text(text=f'Ты взял {grab_count} 🍬 {candy_word}.')
    else:
        await callback.message.edit_text(text=f'Ты взял последние {grab_count} 🍬 {candy_word}!')
    await candy_game_round(user_id=user_id, whose_turn='bot')


async def get_bot_grab(user_id: int, available: int):
    leftover_candy = user_data[user_id]['total_candy']
    bot_grab = leftover_candy % (GRAB_COUNT_CANDY + 1)
    candy_word = get_candy_ending(bot_grab)
    if bot_grab == 0:
        bot_grab = 1
    user_data[user_id]['total_candy'] -= bot_grab
    if user_data[user_id]['total_candy'] > 0:
        await bot.send_message(chat_id=user_id,
                               text=f'Я взял {bot_grab} 🍬 {candy_word}.')
    else:
        await bot.send_message(chat_id=user_id,
                               text=f'Я взял последние {bot_grab} 🍬 {candy_word}!')
    await candy_game_round(user_id=user_id, whose_turn='player')


@dp.callback_query_handler(text=yes_no_kb.callback_list)
async def get_restart_answer(callback: types.CallbackQuery):
    action = callback.data
    user_id = callback.from_user.id
    if action == 'kb_yesno_yes':
        await ask_total_candy(user_id)
    elif action == 'kb_yesno_no':
        img = open('media\\wolf.jpeg', 'rb')
        await bot.send_photo(chat_id=user_id,
                             photo=img,
                             caption=f'Ладно...\n'
                                     f'Но если захочешь еще поиграть просто напиши /start')
    await callback.answer()
