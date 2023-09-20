import logging

from aiogram import Bot, Dispatcher, executor, types
from tugmalar import bosh_menu, photo_menu, kontakt_menu, audio_menu, video_menu, location_menu, stiker_menu, document_menu

API_TOKEN = '6098591968:AAFcuGnae8ioZYRt9YJUKWTZmX6T-ueAvRk'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum!", reply_markup=bosh_menu)


@dp.message_handler(text="RASM")
async def echo(message: types.Message):
    await message.answer("Iltimos kuting ...", reply_markup=photo_menu)
    await message.answer_photo("https://image2.turizm.ru/CE/pub/page/189535/15683752133136.jpg")


@dp.message_handler(text="KONTAKT")
async def echo(message: types.Message):
    await message.answer("Iltimos kuting ...", reply_markup=kontakt_menu)
    await message.answer_contact("+998 93.557-75-35", "Muhammadamin")


@dp.message_handler(text="LOCATION")
async def echo(message: types.Message):
    await message.answer("Iltimos kuting ...", reply_markup=location_menu)
    await message.answer_location(41.367078433950276, 69.28620283642638)


@dp.message_handler(text="AUDIO")
async def echo(message: types.Message):
    await message.answer("Iltimos kuting ...", reply_markup=audio_menu)
    await message.answer_audio("https://t.me/Sara_Xabarlar/30179")


@dp.message_handler(text="VIDEO")
async def echo(message: types.Message):
    await message.answer("Iltimos kuting ...", reply_markup=video_menu)
    await message.answer_video("https://t.me/Sara_Xabarlar/30181")


@dp.message_handler(text="STIKER")
async def echo(message: types.Message):
    await message.answer("Iltimos kuting ...", reply_markup=stiker_menu)
    await message.answer_animation("https://t.me/dev_351/221")


@dp.message_handler(text="DOCUMENT")
async def echo(message: types.Message):
    await message.answer("Iltimos kuting ...", reply_markup=document_menu)
    await message.answer_document("https://t.me/TopDocumentaryFilms/1899")


@dp.message_handler(text="So'rovnoma")
async def echo(message: types.Message):
    await message.answer("Iltimos kuting ...", reply_markup=document_menu)
    await message.answer_poll(question="Mars IT qachon ochilgan?", 
                              options=["2020", "2021", "2022"],
                              correct_option_id=2,
                              type="quiz",
                              open_period=10)


@dp.message_handler(text="ANIMATION")
async def echo(message: types.Message):
    await message.answer("Iltimos kuting ...", reply_markup=animatsiya_menu)
    await message.answer_animation("https://t.me/Back351/6")



# @dp.message_handler(text="")
# async def echo(message: types.Message):
#     await message.answer("Iltimos kuting ...", reply_markup=)
#     await message.answer_document("")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)