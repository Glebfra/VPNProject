import asyncio
import os

from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(os.getenv('BOT_TOKEN'))


@bot.message_handler(commands=['start'])
async def welcome(message):
    text = 'Привет! Я бот, который раздает ключи. Напиши /key, чтобы получить ключ.'
    await bot.reply_to(message, text)


asyncio.run(bot.polling())
