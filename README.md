# 🕷️ Automated Web Scraper with Scheduler

This project is a Python-based automated web scraper that periodically scrapes quotes from a demo website and stores them in a local SQLite database. It also provides a CSV export feature for all scraped data via a Flask web interface.

---

## 🚀 Features

- Scrapes quotes every 60 seconds using `BeautifulSoup`
- Avoids duplicate entries using a UNIQUE constraint
- Stores data in a lightweight `SQLite` database
- Exports scraped quotes to `scraped_data.csv`
- Simple web interface with download button (powered by Flask)

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask** – Web framework
- **BeautifulSoup** – HTML parsing
- **SQLite** – Local database
- **Threading** – Background scraping
- **CSV** – Export functionality

---

## 🌐 Live Demo

> 🔗 [https://replit.com/@mdshoaibiqbal9/web-scraper-scheduler]

---

## 📁 Project Structure
web-scraper/
├── main.py # Flask web server
├── scraper.py # Scrapes quotes from the website
├── db.py # Initializes DB and inserts data
├── export.py # Exports quotes to CSV
├── scraped_data.db # SQLite database (auto-created)
├── scraped_data.csv # Output CSV file (auto-updated)
└── requirements.txt # Python dependencies
 2. Install dependencies
 pip install -r requirements.txt
3. Run the project
python3 main.py



