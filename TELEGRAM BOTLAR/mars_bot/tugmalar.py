from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

bosh_menu_inline = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
        InlineKeyboardButton(text="👨‍👩‍👦 Ota-onalar uchun", callback_data="1"),
        InlineKeyboardButton(text="👨‍🎓 O'quvchi uchun", callback_data="2")
        ],
        
        [
            InlineKeyboardButton(text="👤 Mehmon uchun", callback_data="3")
        ]
    ]
)

student_keyboard = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton("🧑‍🎓 Профиль"),
            KeyboardButton("🪙 Мои монеты"),
            KeyboardButton("💥 Space Shop"),
        ],
        [
            KeyboardButton("🏫 О школе"),
            KeyboardButton("✍️ Оставить отзыв")
        ]
    ],
    resize_keyboard=True
)

Profil_keyboard = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Ism", callback_data="1"),
            InlineKeyboardButton(text="Familiya", callback_data="2")
        ],
        [
            InlineKeyboardButton(text="Til", callback_data="3"),
            InlineKeyboardButton(text="Telefon", callback_data="4")
        ],
        [
            InlineKeyboardButton(text="Shahar", callback_data="5")
        ],     
    ]
)

back_keyboard = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)