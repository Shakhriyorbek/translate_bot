from telebot import TeleBot
from .configs import TOKEN
from database.database import Database

bot = TeleBot(TOKEN)

db = Database()

