import os
from dotenv import load_dotenv
from telebot import TeleBot
from telebot.types import Message
from helpers import get_location_info
from keyboard import Keyboard

load_dotenv()
bot = TeleBot(os.getenv("TOKEN"), parse_mode="HTML")


@bot.message_handler(commands=["start"])
def start(msg: Message) -> None:
    bot.send_message(
        msg.from_user.id,
        f"Надішліть локацію, що вас цікавить 🤔",
        reply_markup=Keyboard.send_location(),
    )


@bot.message_handler(content_types=["location"])
def on_location(msg: Message) -> None:
    coords = (msg.location.latitude, msg.location.longitude)
    info = get_location_info(coords)

    bot.send_message(
        msg.from_user.id,
        f"""
💨 <b>Якість повітря: {info['air']['value']}</b> - зафіксовано за {info['air']['distance']}км
            
🟢 Добрий рівень: 0-50
🟡 Помірний рівень: 51-100
🟠 Шкідливий рівень для чутливих груп: 101-150
🔴 Шкідливий рівень: 151-200
🟣 Дуже шкідливий рівень: 201-300
🟤 Небезпечний рівень: 301+

☢️ <b>Рівень радіації: {info['rad']['value']} нЗв/год</b> - зафіксовано за {info['rad']['distance']}км
ℹ️ Допустиме значення рівня радіаційного фону: 300 нЗв/год
        """,
        reply_markup=Keyboard.remove(),
    )


bot.infinity_polling()
