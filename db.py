import sqlite3
from coin_init import get_ton



# db connect
conn = sqlite3.connect('data.db')
cur = conn.cursor()
def check_user(user_id, time):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('''INSERT OR IGNORE INTO user (user_id) VALUES (?)''', (user_id,))
    cur.execute('''UPDATE user SET time = ? WHERE user_id = ?''', (time, user_id))
    conn.commit()


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
    return [price, change1h, change24h]
conn.close()