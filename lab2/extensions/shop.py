from aiogram.types import Message
from extensions import db, keyboards
import config, main
#---------------------------------------------------------------------------------------
async def init(message: Message):
    user    = message.from_user
    USER_ID = user.id

    have_apples  = db.get(USER_ID, "apples")
    balance      = db.get(USER_ID, "balance")

    await message.answer(
        config.TEXTS["shop"].format(
            balance=balance,
            cost_apples=main.COST_APPLES,
            have_apples=have_apples,
            
        ), reply_markup=keyboards.shop_menu()
    )
#---------------------------------------------------------------------------------------
async def buy(message: Message):
    user    = message.from_user
    USER_ID = user.id
    
    NEED_TO_BUY  = message.text

    have_apples  = db.get(USER_ID, "apples")
    balance      = db.get(USER_ID, "balance")

    if NEED_TO_BUY == "Яблоки":
        if balance >= main.COST_APPLES:
            db.increese(USER_ID, main.HOW_MUCH_ADDED_APPLES, "apples")
            db.decreese(USER_ID, main.COST_APPLES, "balance")
            await message.answer(
            config.TEXTS["shop_successed_buy"].format(
                balance=balance,
                cost_apples=main.COST_APPLES,
                have_apples=db.get(USER_ID, "apples"),
            ), reply_markup=keyboards.shop_menu()
            )
        else:
            await message.answer(
            config.TEXTS["shop_failed_buy"].format(
                balance=balance,
                cost_apples=main.COST_APPLES,
                have_apples=have_apples,
                
            ), reply_markup=keyboards.shop_menu()
        )
    else:
        await message.answer(
            config.TEXTS["shop_unknown"].format(
                balance=balance,
                cost_apples=main.COST_APPLES,
                have_apples=have_apples,
                
            ), reply_markup=keyboards.shop_menu()
        )