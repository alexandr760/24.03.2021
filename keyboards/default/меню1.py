from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Информация"),
            KeyboardButton(text="Скрипты"),
        ],
        [
            KeyboardButton(text="Эксплойты"),
            KeyboardButton(text="Канал безопасников"),
            KeyboardButton(text="Помощь")
        ],
        ],
    resize_keyboard=True
)
