from aiogram.types import Message
from headers import db, keyboards
import config,main

USER_ID = user.id
#---------------------------------------------------------------------------------------
async def init(message: Message):

    have_apples = db.get_user_apples(USER_ID)
    have_carrots = db.get_user_carrots(USER_ID)
    balance = db.get_user_balance(USER_ID)

    await message.answer(
        config.TEXTS["shop"].format(
            balance=balance,
            cost_apples=main.COST_APPLES,
            cost_carrots=main.COST_CARROTS,
            have_apples=have_apples,
            have_carrots=have_carrots
            
        ),reply_markup=keyboards.shop_menu()
    )

async def buy(message: Message):

    NEED_TO_BUY = message.text

    have_apples = db.get_user_apples(USER_ID)
    have_carrots = db.get_user_carrots(USER_ID)
    balance = db.get_user_balance(USER_ID)

    if NEED_TO_BUY == "Яблоки":
        if balance >= main.COST_APPLES:
            db.increese_apples(USER_ID,main.HOW_MUCH_ADDED_APPLES)
            db.decreese_balance(USER_ID,main.COST_APPLES)
        else:
            await message.answer(
            config.TEXTS["shop_failed_buy"].format(
                balance=balance,
                cost_apples=main.COST_APPLES,
                cost_carrots=main.COST_CARROTS,
                have_apples=have_apples,
                have_carrots=have_carrots
                
            ),reply_markup=keyboards.shop_menu()
        )
    elif NEED_TO_BUY == "Морковку":
        if balance >= main.COST_CARROTS:
            db.increese_apples(USER_ID,main.HOW_MUCH_ADDED_CARROTS)
            db.decreese_balance(USER_ID,main.COST_CARROTS)
        else:
            await message.answer(
            config.TEXTS["shop_failed_buy"].format(
                balance=balance,
                cost_apples=main.COST_APPLES,
                cost_carrots=main.COST_CARROTS,
                have_apples=have_apples,
                have_carrots=have_carrots
                
            ),reply_markup=keyboards.shop_menu()
        )
    else:
        await message.answer(
            config.TEXTS["shop_unknown"].format(
                balance=balance,
                cost_apples=main.COST_APPLES,
                cost_carrots=main.COST_CARROTS,
                have_apples=have_apples,
                have_carrots=have_carrots
                
            ),reply_markup=keyboards.shop_menu()
        )