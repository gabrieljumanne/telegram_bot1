from aiogram.filters import Command
from aiogram import Router, types

# this is like minimalist dispature class / object 
# user router for the all message 
user_router_ = Router()

# decorator function from Router
@user_router_.message(Command("start"))
async def cmd_start(msg: types.Message)->None:
    """process the command`start` """
    # message object is created ... 
    await msg.answer(
        "hello welcome to <b>Castorosa bot!</b>"
    )