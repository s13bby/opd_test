from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from extensions import status, help_, start, shop,keyboards as kb, tamogochi as tm
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
    @dp.message(F.text == "Магазин")
    async def shop_button(message: Message):
        await shop.init(message)

    @dp.message(F.text == "Яблоки")
    async def apples_button(message: Message):
        await shop.buy(message)
#---------------------------------------------------------------------------------------
    @dp.message(F.text == "Тамогочи")
    async def tamogochi_button(message: Message):
        await tm.init(message)
        
    @dp.message(F.text == "Покормить")
    async def feed_button(message: Message):
        await tm.feed(message)

    @dp.message(F.text == "Поиграть")
    async def play_button(message: Message):
        await tm.play(message)
#---------------------------------------------------------------------------------------
    @dp.message(F.text == "Назад в меню")
    async def status_button(message: Message):
        await start.init(message)