from aiogram.types import Message
import config

async def help_command(message: Message):
    user = message.from_user

    await message.answer(
        config.TEXTS["help"].format(
            name=user.first_name,
        )
    )