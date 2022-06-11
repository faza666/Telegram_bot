# Telegram_bot
This script uses Telegram Bot as frontend of simple application, wich goes to www.yobit.net,
  picks up current rate **Bitсoin to USD** and send it out back to the Telegram Bot.

### Telegram Bot API documentation you may view on https://core.telegram.org/bots/api
### Yobit API documentation you may view on https://yobit.net/en/api/

### To run this script you need to:
  - Create Telegram Bot :
    * Run the Telegram app on your phone
    * Find **BotFather** through chat serch servis
    * Create the chatBot following instructions..
    * **Save the token** you will receive at the end of the bot creation procedure
  - Install python interpreter version 3.10+ from:
    * https://www.python.org/;
  - Create virtual environment with **cli command**:
    * **python3 -m venv venv**;
  - Activate the virtual environment with:
    * **source venv/bin/activate**;
  - Install all dependencies to your virtual environment from 'requirements.txt' with:
    * **pip install -r requirements.txt**;
  - Run the csript;
  - Open new chat with just created chatbot and send a message to him:
     * **/btc**
  - Enjoy :)
