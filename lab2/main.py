#Игра “Тамагочи”. “Тамагочи” - персонаж, у которого есть потребность в еде, питье, играх. Показатели удовлетворенности уменьшаются с течением времени.


import asyncio
from os import getenv
from aiogram import Bot, Dispatcher
from headers import db, keyboards
from config import TOKEN
#---------------------------------------------------------------------------------------
COST_APPLES  = 5
COST_CARROTS = 2
HOW_MUCH_ADDED_APPLES = 3
HOW_MUCH_ADDED_CARROTS = 5

dp = Dispatcher()
#---------------------------------------------------------------------------------------
async def main():
    bot = Bot(token=TOKEN)

    keyboards.register(dp)
    
    await dp.start_polling(bot)
#---------------------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        print('бот работает')
        db.init_db()
        asyncio.run(main())
        
    except ValueError:
        print('бот не работает')

