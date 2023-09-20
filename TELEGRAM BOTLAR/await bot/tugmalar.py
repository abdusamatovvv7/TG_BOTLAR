from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
bosh_menu = ReplyKeyboardMarkup(
    [
    [
        KeyboardButton("KONTAKT"),
        KeyboardButton("AUDIO"),
        KeyboardButton("VIDEO"),
        KeyboardButton("RASM"),
    ],

    [
                
        KeyboardButton("LOCATION"),
        KeyboardButton("STIKER"),
    ],

    [
        KeyboardButton("DOCUMENT"),
        KeyboardButton("So'rovnoma"),
        KeyboardButton("ANIMATION"),
        KeyboardButton("")
    ]
    ], 
   resize_keyboard=True
)
photo_menu = ReplyKeyboardMarkup(
    resize_keyboard=True 
)
kontakt_menu = ReplyKeyboardMarkup(
   resize_keyboard=True
)
location_menu = ReplyKeyboardMarkup(
    resize_keyboard=True
)
audio_menu = ReplyKeyboardMarkup(
    resize_keyboard=True
)
video_menu = ReplyKeyboardMarkup(
    resize_keyboard=True
)
stiker_menu = ReplyKeyboardMarkup(
    resize_keyboard=True
)
poll_menu = ReplyKeyboardMarkup(
    resize_keyboard=True
)
document_menu = ReplyKeyboardMarkup(
    resize_keyboard=True
)
animatsiya_menu = ReplyKeyboardMarkup(
    resize_keyboard=True
)