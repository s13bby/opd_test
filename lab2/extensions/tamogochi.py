from aiogram.types import Message
from extensions import db, keyboards
import config, main
#---------------------------------------------------------------------------------------
async def init(message: Message):
    user    = message.from_user
    USER_ID = user.id

    food    = db.get(USER_ID, "food")
    water   = db.get(USER_ID, "water")
    comfort = db.get(USER_ID, "comfort")
    have_apples  = db.get(USER_ID, "apples")

    await message.answer(
        config.TEXTS["tm_init"].format(
            name=user.first_name,
            food=food,
            water=water,
            comfort=comfort,
            have_apples=have_apples,
            
        ),reply_markup=keyboards.tm_menu()
    )
#---------------------------------------------------------------------------------------
async def feed (message: Message):
    user    = message.from_user
    USER_ID = user.id

    food    = db.get(USER_ID, "food")
    water   = db.get(USER_ID, "water")
    comfort = db.get(USER_ID, "comfort")
    have_apples  = db.get(USER_ID, "apples")

    NEED_TO_FEED = message.text

    if have_apples >= 2:

        if NEED_TO_FEED == "Покормить":
            if food == 100 or water == 100:
                await message.answer(
                    config.TEXTS["tm_no_need_feed"].format(
                        food=food,
                        water=water,
                        comfort=comfort,
                        have_apples=have_apples,
                    ),reply_markup=keyboards.tm_menu()
                )
            else:
                db.increese(USER_ID, main.HOW_MUCH_ADDED_FOOD, "food")
                db.increese(USER_ID, main.HOW_MUCH_ADDED_WATER, "water")
                db.decreese(USER_ID, main.HOW_MUCH_EAT_TM, "apples")
                if db.get(USER_ID, "food") > 100:
                    db.set_(USER_ID, 100, "food")
                elif db.get(USER_ID, "water") > 100:
                    db.set_(USER_ID, 100, "water")
                
                food    = db.get(USER_ID, "food")
                water   = db.get(USER_ID, "water")
                comfort = db.get(USER_ID, "comfort")
                have_apples  = db.get(USER_ID, "apples")
                
                await message.answer(
                    config.TEXTS["tm_feed"].format(
                        food=food,
                        water=water,
                        comfort=comfort,
                        have_apples=have_apples,
                    ),reply_markup=keyboards.tm_menu()
                )
        else: 
            await message.answer(
                    config.TEXTS["tm_failed"],reply_markup=keyboards.tm_menu()
                )
    else:
        await message.answer(
                    config.TEXTS["tm_no_apples"],reply_markup=keyboards.tm_menu()
            )
#---------------------------------------------------------------------------------------
async def play (message: Message):
    user    = message.from_user
    USER_ID = user.id
    food    = db.get(USER_ID, "food")
    water   = db.get(USER_ID, "water")
    comfort = db.get(USER_ID, "comfort")
    NEED_TO_PLAY = message.text

    if NEED_TO_PLAY == "Поиграть":

        if comfort == 100:
            await message.answer(
                config.TEXTS["tm_no_need_play"].format(
                    food=food,
                    water=water,
                    comfort=comfort,
                ),reply_markup=keyboards.tm_menu()
            )
        else:
            db.increese(USER_ID, main.HOW_MUCH_ADDED_COMFORT, "comfort")
            if db.get(USER_ID, "comfort") > 100:
                db.set_(USER_ID, 100, "comfort")
            
            food    = db.get(USER_ID, "food")
            water   = db.get(USER_ID, "water")
            comfort = db.get(USER_ID, "comfort")
            
            await message.answer(
                config.TEXTS["tm_play"].format(
                    food=food,
                    water=water,
                    comfort=comfort,
                ),reply_markup=keyboards.tm_menu()
            )
    else: 
        await message.answer(
                config.TEXTS["tm_failed"],reply_markup=keyboards.tm_menu()
            )