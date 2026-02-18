from aiogram.filters import Command
from aiogram.types import Message
from headers import db
import config

def register(dp):
    @dp.message(Command('help'))
    async def status_command(message: Message):
        user = message.from_user

        await message.answer(
            config.TEXTS["help"].format(
                name=user.first_name,
            )
        )