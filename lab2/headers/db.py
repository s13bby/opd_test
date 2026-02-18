import sqlite3

DATA_BASE = 'users.db'
#---------------------------------------------------------------------------------------
def init_db():
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        food INTEGER DEFAULT 50,
        water INTEGER DEFAULT 50,
        comfort INTEGER DEFAULT 50,
        balance INTEGER DEFAULT 100,
        apples INTEGER DEFAULT 0,
        carrot INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()
#---------------------------------------------------------------------------------------
def add_user(user_id, username):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)', (user_id, username))
    conn.commit()
    conn.close()
#---------------------------------------------------------------------------------------
def get_user_food(user_id):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('SELECT food FROM users WHERE user_id = ?', (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

def get_user_water(user_id):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('SELECT water FROM users WHERE user_id = ?', (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

def get_user_comfort(user_id):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('SELECT comfort FROM users WHERE user_id = ?', (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

def get_user_balance(user_id):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('SELECT balance FROM users WHERE user_id = ?', (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

def get_user_apples(user_id):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('SELECT apples FROM users WHERE user_id = ?', (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

def get_user_carrots(user_id):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('SELECT carrot FROM users WHERE user_id = ?', (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0
#---------------------------------------------------------------------------------------
def increese_food(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET food = food + ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()

def increese_water(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET water = water + ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()

def increese_comfort(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET comfort = comfort + ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()

def increese_balance(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET balance = balance + ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()

def increese_apples(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET apples = apples + ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()

def increese_carrots(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET carrot = carrot + ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()
#---------------------------------------------------------------------------------------
def decreese_food(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET food = food - ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()

def decreese_water(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET water = water - ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()

def decreese_comfort(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET comfort = comfort - ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()

def decreese_balance(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET balance = balance - ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()

def decreese_apples(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET apples = apples - ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()

def decreese_carrots(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET carrot = carrot - ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()
#---------------------------------------------------------------------------------------
def set_food(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET food = ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()

def set_water(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET water = ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()

def set_comfort(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET comfort = ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()

def set_balance(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET balance = ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()

def set_apples(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET apples = ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()

def set_carrots(user_id, amount):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute('UPDATE users SET carrot = ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()