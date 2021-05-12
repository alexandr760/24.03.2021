from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Выберите из меню ниже", reply_markup=menu)


@dp.message_handler(Text(equals=["Информация", "Скрипты", "Эксплойты", "Канал безопасников", "Помощь"]))
async def get_food(message: Message):
    await message.answer(f"Вы выбрали {message.text}. Спасибо, теперь я знаю, что делать", reply_markup=ReplyKeyboardRemove())