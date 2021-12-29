import logging
import time
from db import check_user, coin_info, jump_check
from aiogram import Bot, Dispatcher, executor, types
import asyncio

# 123

API_TOKEN = '5010835487:AAH1cu1QtZzRZHi0RSWUdZzBM4VDzHPIgt0'



# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help', 'h', 's'])
async def send_welcome(message: types.Message):
    # db connect
    check_user(message.from_user.id, time.asctime())
    await message.reply(
        "Привет, я бот крипто-информатор!\nПредоставляю актуальную информацию о ТОНе (цена, изменение цены за последний час/сутки).\n\nВот список моих команд:\n/ton -Информация о TONCOIN.\n\nОбсуждение TON - тут: @TONcoinTrading")
    time.sleep(3)


# just for knowledge lol
@dp.message_handler(text='бот')
async def send_ask(message: types.Message):
    # db connect
    check_user(message.from_user.id, time.asctime())
    await message.reply(
        "Привет, я бот крипто-информатор!\nПредоставляю актуальную информацию о ТОНе (цена, изменение цены за последний час/сутки.\n\nВот список моих команд:\n/ton -Информация о TONCOIN.\n\nОбсуждение TON - тут: @TONcoinTrading")
    time.sleep(3)


@dp.message_handler(text='@GITBTbot')
async def send_ask1(message: types.Message):
    # db connect
    check_user(message.from_user.id, time.asctime())
    await message.reply(
        "Привет, я бот крипто-информатор!\nПредоставляю актуальную информацию о ТОНе (цена, изменение цены за последний час/сутки.\n\nВот список моих команд:\n/ton -Информация о TONCOIN.\n\nОбсуждение TON - тут: @TONcoinTrading")
    time.sleep(3)


# For chat ton
@dp.message_handler(commands=["ton"])
async def ton(message: types.Message):
    # db connect
    price, change1h, change24h = coin_info()
    check_user(message.from_user.id, time.asctime(), message.chat.id)
    message_ = f"TON/USD\nТекущая цена: {price}$\nИзменение в цене за последний час: {change1h}\nИзменение в цене за последние сутки: {change24h}"
    await message.reply(message_)
    time.sleep(5)


# For 1v1 dialog ton
@dp.message_handler(text=['TON/USD'])
async def ton(message: types.Message):
    # db connect
    price, change1h, change24h = coin_info()
    check_user(message.from_user.id, time.asctime(), message.chat.id)
    message_ = f"TON/USD\nТекущая цена: {price}$\nИзменение в цене за последний час: {change1h}\nИзменение в цене за последние сутки: {change24h}"
    await message.reply(message_)
    time.sleep(5)


# jump checker
async def jump():
    """background task which is created when bot starts"""
    while True:
        await asyncio.sleep(60)
        if jump_check():
            await bot.send_message(-1001784059306, "work")

async def start_check(dispatcher: Dispatcher):
    """List of actions which should be done before bot start"""
    asyncio.create_task(jump())  # creates background task




if __name__ == '__main__':
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    # bot start
    executor.start_polling(dp, skip_updates=True, on_startup=start_check)

