from aiogram import types
from fastapi import FastAPI

from bot import TOKEN, bot, dp, Dispatcher, Bot

app = FastAPI()
WEBHOOK_PATH = f"/bot/{TOKEN}"
WEBHOOK_URL = f"https://0a15-84-54-66-148.ngrok-free.app" + WEBHOOK_PATH


@app.on_event("startup")
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL)


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.on_event("shutdown")
async def on_shutdown():
    pass
