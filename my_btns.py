from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='awqatlar',
                callback_data='awqat'
            ),
            InlineKeyboardButton(
                text='ishimlik',
                callback_data='ishiw'
            )
        ],
        [
            InlineKeyboardButton(
                text='Fast Food',
                callback_data='FF'
            ),   
        ],
        [
            InlineKeyboardButton(
                text='Desert',
                callback_data='desert'
            ),
            InlineKeyboardButton(
                text='Salatlar',
                callback_data='salat'
            ),
        ],
        [
            InlineKeyboardButton(
                text='Garnirlar',
                callback_data='gar'
            ),   
        ]
    ]
)
Food_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='lavash',
                callback_data='lav'
            )
        ],
        [
            InlineKeyboardButton(
                text='plov',
                callback_data='plov'
            )
        ],
        [
            InlineKeyboardButton(
                text='Manti',
                callback_data='man'
            )
        ]
    ]
)








