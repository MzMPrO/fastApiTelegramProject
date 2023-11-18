import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode

logging.basicConfig(level=logging.INFO)

TOKEN = '6516759967:AAE7DMlgc3zhpnENMbtGd9RVgybgBP4zO00'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI am your Echo Bot!")


@dp.message_handler(commands=['echo'])
async def echo_message(message: types.Message):
    await message.reply(message.text, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
