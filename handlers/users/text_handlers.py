from telebot.types import Message, ReplyKeyboardRemove
from data.loader import bot
from keyboards.inline import generate_languages
from data.configs import LANGUAGES
from .call_back import get_text


@bot.message_handler(regexp='(Начать перевод|Выбрать другой язык)')
def reaction_to_start(message: Message):
    chat_id = message.chat.id

    text = '''Выберите язык, на который перевести'''
    bot.send_message(chat_id, 'Перевод начат', reply_markup=ReplyKeyboardRemove())
    bot.send_message(chat_id, text, reply_markup=generate_languages())


@bot.message_handler(regexp='Оставить язык: [A-Za-z]+')
def reaction_to_again(message: Message):
    chat_id = message.chat.id
    text = message.text
    lang_value = text.split(': ')[1]
    lang = get_key(lang_value)
    bot.send_message(chat_id, f'Вы выбрали язык {LANGUAGES[lang]}')
    msg = bot.send_message(chat_id, 'Введите текст, который вы хотите перевести')
    bot.register_next_step_handler(msg, get_text, lang)


def get_key(value):
    for k, v in LANGUAGES.items():
        if v == value:
            return k
