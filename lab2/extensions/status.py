from aiogram.types import Message
from extensions import db, keyboards
import config
#---------------------------------------------------------------------------------------
async def init(message: Message):
    user    = message.from_user
    USER_ID = user.id

    food    = db.get(USER_ID, "food")
    water   = db.get(USER_ID, "water")
    comfort = db.get(USER_ID, "comfort")
    balance = db.get(USER_ID, "balance")
    apples  = db.get(USER_ID, "apples")
    bottles = db.get(USER_ID, "bottles")

    await message.answer(
        config.TEXTS["status"].format(
            food=food,
            water=water,
            comfort=comfort,
            balance=balance,
            apples=apples,
        ),reply_markup=keyboards.back_to_main()
    )