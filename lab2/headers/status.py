from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton
from headers import db
import config

def register(dp):
    @dp.message(Command('status'))
    async def status_command(message: Message):
        user = message.from_user

        food = db.get_user_food(user.id)
        water = db.get_user_water(user.id)
        comfort = db.get_user_comfort(user.id)

        await message.answer(
            config.TEXTS["status"].format(
                name=user.first_name,
                food=food,
                water=water,
                comfort=comfort
            )
        )