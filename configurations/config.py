from aiogram import types

from handlers.commands import register as reg_commands
from handlers.questions import register as reg_questions


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start bot"),
        ]
    )


def register_handlers(dp):
    reg_commands(dp)
    reg_questions(dp)
