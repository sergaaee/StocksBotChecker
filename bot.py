import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5010835487:AAH1cu1QtZzRZHi0RSWUdZzBM4VDzHPIgt0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer("Привет, я бот крипто-информатор! \n Что тебя интересует?", reply_markup=coin_board)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

@dp.message_handler(text='ETH/USD')
async def eth(message: types.Message):
    eth = get_eth()
    message_ = f"{eth.baseCurrency}/{eth.quoteCurrency}\nТекущая цена: {eth.price}$\nИзменение в цене за последний час: {eth.change1h}\nИзменение в цене за последние сутки: {eth.change24h}"
    await message.answer(message_)

@dp.message_handler(text='TONCOIN/USD')
async def ton(message: types.Message):
    ton = get_ton()
    message_ = f"{ton.baseCurrency}/{ton.quoteCurrency}\nТекущая цена: {ton.price}$\nИзменение в цене за последний час: {ton.change1h}\nИзменение в цене за последние сутки: {ton.change24h}"
    await message.answer(message_)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
