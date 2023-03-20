from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup


def questions_start() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Start', callback_data='questions_start')]
    ])
    return kb
