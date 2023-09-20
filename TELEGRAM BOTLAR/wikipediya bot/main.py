import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ''
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

 
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom\nWikipediya botga hush kelibsiz!")


@dp.message_handler()
async def echo(message: types.Message):
    language = message.text[0:2]
    # print(language)
    if language=="uz":
        wikipedia.set_lang("uz")
    elif language=='ru':
        wikipedia.set_lang("ru")
    elif language=='en':
        wikipedia.set_lang("en")

    search_text = message.text[3:]
    # print(search_text)
    javob = wikipedia.summary(search_text)
    await message.answer(javob)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)