from telebot.types import Update
from bot import bot


def lambda_handler(event, _):
    update = Update.de_json(event["body"])
    bot.process_new_updates([update])

    return {"statusCode": 200}
