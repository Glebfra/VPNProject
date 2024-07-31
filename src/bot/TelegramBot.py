import asyncio
import os

from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(os.getenv('BOT_TOKEN'))


@bot.message_handler(commands=[''])
async def welcome(message):
    text = 'Hello World!'
    await bot.reply_to(message, text)


asyncio.run(bot.polling())
