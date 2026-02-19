from aiogram.filters import Command
from aiogram.types import Message
from headers import db, keyboards
import config
#---------------------------------------------------------------------------------------
USER_ID = user.id
USERNAME= user.username
#---------------------------------------------------------------------------------------
async def init(message: Message):
    user    = message.from_user

    db.add_user(USER_ID, USERNAME)

    food    = db.get(USER_ID, "food")
    water   = db.get(USER_ID, "water")
    comfort = db.get(USER_ID, "comfort")
    balance = db.get(USER_ID, "balance")

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