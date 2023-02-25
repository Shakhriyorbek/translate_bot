from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.configs import LANGUAGES


def generate_languages():
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = []
    for key, lang in LANGUAGES.items():
        btn = InlineKeyboardButton(text=lang, callback_data=key)
        buttons.append(btn)
    markup.add(*buttons)
    return markup
