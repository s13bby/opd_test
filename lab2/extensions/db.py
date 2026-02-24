import sqlite3
#---------------------------------------------------------------------------------------
DATA_BASE = "users.db"
FOOD      = "food"
WATER     = "water"
COMFORT   = "comfort"
BALANCE   = "balance"
APPLES    = "apples"
#---------------------------------------------------------------------------------------
def init_db():
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        food INTEGER DEFAULT 50,
        water INTEGER DEFAULT 50,
        comfort INTEGER DEFAULT 50,
        balance INTEGER DEFAULT 10,
        apples INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()
    conn.close()
#---------------------------------------------------------------------------------------
def add_user(user_id, username):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
    conn.commit()
    conn.close()
#---------------------------------------------------------------------------------------
def get_all_users():
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    c.execute("SELECT user_id FROM users")
    result = [row[0] for row in c.fetchall()]
    conn.close()
    return result
#---------------------------------------------------------------------------------------
def get(user_id, that):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    match that:
        case "food":
            c.execute(f"SELECT {FOOD} FROM users WHERE user_id = ?", (user_id,))
        case "water":
            c.execute(f"SELECT {WATER} FROM users WHERE user_id = ?", (user_id,))
        case "comfort":
            c.execute(f"SELECT {COMFORT} FROM users WHERE user_id = ?", (user_id,))
        case "balance":
            c.execute(f"SELECT {BALANCE} FROM users WHERE user_id = ?", (user_id,))
        case "apples":
            c.execute(f"SELECT {APPLES} FROM users WHERE user_id = ?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0
#---------------------------------------------------------------------------------------
def increese(user_id, amount, that):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    match that:
        case "food":
            c.execute(f"UPDATE users SET {FOOD} = {FOOD} + ? WHERE user_id = ?", (amount, user_id))
        case "water":
            c.execute(f"UPDATE users SET {WATER} = {WATER} + ? WHERE user_id = ?", (amount, user_id))
        case "comfort":
            c.execute(f"UPDATE users SET {COMFORT} = {COMFORT} + ? WHERE user_id = ?", (amount, user_id))
        case "balance":
            c.execute(f"UPDATE users SET {BALANCE} = {BALANCE} + ? WHERE user_id = ?", (amount, user_id))
        case "apples":
            c.execute(f"UPDATE users SET {APPLES} = {APPLES} + ? WHERE user_id = ?", (amount, user_id))
    conn.commit()
    conn.close()
#---------------------------------------------------------------------------------------
def decreese(user_id, amount,that):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    match that:
        case "food":
            c.execute(f"UPDATE users SET {FOOD} = {FOOD} - ? WHERE user_id = ?", (amount, user_id))
        case "water":
            c.execute(f"UPDATE users SET {WATER} = {WATER} - ? WHERE user_id = ?", (amount, user_id))
        case "comfort":
            c.execute(f"UPDATE users SET {COMFORT} = {COMFORT} - ? WHERE user_id = ?", (amount, user_id))
        case "balance":
            c.execute(f"UPDATE users SET {BALANCE} = {BALANCE} - ? WHERE user_id = ?", (amount, user_id))
        case "apples":
            c.execute(f"UPDATE users SET {APPLES} = {APPLES} - ? WHERE user_id = ?", (amount, user_id))
    conn.commit()
    conn.close()
#---------------------------------------------------------------------------------------
def set_(user_id, amount, that):
    conn = sqlite3.connect(DATA_BASE)
    c = conn.cursor()
    match that:
        case "food":
            c.execute(f"UPDATE users SET {FOOD} = ? WHERE user_id = ?", (amount, user_id))
        case "water":
            c.execute(f"UPDATE users SET {WATER} = ? WHERE user_id = ?", (amount, user_id))
        case "comfort":
            c.execute(f"UPDATE users SET {COMFORT} = ? WHERE user_id = ?", (amount, user_id))
        case "balance":
            c.execute(f"UPDATE users SET {BALANCE} = ? WHERE user_id = ?", (amount, user_id))
        case "apples":
            c.execute(f"UPDATE users SET {APPLES} = ? WHERE user_id = ?", (amount, user_id))
    conn.commit()
    conn.close()
