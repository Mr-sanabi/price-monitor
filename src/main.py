import argparse
import logging
from datetime import datetime, timezone
from pathlib import Path

from src.fetcher import fetch_page
from src.parser import extract_price, extract_title
from src.price_checker import compare_previous_price, price_compare
from src.price_cleaner import clean_price
from src.product_builder import build_product_data
from src.storage import load_json, load_previous_price, save_csv, save_json


def parse_args():
    parser = argparse.ArgumentParser(description="Monitor a product page and record price changes.")
    parser.add_argument("--config", default="config.json", help="Path to the JSON configuration file")
    return parser.parse_args()


def configure_logging(log_file):
    path = Path(log_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s (%(levelname)s) %(message)s",
        handlers=[logging.FileHandler(path, encoding="utf-8"), logging.StreamHandler()],
    )


def run(config):
    price_config = config["price"]
    scraping = config["scraping"]
    output = config.get("output", {})
    current_path = output.get("current_price", "data/current_price.json")
    history_path = output.get("history", "data/price_history.csv")

    html = fetch_page(price_config["product_url"], config)
    if html is None:
        return None

    raw_price = extract_price(html, scraping["price_selector"])
    if raw_price is None:
        logging.error("Raw price not found")
        return None

    current_price = clean_price(raw_price)
    previous_price = load_previous_price(current_path)
    change, change_status = compare_previous_price(current_price, previous_price)
    product = build_product_data(
        price_config["product_url"], extract_title(html), current_price,
        price_config["target_price"], price_config["currency"],
        price_compare(current_price, price_config["target_price"]),
        datetime.now(timezone.utc).isoformat(timespec="seconds"), previous_price,
        change, change_status,
    )
    save_json(current_path, product)
    save_csv(history_path, product)
    return product


def main():
    args = parse_args()
    config = load_json(args.config)
    configure_logging(config.get("output", {}).get("log", "logs/price_monitor.log"))
    logging.info("Price Monitor started")
    if run(config) is None:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
