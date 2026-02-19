from aiogram.types import Message
from headers import db, keyboards
import config
#---------------------------------------------------------------------------------------
USER_ID = user.id
#---------------------------------------------------------------------------------------
async def init(message: Message):
    user    = message.from_user

    food    = db.get(USER_ID, "food")
    water   = db.get(USER_ID, "water")
    comfort = db.get(USER_ID, "comfort")
    balance = db.get(USER_ID, "balance")
    apples  = db.get(USER_ID, "apples")
    carrot  = db.get(USER_ID, "carrots")
    bottles = db.get(USER_ID, "bottles")

    await message.answer(
        config.TEXTS["status"].format(
            food=food,
            water=water,
            comfort=comfort,
            balance=balance,
            apples=apples,
            carrot=carrot
        ),reply_markup=keyboards.back_to_main()
    )