import sqlite3
import csv

def export_to_csv(filename="scraped_data.csv"):
    conn = sqlite3.connect("scraped_data.db")
    c = conn.cursor()
    c.execute("SELECT * FROM quotes")
    rows = c.fetchall()
    conn.close()

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Quote", "Timestamp"])
        writer.writerows(rows)
