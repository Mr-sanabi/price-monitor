# Price Monitor

A simple Python tool that fetches a product page, extracts the product price, compares it with a target price, and saves price history.

## Features

- Fetches a product page using requests.
- Extracts page title and raw price using BeautifulSoup.
- Cleans raw price strings into numbers.
- Compares current price with target price.
- Compares current price with previous saved price.
- Saves current state to JSON.
- Appends price history to CSV.
- Uses config files for product URL, target price, currency and price selector.

## Tech Stack

- Python
- requests
- BeautifulSoup
- JSON
- CSV
- logging

## Current Status

MVP in progress.  
Works with a simple static product page from Books to Scrape.

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Create config.json based on config_example.json.

3. Run:
   python src/main.py

Current Status:
MVP works with a static product page from Books to Scrape.
