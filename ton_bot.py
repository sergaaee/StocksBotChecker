import logging
import time
from db import check_user, coin_info
from aiogram import Bot, Dispatcher, executor, types
import asyncio

# 123

API_TOKEN = '5068408579:AAGEJYcgmuaileUgpZZAqg8BdLLBr1MITS8'

# Configure logging
logging.basicConfig(level=logging.INFO)

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
    check_user(message.from_user.id, time.asctime())
    message_ = f"TON/USD\nТекущая цена: {price}$\nИзменение в цене за последний час: {change1h}\nИзменение в цене за последние сутки: {change24h}"
    await message.reply(message_)
    time.sleep(5)


# For 1v1 dialog ton
@dp.message_handler(text=['TON/USD'])
async def ton(message: types.Message):
    # db connect
    price, change1h, change24h = coin_info()
    check_user(message.from_user.id, time.asctime())
    message_ = f"TON/USD\nТекущая цена: {price}$\nИзменение в цене за последний час: {change1h}\nИзменение в цене за последние сутки: {change24h}"
    await message.reply(message_)
    time.sleep(5)


async def _bot():
    executor.start_polling(dp, skip_updates=True)


async def _get_check():
    try:
        while True:
            # request
            await bot.send_message(479449574, "213")
            time.sleep(30)

    except:
        return False


async def main():
    bot_loop = loop.create_task(_bot())
    demon = loop.create_task(_get_check())
    await asyncio.wait([bot_loop, demon])


if __name__ == '__main__':

    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except:
        print('ERROR')
