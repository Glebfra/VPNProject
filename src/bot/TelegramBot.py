import os

from telebot.async_telebot import AsyncTeleBot

from src.outline.Outline import Outline

bot = AsyncTeleBot(os.getenv('BOT_TOKEN'))


@bot.message_handler(commands=['start'])
async def welcome(message):
    text = 'Привет! Я бот, который раздает ключи. Напиши /key, чтобы получить ключ'
    await bot.reply_to(message, text)


@bot.message_handler(commands=['key'])
async def get_key(message):
    user_id = message.from_user.id
    outline = Outline()

    try:
        key = outline.get_dynamic_key(user_id)
    except ValueError:
        key = outline.create_dynamic_key(user_id)

    await bot.reply_to(message, key)
