from aiogram import Bot, Dispatcher
from os import getenv


# TOKEN = ''
TOKEN = getenv('TOKEN')


bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)

