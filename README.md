# Price Monitor

A configuration-driven Python monitor that extracts a product price, compares it with previous state, and records price history.

## Pipeline

1. Fetch a configured product page with timeout and HTTP validation.
2. Extract the title and price with a CSS selector.
3. Normalize common currency and thousands separators.
4. Compare the current, previous, and target prices.
5. Atomically save current state and append a CSV history row.

## Setup

```bash
python -m pip install -r requirements.txt
cp config_example.json config.json
python -m src.main --config config.json
```

`config.json` is intentionally ignored because it contains local selectors and settings.

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Reliability

- failed fetches do not overwrite the last known price;
- state writes use a temporary file followed by replacement;
- output and log directories are created automatically;
- timestamps are stored in UTC.

## Stack

Python 3.11+, Requests, Beautiful Soup, JSON, CSV, pytest.
