from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


coin_board = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('BTC/USD'),
    KeyboardButton('ETH/USD'),
    KeyboardButton('TONCOIN/USD')
)