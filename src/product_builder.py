def build_product_data(
    product_url,
    product_title,
    current_price,
    target_price,
    currency,
    target_price_status,
    checked_at,
    previous_price,
    price_change,
    price_change_status
):
    return {
        "product_url": product_url,
        "product_title": product_title,
        "current_price": current_price,
        "target_price": target_price,
        "currency": currency,
        "target_price_status": target_price_status,
        "checked_at": checked_at,
        "previous_price": previous_price,
        "price_change": price_change,
        "price_change_status": price_change_status,
    }