from flask import Flask, send_file
from scraper import scrape
from db import init_db, insert_quotes
from export import export_to_csv
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
init_db()

# Schedule scraping job
scheduler = BackgroundScheduler()
def scrape_job():
    quotes = scrape()
    insert_quotes(quotes)
    export_to_csv()  # Automatically update CSV after scraping
    print(f"Inserted {len(quotes)} quotes.")

scheduler.add_job(scrape_job, 'interval', seconds=60)
scheduler.start()

@app.route('/')
def home():
    return '''
        <h2>Web Scraper is Running</h2>
        <p>Scrapes every 60 seconds.</p>
        <a href="/download">📥 Download CSV</a>
    '''

@app.route('/download')
def download_csv():
    export_to_csv()  # Make sure file is up to date
    return send_file('scraped_data.csv', as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
