import gspread
from datetime import datetime
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from decouple import config
from configurations import text, states
from oauth2client.service_account import ServiceAccountCredentials


sheet_url = config("SHEET_URL")
credentials_path = "json/name_of_your_json_file.json"
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
gc = gspread.authorize(credentials)
sh = gc.open_by_url(sheet_url)
worksheet = sh.get_worksheet(0)


async def question_1(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=text.question_1)
    await states.Questions.next()


async def question_2(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_1'] = msg.text
    await msg.answer(text=text.question_2)
    await states.Questions.next()


async def question_3(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_2'] = msg.text
    await msg.answer(text=text.question_3)
    await states.Questions.next()


async def question_4(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_3'] = msg.text
    await msg.answer(text=text.question_4)
    await states.Questions.next()


async def question_5(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_4'] = msg.text
    await msg.answer(text=text.question_5)
    await states.Questions.next()


async def question_6(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_5'] = msg.text
    await msg.answer(text=text.question_6)
    await states.Questions.next()


async def question_7(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_6'] = msg.text
    await msg.answer(text=text.question_7)
    await states.Questions.next()


async def question_8(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_7'] = msg.text
    await msg.answer(text=text.question_8)
    await states.Questions.next()


async def question_9(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_8'] = msg.text
    await msg.answer(text=text.question_9)
    await states.Questions.next()


async def question_10(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_9'] = msg.text
    await msg.answer(text=text.question_10)
    await states.Questions.next()


async def write_answers_to_sheet(data, user_name):
    row = [str(user_name), str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')), data['question_1'], data['question_2'],
           data['question_3'], data['question_4'], data['question_5'], data['question_6'], data['question_7'],
           data['question_8'], data['question_9'], data['question_10']]
    worksheet.append_row(row, 2)


async def save_answers(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user_name = msg.from_user.full_name
        data['question_10'] = msg.text
        await write_answers_to_sheet(data, user_name)
    await msg.answer(text=text.save_answers)
    await state.finish()


def register(dp: Dispatcher):
    dp.register_callback_query_handler(question_1, text='questions_start', state=states.Questions.question_1)
    dp.register_message_handler(question_2, state=states.Questions.question_2)
    dp.register_message_handler(question_3, state=states.Questions.question_3)
    dp.register_message_handler(question_4, state=states.Questions.question_4)
    dp.register_message_handler(question_5, state=states.Questions.question_5)
    dp.register_message_handler(question_6, state=states.Questions.question_6)
    dp.register_message_handler(question_7, state=states.Questions.question_7)
    dp.register_message_handler(question_8, state=states.Questions.question_8)
    dp.register_message_handler(question_9, state=states.Questions.question_9)
    dp.register_message_handler(question_10, state=states.Questions.question_10)
    dp.register_message_handler(save_answers, state=states.Questions.save_answers)
