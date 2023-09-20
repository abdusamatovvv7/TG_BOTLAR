import logging

from aiogram import Bot, Dispatcher, executor, types
from tugmalar import *
API_TOKEN = ''

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Mars botiga xush kelibsiz!\nIltimos, variantni tanlang", reply_markup=bosh_menu_inline)

 
@dp.message_handler(text="🧑‍🎓 Профиль")
async def echo(message: types.Message):
    await message.answer("""
Ism: Muhammad Amin
Familiya: Abdusamatov
Til: uz
Telefon: 93.557-75-35
Shahar: Toshkent
Ta’lim markazi: YUNUSABAD
""", reply_markup=Profil_keyboard)


@dp.message_handler(text="🪙 Мои монеты")
async def echo(message: types.Message):
    await message.answer("Mening mars tangalarim:  ∞")


@dp.message_handler(text="💥 Space Shop")
async def echo(message: types.Message):
    await message.answer_photo("https://t.me/dlya_silku/2")
    await message.answer_photo("https://t.me/dlya_silku/3")
    await message.answer_photo("https://t.me/dlya_silku/4")
    await message.answer_photo("https://t.me/dlya_silku/5")
    await message.answer_photo("https://t.me/dlya_silku/6")
    await message.answer_photo("https://t.me/dlya_silku/7")
    await message.answer_photo("https://t.me/dlya_silku/8")

@dp.message_handler(text="🏫 О школе")
async def echo(message: types.Message):
    await message.answer("""Biz haqimizda
O’zbekistonda IT o’quv markazlari kundan-kunga ko’payib bormoqda. Ammo bular ichida yosh bolalarga mo’ljallangan dasturlash o’quv markazlari qo’l bilan sanoqli.

Mars IT School esa ana shu talabni hisobga olgan holda 8-16 yosh bolalarga kompyuter savodxonligi, scratch, python, grafik dizayn va boshqa IT kurslarini ta’lim berib kelmoqda.

O’quv markazning asosiy maqsadi xalqimizga yetuk IT mutaxassislar tayyorlab beribgina qolmay, vaqtlari kompyuter va telefon o’yinlarini o’ynash bilan behuda o’tayotgan bolalarga ushbu qurilmalardan oqilona foydalanishni o’rgatishdir.

Biz bilan farzandingiz o’yin o’ynamaydi, o’yin yaratadi!""")


@dp.message_handler(text="✍️ Оставить отзыв")
async def echo(message: types.Message):
    await message.answer("Yozing ! ! !")


@dp.callback_query_handler(text="2")
async def echo(call: types.CallbackQuery):
    await call.message.answer("O'quvchi botimizga xush kelibsiz ! ! !", reply_markup=student_keyboard)


@dp.callback_query_handler(text="1")
async def echo(call: types.CallbackQuery):
    await call.message.answer("Yangi ism qo'ying", reply_markup=back_keyboard)


@dp.message_handler(text="Orqaga")
async def echo(message: types.Message):
    await message.answer("Bekor qilindi", reply_markup=student_keyboard)


@dp.message_handler(content_types=types.ContentTypes.ANIMATION)
async def echo(message: types.Message):
    await message.answer("Siz gif jo'natingiz🛑❗️")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Qabul qilindi ! ! !")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)