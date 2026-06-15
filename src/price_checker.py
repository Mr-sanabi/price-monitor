def price_compare(current_price, target_price):
    if current_price > target_price:
        return "above"
    elif current_price < target_price:
        return "below"
    elif current_price == target_price:
        return "equal"

def compare_previous_price(current_price, previous_price):
    price_change = None
    price_change_status = "unknown"

    if previous_price is None:
        return price_change, price_change_status
    
    price_change = current_price - previous_price

    if current_price > previous_price :
        price_change_status = "increased"
    elif current_price < previous_price:
        price_change_status = "decreased"
    else: 
        price_change_status = "unchanged"

    return price_change, price_change_status