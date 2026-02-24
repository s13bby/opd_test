from aiogram.types import Message
from extensions import keyboards
import config
#---------------------------------------------------------------------------------------
async def init(message: Message):
    user = message.from_user

    await message.answer(
        config.TEXTS["help"].format(
            name=user.first_name,
        ), reply_markup=keyboards.back_to_main()
    )