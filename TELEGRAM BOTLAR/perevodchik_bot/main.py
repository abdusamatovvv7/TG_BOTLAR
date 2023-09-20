import logging
import requests

from aiogram import Bot, Dispatcher, executor, types
from test import google_translate
API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom")

@dp.message_handler(commands=['salom'])
async def send_welcome(message: types.Message):
    any_text = message.text
    await messgae.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    