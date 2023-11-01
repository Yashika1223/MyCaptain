import requests
from bs4 import BeautifulSoup
import sqlite3

# Function to create a table in the database
def create_table():
    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS quotes (text TEXT, author TEXT, tags TEXT)''')
    conn.commit()
    conn.close()

#site used : http://quotes.toscrape.com/
#to scrape quotes & store them in the database
def scrape_and_store_quotes():
    url = 'http://quotes.toscrape.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')

    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()

    for quote, author, tag in zip(quotes, authors, tags):
        text = quote.get_text()
        author_name = author.get_text()
        tag_text = [tag.get_text() for tag in tag.find_all('a')]
        tags = ', '.join(tag_text)

        #store data in database
        c.execute("INSERT INTO quotes (text, author, tags) VALUES (?, ?, ?)", (text, author_name, tags))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    scrape_and_store_quotes()
