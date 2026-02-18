from aiogram.filters import Command
from aiogram.types import Message
from headers import db, keyboards
import config

async def init(message: Message):
    user = message.from_user

    db.add_user(user.id, user.username)

    food = db.get_user_food(user.id)
    water = db.get_user_water(user.id)
    comfort = db.get_user_comfort(user.id)
    balance = db.get_user_balance(user.id)

    await message.answer(
        config.TEXTS["welcome"].format(
            name=user.first_name,
            food=food,
            water=water,
            comfort=comfort,
            balance=balance
        ), reply_markup=keyboards.main_menu()
    )
c