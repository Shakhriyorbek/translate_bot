from telebot.types import Message, CallbackQuery
from data.loader import bot, db
from data.configs import LANGUAGES
from googletrans import Translator
from keyboards.reply import generate_what_next


@bot.callback_query_handler(lambda call: call.data in LANGUAGES.keys())
def get_lang_ask_text(call: CallbackQuery):
    chat_id = call.message.chat.id
    message_id = call.message.id
    lang = call.data
    bot.delete_message(chat_id, message_id)
    bot.send_message(chat_id, f'Вы выбрали язык {LANGUAGES[lang]}')
    msg = bot.send_message(chat_id, 'Введите текст, который вы хотите перевести')
    bot.register_next_step_handler(msg, get_text, lang)


def get_text(message: Message, lang):
    chat_id = message.chat.id
    text = message.text
    shahriyor = Translator()
    try:
        translated_text = shahriyor.translate(text=text, dest=lang, src='ru').text
        pronunciation = shahriyor.translate(text=text, dest=lang, src='ru').pronunciation
        bot.send_message(chat_id, f'{translated_text}\n{pronunciation}', reply_markup=generate_what_next(LANGUAGES[lang]))
        db.save_data(chat_id, 'ru', lang, text, translated_text)
    except:
        msg = bot.send_message(chat_id, 'Не удалось перевести. Пробуйте снова')
        bot.register_next_step_handler(msg, get_text, lang)
