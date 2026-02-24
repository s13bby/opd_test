#Игра "Тамагочи". "Тамагочи" - персонаж, у которого есть потребность в еде, питье, играх. Показатели удовлетворенности уменьшаются с течением времени.


import asyncio
from os import getenv
from aiogram import Bot, Dispatcher

from extensions import db, interface, scheduler
from config import TOKEN
#---------------------------------------------------------------------------------------
COST_APPLES  = 5

HOW_MUCH_ADDED_APPLES  = 3
HOW_MUCH_ADDED_COINS   = 1
HOW_MUCH_ADDED_FOOD    = 5
HOW_MUCH_ADDED_WATER   = 2
HOW_MUCH_ADDED_COMFORT = 9

HOW_MUCH_REMOVE_COMFORT= 2
HOW_MUCH_REMOVE_FOOD   = 3
HOW_MUCH_REMOVE_WATER  = 1
HOW_MUCH_EAT_TM        = 2


dp = Dispatcher()
#---------------------------------------------------------------------------------------
async def main():
    bot = Bot(token=TOKEN)

    interface.register(dp)

    scheduler.tasker.add_job(scheduler.reward_job, "interval", minutes=5)
    scheduler.tasker.add_job(scheduler.decreese, "interval", minutes= 10)
    scheduler.tasker.start()

    await dp.start_polling(bot)
#---------------------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        print("бот работает")
        db.init_db()
        asyncio.run(main())
        
    except ValueError:
        print("бот не работает")
