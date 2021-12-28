import logging
import time
from db import check_user, coin_info
from aiogram import Bot, Dispatcher, executor, types
#from keyboard import coin_board
from coins_init import get_ton
API_TOKEN = '5010835487:AAH1cu1QtZzRZHi0RSWUdZzBM4VDzHPIgt0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)





#reply_markup=coin_board
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    # db connect
    check_user(message.from_user.id, time.asctime())
    await message.reply(
        "Привет, я бот крипто-информатор!\nПредоставляю актуальную информацию о ТОНе (цена, изменение цены за последний час/сутки.\n\nВот список моих команд:\n/ton -Информация о TONCOIN.\n\nОбсуждение TON - тут: @TONcoinTrading")

# just for knowledge lol
@dp.message_handler(text = 'бот')
async def send_ask(message: types.Message):
    # db connect
    check_user(message.from_user.id, time.asctime())
    await message.reply(
        "Привет, я бот крипто-информатор!\nПредоставляю актуальную информацию о ТОНе (цена, изменение цены за последний час/сутки.\n\nВот список моих команд:\n/ton -Информация о TONCOIN.\n\nОбсуждение TON - тут: @TONcoinTrading")

@dp.message_handler(text = '@GITBTbot')
async def send_ask(message: types.Message):
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

#For 1v1 dialog ton
@dp.message_handler(text='TONCOIN/USD')
async def ton(message: types.Message):
    # db connect
    price, change1h, change24h = coin_info()
    check_user(message.from_user.id, time.asctime())
    message_ = f"TON/USD\nТекущая цена: {price}$\nИзменение в цене за последний час: {change1h}\nИзменение в цене за последние сутки: {change24h}"
    await message.reply(message_)
    time.sleep(5)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
