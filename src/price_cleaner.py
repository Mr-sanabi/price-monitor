import re

def clean_price(dirty_price):
    
    clean_price = re.sub(r"[^\d.,]", "", dirty_price) 
    clean_price = clean_price.replace(",", ".").replace(" ", "")
    return float(clean_price)



