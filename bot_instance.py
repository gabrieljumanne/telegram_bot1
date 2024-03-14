from aiogram import Bot
from token_api import token_api

bot_ = Bot(
    token=token_api,
    parse_mode="HTML"
)
