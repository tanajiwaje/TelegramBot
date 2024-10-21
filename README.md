# TelegramBot
Step 1:Create a Telegram Account
  if you dont already have a telegram account,download the telegram app on your phone or desktop and sign up.

Step 2:Create a new Bot using BotFather
  *Open Telegram and search for BotFather,which is an official bot provided by     Telegram to manage other bots

  *Start a chat with BotFather by clicking the "Start" Button

  *Create a new bot
    >Type /newbot and press enter.
    >BotFather will ask you to choose a name for your bot.This can be               anything,such as "myfirstbot"
    >After choosing the bot's name, you will be asked to choose a username for
    the bot, which must end in "bot"(eg."my_test_bot").
    

Step 3:Get the bot token:
  >after creating the bot, BotFather will send a message containing your bot's token. The token will look someting like this :
  123456789:ABCdefghtIJKlmdofjrrtrd_ddfhdffSDERED.
  >Keep this token safe, as it will be used to authenticate your bot when sending or receiving message.

Step 4:Get your user chat ID
  To interact with your bot programmatically, you will need your chat ID.
  >Start a conversation with your bot:
   Search for your bot's username(eg."my_test_bot") and start a chat by clicking the "start" button.
  >Get your chat ID:
  >open your web browser and navigate to the following URL, replacing <YOUR_BOT_TOKEN> with the token you received from BotFather:
  >https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates

Step 5 :Check the response 
  You will see the JSON response that contains information about the chat,
  including the chat ID
  Look for the "chat" section in the JSON response. It will look something like:
  {
  "update_id": 123456789,
  "message": {
    "message_id": 1,
    "from": {
      "id": 1811705004,  // This is the chat ID
      "is_bot": false,
      "first_name": "John",
      "last_name": "Doe",
      "username": "john_doe",
      "language_code": "en"
    },
    "chat": {
      "id": 1811705004,  // This is also the chat ID
      "first_name": "John",
      "last_name": "Doe",
      "username": "john_doe",
      "type": "private"
    },
    "date": 1609459200,
    "text": "/start"
   }
   }

step 6: Write code in any programming language then check the result 
 for example i wrote code in python 

  

  
