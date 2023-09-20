import logging

from aiogram import Bot, Dispatcher, executor, types
from tugmalar import bosh_menu, ovqatlar_menu, salatlar_menu, ichimliklar_menu, osh_menu, fanta_menu
API_TOKEN = ''

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum!", reply_markup=bosh_menu)



#OVQAT
@dp.message_handler(text="Ovqat")
async def echo(message: types.Message):
    await message.answer("Menu", reply_markup=ovqatlar_menu)

@dp.message_handler(text="Ortga")
async def echo(message: types.Message):
    await message.answer("Ortga qayttingiz!", reply_markup=bosh_menu)

#SALAT
@dp.message_handler(text="Salat")
async def echo(message: types.Message):
    await message.answer("Menu", reply_markup=salatlar_menu)

@dp.message_handler(text="Ortga")
async def echo(message: types.Message):
    await message.answer("Ortga qayttingiz!", reply_markup=bosh_menu)

#ICHIMLIK

@dp.message_handler(text="Ichimlik")
async def echo(message: types.Message):
    await message.answer("Menu", reply_markup=ichimliklar_menu)

@dp.message_handler(text="Ortga")
async def echo(message: types.Message):
    await message.answer("Ortga qayttingiz!", reply_markup=bosh_menu)

@dp.message_handler(text="Fanta")
async def echo(message: types.Message):
    await message.answer("Sonini kiriting !", reply_markup=fanta_menu)


#OSH
@dp.message_handler(text="Osh")
async def echo(message: types.Message):
    await message.answer("Sonini kiritng!", reply_markup=osh_menu)


@dp.message_handler(text="Ortga")
async def echo(message: types.Message):
    await message.answer("Ortga qayttingiz!", reply_markup=osh_menu)


@dp.message_handler(text="1")
async def echo(message: types.Message):
    await message.answer("1 porsa osh \n ✅Qabul qilindi ! \n Narxi; 45.000💸 \n UZB boylab dastavka BEPUL💸", reply_markup=osh_menu)    


@dp.message_handler(text="2")
async def echo(message: types.Message):
    await message.answer("2 porsa osh \n ✅Qabul qilindi ! \n Narxi; 90.000💸 \n UZB boylab dastavka BEPUL💸", reply_markup=osh_menu)  


@dp.message_handler(text="3")
async def echo(message: types.Message):
    await message.answer("3 porsa osh \n ✅Qabul qilindi ! \n Narxi; 135.000💸 \n UZB boylab dastavka BEPUL💸", reply_markup=osh_menu)      
    

@dp.message_handler(text="4")
async def echo(message: types.Message):
    await message.answer("4 porsa osh \n ✅Qabul qilindi ! \n Narxi; 180.000💸 \n UZB boylab dastavka BEPUL💸", reply_markup=osh_menu)  

@dp.message_handler(text="5")
async def echo(message: types.Message):
    await message.answer("5 porsa osh \n ✅Qabul qilindi ! \n Narxi; 225.000💸 \n UZB boylab dastavka BEPUL💸", reply_markup=osh_menu) 


@dp.message_handler(text="6")
async def echo(message: types.Message):
    await message.answer("6 porsa osh \n ✅Qabul qilindi ! \n Narxi; 270.000💸 \n UZB boylab dastavka BEPUL💸", reply_markup=osh_menu)    


@dp.message_handler(text="7")
async def echo(message: types.Message):
    await message.answer("7 porsa osh \n ✅Qabul qilindi ! \n Narxi; 315.000💸 \n UZB boylab dastavka BEPUL💸", reply_markup=osh_menu)  


@dp.message_handler(text="8")
async def echo(message: types.Message):
    await message.answer("8 porsa osh \n ✅Qabul qilindi ! \n Narxi; 360.000💸 \n UZB boylab dastavka BEPUL💸", reply_markup=osh_menu)      
    

@dp.message_handler(text="9")
async def echo(message: types.Message):
    await message.answer("9 porsa osh \n ✅Qabul qilindi ! \n Narxi; 405.000💸 \n UZB boylab dastavka BEPUL💸", reply_markup=osh_menu)  

@dp.message_handler(text="10")
async def echo(message: types.Message):
    await message.answer("10 porsa osh \n ✅Qabul qilindi ! \n Narxi; 450.000💸 \n UZB boylab dastavka BEPUL💸", reply_markup=osh_menu) 
@dp.message_handler()


async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)