from aiogram import Dispatcher, types


async def cmd_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! я бот-магазин здоровых напитков, для ознакомления с ассортиментом нажмите на кнопку \"Магазин\"")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
