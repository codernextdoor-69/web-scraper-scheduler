import sqlite3

def clean_duplicates():
    conn = sqlite3.connect("scraped_data.db")
    c = conn.cursor()

    # Create a temporary table with distinct quotes only
    c.execute('''
        CREATE TABLE IF NOT EXISTS quotes_cleaned (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote TEXT UNIQUE,
            timestamp DATETIME
        )
    ''')

    # Insert only unique quotes from old table
    c.execute('''
        INSERT OR IGNORE INTO quotes_cleaned (quote, timestamp)
        SELECT quote, MIN(timestamp)
        FROM quotes
        GROUP BY quote
    ''')

    # Drop old table
    c.execute('DROP TABLE quotes')

    # Rename cleaned table to original name
    c.execute('ALTER TABLE quotes_cleaned RENAME TO quotes')

    conn.commit()
    conn.close()
    print("✅ Cleaned all duplicate quotes from the database.")

clean_duplicates()
