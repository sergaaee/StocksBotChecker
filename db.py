import sqlite3
from coin_init import get_ton


# Adding user_id and time of his last massage to the database
def check_user(user_id, time, chat_id):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('''INSERT OR IGNORE INTO user (user_id) VALUES (?)''', (user_id,))
    cur.execute('''UPDATE user SET time = ?, chat_id = ? WHERE user_id = ?''', (time, chat_id, user_id))
    conn.commit()
    conn.close()


# getting actual info about TON
def coin_info():
    info = get_ton()
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('''UPDATE coin SET price =?, change1h = ?, change24h = ? WHERE name = ? ''', (info.price, info.change1h, info.change24h, "TON"))
    conn.commit()

    cur.execute('''SELECT price from coin where name = ?''', ("TON",))
    price = float(cur.fetchone()[0])
    cur.execute('''SELECT change1h from coin where name = ?''', ("TON",))
    change1h = str(cur.fetchone()[0])
    cur.execute('''SELECT change24h from coin where name = ?''', ("TON",))
    change24h = str(cur.fetchone()[0])
    conn.close()
    return [price, change1h, change24h]

#check for pump/dump
def jump_check():
    info = get_ton()
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    last_price = info.price
    cur.execute('''SELECT price from coin where name = ?''', ("TON",))
    price = float(cur.fetchone()[0])
    jump = price - last_price # вычитаем из старой стоимости новую(обновленную только что)
    if abs(jump) >= price/10:
        return True
    conn.close()
    return False
