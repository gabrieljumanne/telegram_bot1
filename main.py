import asyncio 
from aiogram import  Dispatcher
from bot_instance import bot_
from bot.handlers.user_handlers import user_router_

# a synchronous function 
def register_routers(dp: Dispatcher)->None:
    """ Register Routers in the dispatcher(Root router) """
    
    dp.include_router(user_router_)




async def main()->None:
    """The main function that will execute our event loop and start polling."""

    dp = Dispatcher()
    # registered routers .. 
    register_routers(dp)

    await dp.start_polling(bot_)



# basic edm 
if __name__ == "__main__":
    asyncio.run(main()) 