from data.loader import bot, db
import handlers

if __name__ == '__main__':
    db.create_table()
    bot.infinity_polling()

