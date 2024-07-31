import asyncio
import os

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from telebot.async_telebot import AsyncTeleBot

from src.models.DynamicKey import DynamicKey
from src.models.OutlineKey import OutlineKey
from src.outline.Outline import Outline

bot = AsyncTeleBot(os.getenv('BOT_TOKEN'))


@bot.message_handler(commands=['start'])
async def welcome(message):
    text = 'Привет! Я бот, который раздает ключи. Напиши /key, чтобы получить ключ'
    await bot.reply_to(message, text)


@bot.message_handler(commands=['key'])
async def get_key(message):
    user_id = message.from_user.id

    try:
        key = Outline().get_dynamic_key(user_id)
    except ValueError:
        key = Outline().generate_dynamic_key(user_id)

    await bot.reply_to(message, key)


asyncio.run(bot.polling())
