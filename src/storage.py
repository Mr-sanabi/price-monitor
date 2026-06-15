import json
import csv
import logging
import os

def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
    
def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        return json.dump(data, file, indent=4, ensure_ascii=False)
    
def save_csv(filename, data):
    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="", encoding="utf-8") as file:
        fields = data.keys()
        writer = csv.DictWriter(file, fieldnames=fields)

        if not file_exists:
            writer.writeheader()
        
        writer.writerow(data)

def load_previous_price(filename):
    try:
        previous_data = load_json(filename)
        if previous_data is not None:
            return previous_data["current_price"]
    except FileNotFoundError:
        logging.error("File with previous price not found")
        return None
    except json.JSONDecodeError:
        logging.error("Invalid json file error")
        return None
    except KeyError:
        logging.error("Previous price data does not contain current_price")
        return None