from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
bosh_menu = ReplyKeyboardMarkup(
    [
    [
        KeyboardButton("Ovqat"),
        KeyboardButton("Salat"),
        KeyboardButton("Ichimlik"),
    ]
    ], 
   resize_keyboard=True
)
ovqatlar_menu = ReplyKeyboardMarkup(
    [
    [
        KeyboardButton("Osh"),
        KeyboardButton("Shashlik"),
        KeyboardButton("Norin"),
        KeyboardButton("Ortga")
    ]
    ],
    resize_keyboard=True
)

osh_menu = ReplyKeyboardMarkup(
    [
    [
        KeyboardButton("1"),
        KeyboardButton("2"),
        KeyboardButton("3"),
        KeyboardButton("4"),
        KeyboardButton("5"),
        KeyboardButton("6"),
        KeyboardButton("7"),
        KeyboardButton("8"),
        KeyboardButton("9"),
        KeyboardButton("10")
    ],
    [
        KeyboardButton("Ortga")
    ]
    ],
    resize_keyboard=True
)
salatlar_menu = ReplyKeyboardMarkup(
    [
    [
        KeyboardButton("Olivye"),
        KeyboardButton("Vinigret"),
        KeyboardButton("Sezar"),
        KeyboardButton("Ortga")
    ]
    ],
    resize_keyboard=True
)
ichimliklar_menu  = ReplyKeyboardMarkup(
    [
    [
        KeyboardButton("Fanta"),
        KeyboardButton("Cola"),
        KeyboardButton("Pepsi"),
        KeyboardButton("Ortga")
    ]
    ],
    resize_keyboard=True
)
fanta_menu = ReplyKeyboardMarkup(
    [
    [
        KeyboardButton("1"),
        KeyboardButton("2")
    ]
    ]
)