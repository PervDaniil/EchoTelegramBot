import env
from aiogram import Bot, Dispatcher
from aiogram.types import Message, BotCommand
from aiogram.filters import Command, CommandStart


bot = Bot(env.API_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def greet_message(message: Message):
    await message.answer('Welcome!')
    

@dp.message()
async def handle_incoming_message(message: Message):
    await message.answer(message.text)


async def start():
    await dp.start_polling(bot)