import sqlite3




# db connect
conn = sqlite3.connect('data.db')
cur = conn.cursor()
def db(user_id, time):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('''INSERT OR IGNORE INTO user (user_id) VALUES (?)''', (user_id,))
    cur.execute('''UPDATE user SET time = ? WHERE user_id = ?''', (time, user_id))
    conn.commit()





conn.close()