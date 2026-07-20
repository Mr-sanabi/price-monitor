import re

def clean_price(dirty_price):
    if dirty_price is None:
        raise ValueError("Price is missing")

    value = re.sub(r"[^\d,.-]", "", str(dirty_price))
    if not value:
        raise ValueError("Price does not contain a number")

    if "," in value and "." in value:
        decimal = "," if value.rfind(",") > value.rfind(".") else "."
        thousands = "." if decimal == "," else ","
        value = value.replace(thousands, "").replace(decimal, ".")
    elif value.count(",") == 1:
        integer, fraction = value.split(",")
        value = integer + fraction if len(fraction) == 3 else integer + "." + fraction
    elif value.count(",") > 1:
        parts = value.split(",")
        value = "".join(parts[:-1]) + "." + parts[-1]
    elif value.count(".") == 1:
        integer, fraction = value.split(".")
        value = integer + fraction if len(fraction) == 3 else value
    elif value.count(".") > 1:
        parts = value.split(".")
        value = "".join(parts[:-1]) + "." + parts[-1]

    return float(value)

