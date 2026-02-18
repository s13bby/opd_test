#Игра “Тамагочи”. “Тамагочи” - персонаж, у которого есть потребность в еде, питье, играх. Показатели удовлетворенности уменьшаются с течением времени.


import asyncio
from os import getenv
from aiogram import Bot, Dispatcher
from headers import db, start, status, help_, keyboards
from config import TOKEN

dp = Dispatcher()

async def main():
    bot = Bot(token=TOKEN)

    start.register(dp)
    keyboards.register(dp)
    
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        print('бот работает')
        db.init_db()
        asyncio.run(main())
        
    except ValueError:
        print('бот не работает')
