from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def generate_start_translate():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text='Начать перевод')
    markup.add(btn)
    return markup


def generate_what_next(lang):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    new = KeyboardButton(text='Выбрать другой язык')
    again = KeyboardButton(text=f'Оставить язык: {lang}')
    markup.row(new, again)
    return markup
