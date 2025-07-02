import sqlite3

def init_db():
    conn = sqlite3.connect("scraped_data.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote TEXT UNIQUE,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_quotes(quotes):
    conn = sqlite3.connect("scraped_data.db")
    c = conn.cursor()
    for q in quotes:
        try:
            c.execute("INSERT INTO quotes (quote) VALUES (?)", (q,))
        except sqlite3.IntegrityError:
            # Skip duplicate quotes
            continue
    conn.commit()
    conn.close()
