from aiogram.types import Message
from headers import db, keyboards
import config,main
#---------------------------------------------------------------------------------------
USER_ID = user.id
#---------------------------------------------------------------------------------------
async def init(message: Message):

    have_apples  = db.get(USER_ID, "apples")
    have_carrots = db.get(USER_ID, "carrots")
    balance      = db.get(USER_ID, "balance")

    await message.answer(
        config.TEXTS["tm_init"].format(
            balance=balance,
            cost_apples=main.COST_APPLES,
            cost_carrots=main.COST_CARROTS,
            have_apples=have_apples,
            have_carrots=have_carrots
            
        ),reply_markup=keyboards.tm_menu()
    )
#---------------------------------------------------------------------------------------
async def feed (message: Message):

    NEED_TO_FEED = message.text

    have_apples  = db.get(USER_ID, "apples")
    have_carrots = db.get(USER_ID, "carrots")
    balance      = db.get(USER_ID, "balance")

    if have_apples >= 1 or have_carrots >= 1:
        if NEED_TO_FEED == "":
            None
        elif NEED_TO_FEED == "":
            None
        else: 
            None
    else:
        await message.answer(
            config.TEXTS["tm_feed_failed"].format(
                
            ),reply_markup=keyboards.tm_menu()
        )
#---------------------------------------------------------------------------------------
async def play (message: Message):
    None