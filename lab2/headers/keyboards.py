from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from aiogram import F
from aiogram.filters import Command
from headers import status, help_, start, shop, tamogochi
#---------------------------------------------------------------------------------------
def main_menu():
    kb = [
        [KeyboardButton(text="Статус")],
        [KeyboardButton(text="Тамогочи")],
        [KeyboardButton(text="Магазин")],
        [KeyboardButton(text="Справка")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Главное Меню"
    )
#---------------------------------------------------------------------------------------
def back_to_main():
    kb = [
        [KeyboardButton(text="Назад")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Назад в ГМ"
    )
#---------------------------------------------------------------------------------------
def shop_menu():
    kb = [
        [KeyboardButton(text="Яблоки")],
        [KeyboardButton(text="Морковку")]
        [KeyboardButton(text="Назад")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Меню магазина"
    )
#---------------------------------------------------------------------------------------
def register(dp):
#---------------------------------------------------------------------------------------
    @dp.message(Command('start'))
    async def back_to_start(message: Message):
        await start.init(message)
#---------------------------------------------------------------------------------------
    @dp.message(F.text == "Статус")
    async def status_button(message: Message):
        await status.init(message)
#---------------------------------------------------------------------------------------
    @dp.message(F.text == "Справка")
    async def help_button(message: Message):
        await help_.init(message)
#---------------------------------------------------------------------------------------
    @dp.message(F.text == "Тамогочи")
    async def tamogochi_button(message: Message):
        await tamogochi.init(message)
#---------------------------------------------------------------------------------------
    @dp.message(F.text == "Магазин")
    async def shop_button(message: Message):
        await shop.init(message)

    @dp.message(F.text == "Яблоки" or F.text == "Морковку")
    async def apples_button(message: Message):
        await shop.buy(message)

#---------------------------------------------------------------------------------------
    @dp.message(F.text == "Назад")
    async def status_button(message: Message):
        await start.status(message)