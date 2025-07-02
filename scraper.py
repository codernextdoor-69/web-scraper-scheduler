import requests
from bs4 import BeautifulSoup

def scrape():
    all_quotes = []
    base_url = "https://quotes.toscrape.com/page/{}/"
    page = 1

    while True:
        url = base_url.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("span", class_="text")
        if not quotes:
            break  # No more pages

        for quote in quotes:
            all_quotes.append(quote.get_text())

        page += 1  # Go to next page

    return all_quotes
