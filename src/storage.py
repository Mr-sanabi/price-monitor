import json
import csv
import logging
import os
from pathlib import Path

def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
    
def save_json(filename, data):
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    temporary.replace(path)
    
def save_csv(filename, data):
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
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
    except TypeError:
        logging.error("Previous price data has an invalid structure")
        return None
