import requests 
import time
import logging

def fetch_page(url: str, config: dict) -> str | None:
    delay = config["scraping"]["delay"]
    try:
        time.sleep(delay)
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None

    if response.status_code != 200:
        logging.error(f"Bad status code: {response.status_code}")
        return None
    
    logging.info(f"Page fetch successfully: {url}")
    return response.text