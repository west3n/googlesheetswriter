## <p align="center">Question Handler in Google Sheets Bot </p>
### <p align="center">This is a simple template for a Telegram Bot that can save answers in Google Sheets table. To start using this bot, you need to follow these steps:</p>
* Ask @BotFather for a [new token](https://core.telegram.org/bots/tutorial#obtain-your-bot-token) for you bot.
* Go to Google API Console through your account (https://console.developers.google.com).
* Create a new project.
* Open the "Credentials" section.
* Click on "Create credentials" and select "Service account".
* Fill in the Service account name field. Choose a name at your discretion. Service account ID will be generated automatically (you can manually edit it, but it's not required).
* At the bottom, under Service account ID, there will be an e-mail address. It needs to be saved (!)
* Click "Create and continue". Choose Basic -> Editor for "role", then "Continue", then "Done".
* Now you need to go to the created Service account, in the Keys section select Add key -> Create new key -> JSON. A file should start downloading. You need to create folder "json" into project and put this file to this folder!
* Go to the link (https://console.cloud.google.com/apis/library/sheets.googleapis.com), click "Enable".
* Using the same account, create a table where the data will be entered. In this table, in the "Access settings" section, grant access by email with editor function, which you saved in previous steps.
* Replace **"YOUR_TOKEN_HERE"** and **"YOUR_SHEET_URL_HERE"** with your actual token and sheet url in the **.env.example** file. Then rename **.env.example** to **.env.**
* Replace **name_of_your_json_file** with your actual json file [here](https://github.com/west3n/googlesheetswriter/blob/a0cf7a1b5364e4092c06a447454d18e31924f83a/handlers/questions.py#LL11-L11C54)
* Install all the required libraries by running `pip install -r requirements.txt`.
## <p align="center">That's it!</p>
