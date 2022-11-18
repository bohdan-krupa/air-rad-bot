from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


class Keyboard:
    def __new__(self, *buttons) -> ReplyKeyboardMarkup:
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        _ = [keyboard.add(*i) for i in buttons]

        return keyboard

    @classmethod
    def send_location(cls):
        button_geo = KeyboardButton(text=" Надіслати локацію 🌍", request_location=True)

        return cls((button_geo,))

    @classmethod
    def remove(_):
        return ReplyKeyboardRemove()
