from aiogram.types import Message
from headers import db, keyboards
import config,main
#---------------------------------------------------------------------------------------
async def status_command(message: Message):

    have_apples = db.get_user_apples(user.id)
    have_carrots = db.get_user_carrots(user.id)
    balance = db.get_user_balance(user.id)

    await message.answer(
        config.TEXTS["shop"].format(
            balance=balance,
            cost_apples=main.COST_APPLES,
            cost_carrots=main.COST_CARROTS,
            have_apples=have_apples,
            have_carrots=have_carrots
            
        ),reply_markup=keyboards.shop_menu()
    )