import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

API_TOKEN = '7987427447:AAE6vFnFIQve_u5MCaCQSX4Yuh_SwgMwc3g'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я бот помогающий твоему здоровью")

@dp.message_handler()
async def all_messages(message: types.Message):

    await message.reply(f"Введите команду /start,чтобы начать общение: {message.text}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)