import calendar
import logging, time
from aiogram import Bot, Dispatcher, executor, types
#from keyboard import coin_board
from coins_init import  get_btc, get_eth, get_ton
API_TOKEN = '5010835487:AAH1cu1QtZzRZHi0RSWUdZzBM4VDzHPIgt0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)




#reply_markup=coin_board
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer("Привет, я бот крипто-информатор!\nПредоставляю актуальную информацию о выбранной криптовалюте (цена, изменение цены за последний час/сутки.\n\nВот список моих команд:\n/ton -Информация о TONCOIN.")

# just for knowledge lol
@dp.message_handler(text = 'бот')
async def send_ask(message: types.Message):
    await message.answer("Привет, я бот крипто-информатор!\nПредоставляю актуальную информацию о выбранной криптовалюте (цена, изменение цены за последний час/сутки.\n\nВот список моих команд:\n/ton -Информация о TONCOIN.\n/btc - Информация о биткоине.\n/eth - Информация об эфире.")

#For chats btc
#@dp.message_handler(commands=["btc"])
async def btc(message: types.Message):
    btc = get_btc()
    message_ = f"{btc.baseCurrency}/{btc.quoteCurrency}\nТекущая цена: {btc.price}$\nИзменение в цене за последний час: {btc.change1h}\nИзменение в цене за последние сутки: {btc.change24h}"
    await message.reply(message_)

#For 1v1 dialog btc
#@dp.message_handler(text='BTC/USD')
async def btc(message: types.Message):
    btc = get_btc()
    message_ = f"{btc.baseCurrency}/{btc.quoteCurrency}\nТекущая цена: {btc.price}$\nИзменение в цене за последний час: {btc.change1h}\nИзменение в цене за последние сутки: {btc.change24h}"
    await message.reply(message_)

#For chat eth
#@dp.message_handler(commands=["eth"])
async def eth(message: types.Message):
    eth = get_eth()
    message_ = f"{eth.baseCurrency}/{eth.quoteCurrency}\nТекущая цена: {eth.price}$\nИзменение в цене за последний час: {eth.change1h}\nИзменение в цене за последние сутки: {eth.change24h}"
    await message.reply(message_)

#For 1v1 dialog eth
#@dp.message_handler(text='ETH/USD')
async def eth(message: types.Message):
    eth = get_eth()
    message_ = f"{eth.baseCurrency}/{eth.quoteCurrency}\nТекущая цена: {eth.price}$\nИзменение в цене за последний час: {eth.change1h}\nИзменение в цене за последние сутки: {eth.change24h}"
    await message.reply(message_)


# For chat ton
#@dp.message_handler(commands=["ton"])
async def ton(message: types.Message):
    ton = get_ton()
    message_ = f"{ton.baseCurrency}/{ton.quoteCurrency}\nТекущая цена: {ton.price}$\nИзменение в цене за последний час: {ton.change1h}\nИзменение в цене за последние сутки: {ton.change24h}"
    await message.reply(message_)

#For 1v1 dialog ton
@dp.message_handler(text='TONCOIN/USD')
async def ton(message: types.Message):
    ton = get_ton()
    message_ = f"{ton.baseCurrency}/{ton.quoteCurrency}\nТекущая цена: {ton.price}$\nИзменение в цене за последний час: {ton.change1h}\nИзменение в цене за последние сутки: {ton.change24h}"
    await message.reply(message_)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


while True:
    time.sleep(1)
    print(time.asctime())