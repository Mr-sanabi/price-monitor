import logging
import json
from datetime import datetime
from price_cleaner import clean_price
from storage import load_json, save_json, save_csv, load_previous_price
from price_checker import price_compare, compare_previous_price
from fetcher import fetch_page
from parser import extract_title, extract_price
from product_builder import build_product_data


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s (%(levelname)s) %(message)s",
    handlers=[
        logging.FileHandler("log.txt", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def main():
    logging.info("Price Monitor started")

    # Load conifg

    config = load_json("config.json")
    target_price = config["price"]["target_price"]
    currency = config["price"]["currency"]
    product_url = config["price"]["product_url"]
    price_selector = config["scraping"]["price_selector"]

    # Fetch Page and extract title
    
    html = fetch_page(product_url, config)


    if html is not None:
        title = extract_title(html)
        logging.info(f"Page title: {title}")
    else:
        logging.error("HTML is not available")
        return

    logging.info(f"Product_url: {product_url}")
    logging.info(f"Target_price: {target_price}")
    logging.info(f"Currency: {currency}")

    # Temporary parser test with sample HTML


    raw_price = extract_price(html, price_selector)

    if raw_price is not None:
        logging.info(f"Raw price: {raw_price}")
        current_price = clean_price(raw_price)
    else:
        logging.error("Raw price not found")
        return

    target_price_status = price_compare(current_price, target_price) 

    logging.info(f"Target price status: {target_price_status}")
    logging.info(f"Current price: {current_price}")
    logging.info(f"Target price: {target_price}")

    checked_at = datetime.now().isoformat(timespec="seconds")

    previous_price = None

    previous_price = load_previous_price("data/current_price.json")

    price_change, price_change_status = compare_previous_price(current_price, previous_price)

    logging.info(f"Price change: {price_change}")
    logging.info(f"Price change status: {price_change_status}")

    # Build product data

    product_data = build_product_data(
        product_url,
        title,
        current_price,
        target_price,
        currency,
        target_price_status,
        checked_at,
        previous_price,
        price_change,
        price_change_status
    )

    # Save data

    save_json("data/current_price.json", product_data)
    save_csv("data/price_history.csv", product_data)
    logging.info("Current price and history saved successfully")
    logging.info(f"Product data: {product_data}")

if __name__ == "__main__":
    main()