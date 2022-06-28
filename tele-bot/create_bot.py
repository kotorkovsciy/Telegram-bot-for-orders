from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot
import os


bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher(bot, storage=MemoryStorage())
