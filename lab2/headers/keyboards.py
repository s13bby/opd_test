from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
from headers import status, help_

def get_main_menu():
    kb = [
        [KeyboardButton(text="Статус")],
        [KeyboardButton(text="Справка")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Главное Меню"
    )

def get_main_menu():
    kb = [
        [KeyboardButton(text="Статус")],
        [KeyboardButton(text="Справка")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Главное Меню"
    )

def register(dp):
    @dp.message(F.text == "Статус")
    async def status_button(message: Message):
        await status.status_command(message)

    @dp.message(F.text == "Справка")
    async def status_button(message: Message):
        await help_.help_command(message)
