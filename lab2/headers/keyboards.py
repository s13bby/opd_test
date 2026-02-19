from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#---------------------------------------------------------------------------------------
def main_menu():
    kb = [
        [KeyboardButton(text="Статус")],
        [KeyboardButton(text="Тамогочи")],
        [KeyboardButton(text="Магазин")],
        [KeyboardButton(text="Справка")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Главное Меню"
    )
#---------------------------------------------------------------------------------------
def back_to_main():
    kb = [
        [KeyboardButton(text="Назад в меню")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Назад в ГМ"
    )
#---------------------------------------------------------------------------------------
def shop_menu():
    kb = [
        [KeyboardButton(text="Яблоки")],
        [KeyboardButton(text="Морковку")]
        [KeyboardButton(text="Назад")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Меню магазина"
    )
#---------------------------------------------------------------------------------------
def tm_menu():
    kb = [
        [KeyboardButton(text="Покормить")],
        [KeyboardButton(text="Поиграть")]
        [KeyboardButton(text="Назад в меню")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Меню ТМ"
    )
