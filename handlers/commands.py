from aiogram import Dispatcher, types
from keyboards import inline
from configurations import states


async def bot_start(msg: types.Message):
    await msg.delete()
    name = msg.from_user.first_name
    await msg.answer(f"Hello, {name}! Press 'Start' for test beginning",
                     reply_markup=inline.questions_start())
    await states.Questions.question_1.set()


def register(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands='start', state='*')
    dp.register_message_handler(ya_disk, commands='disk', state='*')
