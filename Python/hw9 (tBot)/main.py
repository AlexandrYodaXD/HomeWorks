from handlers.main_handlers import dp
from aiogram import executor


async def on_start(_):
    print('Bot started')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)
