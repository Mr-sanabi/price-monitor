import logging

from bs4 import BeautifulSoup

def extract_title(html: str) -> str | None:

    logging.info("Extracting page title")
    soup = BeautifulSoup(html, "html.parser")

    title_element = soup.find("title")

    if title_element is None:
        return None
    
    return title_element.get_text(strip=True) 

def extract_price(html: str, price_selector) -> str | None:

    logging.info("Extracting raw price")
    soup = BeautifulSoup(html, "html.parser")

    price_element = soup.select_one(price_selector)

    if price_element is None:
        return None
    
    return price_element.get_text(strip=True) 
