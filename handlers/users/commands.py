from data.loader import bot, db
from telebot.types import Message
from keyboards.reply import generate_start_translate


@bot.message_handler(commands=['start', 'help', 'about'])
def commands(message: Message):
    chat_id = message.chat.id
    if message.text == '/start':
        bot.send_message(chat_id, 'Здравствуйте, я бот переводчик, для начала перевода нажмите на кнопку',
                         reply_markup=generate_start_translate())
    elif message.text == '/help':
        bot.send_message(chat_id, '''Если у вас возникла ошибку или есть предложения
Напишите в наш тех. поддержку: @Very_Good_One''')
    elif message.text == '/history':
        data = db.select_data(chat_id)
        return bot.send_message(chat_id, f'''История\n{data}''')
    else:
        bot.send_message(chat_id, '''Этот бот был сделан для помощи другим, а на остальное мне все равно.
Пишите /help для жалоб. Все равно не смотрю''')




