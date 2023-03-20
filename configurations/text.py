from decouple import config

url = config("SHEET_URL")

question_1 = "What is your favorite fruit?"
question_2 = "Do you prefer staying up late or waking up early?"
question_3 = "What is 2+2?"
question_4 = "What is your favorite season?"
question_5 = "What is the meaning of life?"
question_6 = "Do you prefer sweet or savory foods?"
question_7 = "Who is your favorite musician?"
question_8 = "What did you eat for breakfast today?"
question_9 = "Which do you prefer: city or countryside?"
question_10 = "What is your favorite animal?"
save_answers = f'Congratulations on completing the test!<a href="{url}"> Here</a> is the table with the answers.'
